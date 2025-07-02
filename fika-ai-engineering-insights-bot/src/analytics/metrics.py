from datetime import datetime, timedelta
import json

def calculate_dora_metrics(events):
    pr_events = [e for e in events if e['event_type'] == 'pull_request']
    if not pr_events:
        return {
            'lead_time': 'N/A',
            'deploy_frequency': 'N/A',
            'change_failure_rate': 'N/A',
            'mttr': 'N/A'
        }
    # Lead time: avg time from PR created_at to merged_at
    lead_times = []
    deploys = 0
    fix_prs = 0
    fix_mttrs = []
    for pr in pr_events:
        data = pr['data']
        created = data.get('created_at')
        merged = data.get('merged_at')
        if created and merged:
            created_dt = datetime.strptime(created, "%Y-%m-%dT%H:%M:%SZ")
            merged_dt = datetime.strptime(merged, "%Y-%m-%dT%H:%M:%SZ")
            lead_time = (merged_dt - created_dt).total_seconds() / 3600  # hours
            lead_times.append(lead_time)
            deploys += 1
            if 'fix' in data.get('title', '').lower():
                fix_prs += 1
                fix_mttrs.append(lead_time)
    lead_time_avg = round(sum(lead_times) / len(lead_times), 2) if lead_times else 'N/A'
    deploy_frequency = deploys  # per week (assuming events are for a week)
    change_failure_rate = f"{round((fix_prs / deploys) * 100, 1)}%" if deploys else 'N/A'
    mttr = round(sum(fix_mttrs) / len(fix_mttrs), 2) if fix_mttrs else 'N/A'
    return {
        'lead_time': f"{lead_time_avg} hours" if lead_time_avg != 'N/A' else 'N/A',
        'deploy_frequency': f"{deploy_frequency} PRs/week",
        'change_failure_rate': change_failure_rate,
        'mttr': f"{mttr} hours" if mttr != 'N/A' else 'N/A'
    } 