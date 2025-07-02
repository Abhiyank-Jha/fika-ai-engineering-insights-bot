import os
# NOTE: You must install slack_bolt for these imports to resolve
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from src.agents.data_harvester import get_recent_events
from src.agents.diff_analyst import analyze_churn
from src.agents.insight_narrator import generate_narrative
from src.viz.charts import plot_churn_bar_chart

SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN", "xoxb-your-bot-token")
SLACK_APP_TOKEN = os.environ.get("SLACK_APP_TOKEN", "xapp-your-app-token")

app = App(token=SLACK_BOT_TOKEN)

@app.command("/dev-report")
def handle_dev_report(ack, respond, command, client):
    ack()
    events = get_recent_events()
    churn_summary = analyze_churn(events)
    report = generate_narrative(churn_summary, events=events)
    chart_path = plot_churn_bar_chart(churn_summary)
    # Upload the chart image
    with open(chart_path, "rb") as f:
        client.files_upload(
            channels=command["channel_id"],
            file=f,
            title="Code Churn by Author",
            initial_comment="*Engineering Productivity Report Chart*"
        )
    # Respond with the narrative
    respond(f"*Engineering Productivity Report:*\n```{report['narrative']}```")

if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start() 