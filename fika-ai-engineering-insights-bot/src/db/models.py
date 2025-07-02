from sqlalchemy import Column, Integer, String, DateTime, Text, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

Base = declarative_base()

class GitHubEvent(Base):
    __tablename__ = 'github_events'
    id = Column(Integer, primary_key=True)
    event_type = Column(String, nullable=False)
    repo = Column(String, nullable=False)
    author = Column(String, nullable=False)
    data = Column(Text, nullable=False)  # JSON as string
    created_at = Column(DateTime, default=datetime.utcnow)

class Metric(Base):
    __tablename__ = 'metrics'
    id = Column(Integer, primary_key=True)
    author = Column(String, nullable=False)
    metric_type = Column(String, nullable=False)  # e.g., 'commits', 'pr_throughput'
    value = Column(Integer, nullable=False)
    period = Column(String, nullable=False)  # e.g., 'daily', 'weekly', 'monthly'
    calculated_at = Column(DateTime, default=datetime.utcnow)

class PromptLog(Base):
    __tablename__ = 'prompt_logs'
    id = Column(Integer, primary_key=True)
    agent = Column(String, nullable=False)
    prompt = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

# Database setup helper
DATABASE_URL = 'sqlite:///fika_ai.db'
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine) 