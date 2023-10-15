import pandas as pd
import wf_searchwords
import re

categories = {
    "Bad Teammates": {
        "keywords": ["teammates", "feed", "int", "afk", "noob", "team", "troll", "running it down", "run it down",
                     "ran it down", "inting", "griefing", "useless", "carried", "carry", "report", "toxic"],
        "weight": 2
    },
    "Champion Design": {
        "keywords": ["redesign", "rework", "kit", "permaban", "nerf", "buff", "op", "overpowered", "underpowered", "unbalanced", "winrate",
                     "win rate", "ban rate", "unplayable", "counterplay", "meta champ"],
        "weight": 2
    },
    "Game Balance": {
        "keywords": ["lane", "balance", "overpowered", "underpowered", "item", "mythic"],
        "weight": 1
    },
    "Losing Streaks" : {
        "keywords": ["losing streak", "keep losing", "frustrated", "frustration"],
        "weight": 1
    },
    "Ranked Pressure": {
        "keywords": ["elo hell", "low elo", "lp", "elo", "rank up", "lp gain", "lp loss", "win", "mmr"],
        "weight": 3
    },
    "Toxicity from Others": {
        "keywords": ["toxic teammate", "toxicity", "toxic", "flaming"],
        "weight": 2
    },
    "Communication Issues": {
        "keywords": ["communication", "coordination", "listen"],
        "weight": 1
    }
}

csv_path = 'data_original/reddit_data.csv'
df = pd.read_csv(csv_path)

df['Content'].fillna('', inplace=True)
df['Content'] = df['Content'].str.lower()
df['Title'] = df['Title'].str.lower()

# Remove punctuation from content and title
df['Content'] = df['Content'].apply(lambda x: re.sub(r'[^\w\s]', '', x))
df['Title'] = df['Title'].apply(lambda x: re.sub(r'[^\w\s]', '', x))

# Create a dictionary to store category counts
category_counts = {category: 0 for category in categories}
category_counts['Uncategorized'] = 0


def categorize_post(row):
    post_category = "Uncategorized"
    max_weight = 0

    for category, details in categories.items():
        keywords = details["keywords"]
        weight = details["weight"]

        keyword_count = sum(keyword in row['Title'] or keyword in row['Content'] for keyword in keywords)

        if keyword_count * weight > max_weight:
            post_category = category
            max_weight = keyword_count * weight

    category_counts[post_category] += 1
    return post_category


df['Category'] = df.apply(categorize_post, axis=1)

# Save categorized data to a new CSV
categorized_csv_path = 'data_original/categorized_reddit_data.csv'
df.to_csv(categorized_csv_path, index=False)

for category, count in category_counts.items():
    print(f"{category}: {count} posts")
