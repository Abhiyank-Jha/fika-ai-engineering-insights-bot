# fika-ai-engineering-insights-bot

## 🚀 What This Bot Does

### 1. **Engineering Productivity Analytics**
- The bot analyzes GitHub activity (commits, pull requests) for your team or organization.
- It tracks key engineering metrics such as:
  - Number of commits and PRs
  - Code churn (lines added/deleted)
  - Per-author stats (who contributed what)
  - DORA metrics (lead time, deploy frequency, change failure rate, MTTR)

### 2. **AI-Powered Insights**
- Uses a modular agent architecture:
  - **Data Harvester**: Collects GitHub events (commits, PRs) from a database or directly from GitHub.
  - **Diff Analyst**: Aggregates code churn, flags outliers (e.g., unusually high activity), and links churn to potential defect risk.
  - **Insight Narrator**: Generates a human-readable summary and maps the data to business-relevant DORA metrics.

### 3. **Chat-First Output**
- The bot is integrated with Slack (or can be adapted for Discord).
- When you type `/dev-report` in Slack, the bot:
  - Posts a chart (PNG image) showing code churn by author.
  - Posts a text summary with key metrics and insights for the week.

### 4. **Easy to Run and Demo**
- Includes a seed script to generate fake GitHub data for instant demo/testing.
- Can be started with a single command using Docker Compose or by running Python scripts.

### 5. **For Teams and Leadership**
- Helps engineering leaders and teams understand:
  - Who is contributing most
  - Where code churn is highest (potential risk)
  - How the team is performing on industry-standard DORA metrics
  - Where to focus for process improvement

---

## 🟢 Typical Usage Flow

1. **Seed or ingest real GitHub data** (commits/PRs).
2. **Run the bot** (in Slack).
3. **Type `/dev-report`** in a Slack channel.
4. **Get an instant, visual, and narrative report** on your team’s engineering productivity.

---

## 🧑‍💻 Who Is This For?

- **Engineering managers** who want actionable insights.
- **Developers** who want to see their impact.
- **Organizations** looking to improve software delivery and team health.

---
