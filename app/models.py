from sqlalchemy import Column, Integer, String, Text, DateTime, func
from app.database import Base

class Summary(Base):
    __tablename__ = "summaries"

    id = Column(Integer, primary_key=True, index=True)
    commit_hash = Column(String(50), index=True, unique=True)
    diff = Column(Text)
    summary = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
