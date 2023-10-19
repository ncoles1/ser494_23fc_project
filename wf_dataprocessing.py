import datetime

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
        "keywords": ["redesign", "rework", "kit", "permaban", "nerf", "buff", "op", "overpowered", "underpowered",
                     "unbalanced", "winrate", "win rate", "ban rate", "unplayable", "counterplay", "meta champ",
                     "champion balance", "champion design", "champion rework"],
        "weight": 2
    },
    "Game Balance": {
        "keywords": ["lane", "balance", "overpowered", "underpowered", "item", "mythic", "jungle", "top", "bot",
                     "mid", "adc", "sup"],
        "weight": 1
    },
    "Losing Streaks": {
        "keywords": ["losing streak", "keep losing", "frustrated", "frustration", "losing games",
                     "losing streak", "losers queue", "losing"],
        "weight": 1
    },
    "Ranked Pressure": {
        "keywords": ["elo hell", "low elo", "lp", "rank up", "lp gain", "lp loss", "win",
                     "mmr", "hardstuck", "stuck"],
        "weight": 2
    },
    "Toxicity from Others": {
        "keywords": ["toxic teammate", "toxicity", "toxic", "flaming", "report", "toxic players", "mute", "abuse",
                     "harrasment", "harass", "negative attitude", "raging", "insult"],
        "weight": 2
    },
    "Communication Issues": {
        "keywords": ["communication", "coordination", "listen", "voice chat", "ping", "no comm", "shotcall"],
        "weight": 1
    }
}


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


def main():
    csv_path = 'data_original/reddit_data.csv'
    df = pd.read_csv(csv_path)

    df['Content'].fillna('', inplace=True)
    df['Content'] = df['Content'].str.lower()
    df['Title'] = df['Title'].str.lower()

    # Remove punctuation from content and title, change date from seconds to datetime format.
    df['Content'] = df['Content'].apply(lambda x: re.sub(r'[^\w\s]', '', x))
    df['Title'] = df['Title'].apply(lambda x: re.sub(r'[^\w\s]', '', x))
    df['Date'] = df['Date'].apply(
        lambda timestamp: datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'))

    df['Category'] = df.apply(categorize_post, axis=1)

    categorized_csv_path = 'data_processed/categorized_reddit_data.csv'
    df.to_csv(categorized_csv_path, index=False)

    for category, count in category_counts.items():
        print(f"{category}: {count} posts")
