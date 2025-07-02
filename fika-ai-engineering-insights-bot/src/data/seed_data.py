import json
from datetime import datetime, timedelta
from src.db.models import GitHubEvent, init_db, SessionLocal

def seed_fake_github_events():
    session = SessionLocal()
    now = datetime.utcnow()
    fake_events = [
        GitHubEvent(
            event_type="commit",
            repo="demo/repo",
            author="alice",
            data=json.dumps({
                "sha": "abc123",
                "commit": {
                    "author": {"name": "alice", "date": (now - timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")},
                    "message": "Initial commit"
                },
                "stats": {"additions": 100, "deletions": 0, "total": 100},
                "files": [{"filename": "main.py", "additions": 100, "deletions": 0}]
            }),
            created_at=now - timedelta(days=1)
        ),
        GitHubEvent(
            event_type="commit",
            repo="demo/repo",
            author="bob",
            data=json.dumps({
                "sha": "def456",
                "commit": {
                    "author": {"name": "bob", "date": (now - timedelta(hours=12)).strftime("%Y-%m-%dT%H:%M:%SZ")},
                    "message": "Add feature X"
                },
                "stats": {"additions": 50, "deletions": 10, "total": 60},
                "files": [{"filename": "feature.py", "additions": 50, "deletions": 10}]
            }),
            created_at=now - timedelta(hours=12)
        ),
        GitHubEvent(
            event_type="pull_request",
            repo="demo/repo",
            author="carol",
            data=json.dumps({
                "number": 1,
                "title": "Fix bug Y",
                "user": {"login": "carol"},
                "created_at": (now - timedelta(hours=6)).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "merged_at": (now - timedelta(hours=2)).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "additions": 20,
                "deletions": 5,
                "changed_files": 2
            }),
            created_at=now - timedelta(hours=6)
        )
    ]
    session.add_all(fake_events)
    session.commit()
    session.close()
    print("Seeded fake GitHub events.")

if __name__ == "__main__":
    init_db()
    seed_fake_github_events() 