from datetime import datetime, timedelta
from src.db.models import GitHubEvent, SessionLocal
import json

def get_recent_events(days=7):
    session = SessionLocal()
    since = datetime.utcnow() - timedelta(days=days)
    events = session.query(GitHubEvent).filter(GitHubEvent.created_at >= since).all()
    result = []
    for event in events:
        result.append({
            'id': event.id,
            'event_type': event.event_type,
            'repo': event.repo,
            'author': event.author,
            'data': json.loads(str(event.data)),
            'created_at': event.created_at.isoformat()
        })
    session.close()
    return result 