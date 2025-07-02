from collections import defaultdict

def analyze_churn(events):
    """
    Aggregates churn stats per author and flags outliers.
    Args:
        events: List of event dicts from Data Harvester.
    Returns:
        {
            'per_author': {author: {'additions': int, 'deletions': int, 'files': int, 'commits': int}},
            'outliers': [author, ...]
        }
    """
    churn = defaultdict(lambda: {'additions': 0, 'deletions': 0, 'files': 0, 'commits': 0})
    for event in events:
        if event['event_type'] == 'commit':
            stats = event['data'].get('stats', {})
            churn[event['author']]['additions'] += stats.get('additions', 0)
            churn[event['author']]['deletions'] += stats.get('deletions', 0)
            churn[event['author']]['files'] += len(event['data'].get('files', []))
            churn[event['author']]['commits'] += 1
    # Flag outliers: authors with churn > 2x average
    all_churn = [v['additions'] + v['deletions'] for v in churn.values() if v['commits'] > 0]
    avg_churn = sum(all_churn) / len(all_churn) if all_churn else 0
    outliers = [author for author, stats in churn.items() if (stats['additions'] + stats['deletions']) > 2 * avg_churn and stats['commits'] > 0]
    return {'per_author': dict(churn), 'outliers': outliers} 