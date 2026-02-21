# Q&A history model
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.db.database import Base

class QAHistory(Base):
    __tablename__ = "qa_history"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
