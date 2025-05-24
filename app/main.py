from fastapi import FastAPI, Body, HTTPException ,Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from app.summarizer import get_chain, summarize_diff
from app.database import SessionLocal
from app.crud import save_summary
from pydantic import BaseModel

from app.models import Base ,Summary
from app.database import engine

Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="templates")

app = FastAPI()

class DiffRequest(BaseModel):
    diff: str
    commit_hash: str
    groq_api_key: str



@app.post("/summarize")
def summarize(request: DiffRequest):
    try:
        chain = get_chain(request.groq_api_key)
        summary = chain.invoke({"diff": request.diff})
        db = SessionLocal()
        save_summary(db, request.commit_hash, request.diff, summary)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    db = SessionLocal()
    summaries = db.query(Summary).order_by(Summary.created_at.desc()).all()
    return templates.TemplateResponse("summaries.html", {"request": request, "summaries": summaries})