import matplotlib.pyplot as plt
import os

def plot_churn_bar_chart(churn_summary, output_path="churn_chart.png"):
    per_author = churn_summary.get('per_author', {})
    authors = list(per_author.keys())
    churn_values = [stats['additions'] + stats['deletions'] for stats in per_author.values()]
    plt.figure(figsize=(8, 4))
    plt.bar(authors, churn_values, color='skyblue')
    plt.xlabel('Author')
    plt.ylabel('Code Churn (Additions + Deletions)')
    plt.title('Code Churn by Author')
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    return os.path.abspath(output_path) 