from sqlalchemy.orm import Session
from app.models import Summary

def save_summary(db: Session, commit_hash: str, diff: str, summary: str):
    db_summary = Summary(
        commit_hash=commit_hash,
        diff=diff,
        summary=summary
    )
    db.add(db_summary)
    db.commit()
    db.refresh(db_summary)
    return db_summary
