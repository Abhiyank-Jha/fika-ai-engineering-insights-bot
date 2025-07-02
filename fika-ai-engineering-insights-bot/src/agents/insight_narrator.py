from src.analytics.metrics import calculate_dora_metrics

def generate_narrative(churn_summary, events=None):
    """
    Generate a narrative summary and DORA metrics from churn analysis.
    Args:
        churn_summary: Output from Diff Analyst (per_author, outliers)
        events: Full event list for DORA metrics
    Returns:
        {
            'narrative': str,
            'dora_metrics': dict
        }
    """
    per_author = churn_summary.get('per_author', {})
    outliers = churn_summary.get('outliers', [])
    lines = []
    lines.append("Engineering Productivity Report:")
    for author, stats in per_author.items():
        lines.append(f"- {author}: {stats['commits']} commits, {stats['additions']} additions, {stats['deletions']} deletions, {stats['files']} files changed.")
    if outliers:
        lines.append("")
        lines.append(f"⚠️ Outlier(s) detected: {', '.join(outliers)} (high code churn)")
    else:
        lines.append("No code churn outliers detected.")
    # Real DORA metrics
    dora_metrics = calculate_dora_metrics(events or [])
    lines.append("")
    lines.append("DORA Metrics:")
    for k, v in dora_metrics.items():
        lines.append(f"- {k.replace('_', ' ').title()}: {v}")
    return {
        'narrative': '\n'.join(lines),
        'dora_metrics': dora_metrics
    } 