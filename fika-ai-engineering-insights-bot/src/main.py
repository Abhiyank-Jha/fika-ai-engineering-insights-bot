# To run: python -m src.main
from src.agents.data_harvester import get_recent_events
from src.agents.diff_analyst import analyze_churn
from src.agents.insight_narrator import generate_narrative

def main():
    print("FIKA AI Engineering Insights Bot starting...")
    events = get_recent_events()
    churn_summary = analyze_churn(events)
    report = generate_narrative(churn_summary, events=events)
    print("\n=== Engineering Productivity Report ===\n")
    print(report['narrative'])

if __name__ == "__main__":
    main() 