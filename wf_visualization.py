import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

import wf_dataprocessing
import wf_searchwords


def main():
    categorized_csv_path = 'data_processed/categorized_reddit_data.csv'
    df = pd.read_csv(categorized_csv_path)

    selected_features = ['Upvotes', 'Date', 'Category', 'Comment_Count']
    stats_data = []

    for feature in selected_features:
        if feature == 'Category':
            most_freq = df[feature].value_counts().head(1).index.tolist()
            least_freq = df[feature].value_counts().tail(1).index.tolist()

            stats_data.append({
                'Feature': 'Toxicity Category',
                'Min': 'N/A',
                'Max': 'N/A',
                'Median': 'N/A',
                'Number of Categories: ': df[feature].nunique(),
                'Most Frequent Category: ': ', '.join(most_freq),
                'Least Frequent Category: ': ', '.join(least_freq)
            })
        elif feature == "Date":
            median_index = len(df[feature]) // 2
            stats_data.append({
                'Feature': feature,
                'Min': df[feature].min(),
                'Max': df[feature].max(),
                'Median': df[feature][median_index]
            })

        else:
            stats_data.append({
                'Feature': feature,
                'Min': df[feature].min(),
                'Max': df[feature].max(),
                'Median': df[feature].median()
            })

    keyword_counts = {keyword: df['Content'].str.count(keyword).sum() + df['Title'].str.count(keyword).sum()
                      for keyword in wf_searchwords.search_words}

    keyword_counts_values = list(keyword_counts.values())
    stats_data.append({
        'Feature': 'Keywords',
        'Min': min(keyword_counts_values),
        'Max': max(keyword_counts_values),
        'Median': sum(keyword_counts_values) / len(keyword_counts_values)
    })

    # Create the stats matrix
    stats_matrix = pd.DataFrame(stats_data)

    summary_file = 'data_processed/summary.txt'

    stats_matrix.to_csv(summary_file, sep='\t', index=False)
    print("Summary saved to data_processed/summary.txt")

    df['Date'] = pd.to_datetime(df['Date']).astype('int64') // 10**9

    quant_features = ['Upvotes', 'Comment_Count', 'Date']
    quant_df = df[quant_features]
    qualitative_features = ['Category']

    correlation_matrix = quant_df.corr()
    print(correlation_matrix)

    output_path = 'visuals/'

    stats_matrix.to_csv(summary_file, sep='\t', index=False)
    with open(summary_file, 'a') as f:
        f.write("\n")
        f.write(correlation_matrix.to_string())
    print("Summary saved to data_processed/summary.txt")

    # Create scatter plots for quantitative features
    for i in range(len(quant_features)):
        for j in range(i + 1, len(quant_features)):
            feature1 = quant_features[i]
            feature2 = quant_features[j]

            plt.scatter(df[feature1], df[feature2], label=f'{feature1} vs {feature2}')
            plt.grid(True)
            plt.xlabel(feature1)
            plt.ylabel(feature2)
            plt.title(f'{feature1} vs {feature2}')
            plt.legend()
            plt.savefig(f'{output_path}{feature1}_{feature2}_scatter.png')
            plt.close()

    # Histograms for qualitative features
    for feature in qualitative_features:
        plt.figure()
        value_counts = df[feature].value_counts()
        value_counts.plot(kind='bar', color='skyblue', label=feature)
        plt.xticks(rotation=45, ha='right')

        plt.xlabel(feature)
        plt.ylabel('Count')
        plt.title(f'Histogram of {feature}')
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f'{output_path}{feature}_histogram.png')
        plt.close()

    print("Graphs saved to the visuals directory.")
