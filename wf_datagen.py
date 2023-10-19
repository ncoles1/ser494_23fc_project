import os.path
import time
import requests
import csv
import wf_searchwords

# SER 494 - Data Science MS3
# Author: Nicolas Coles
# Date: 10/10/2023
# Description: This is a rudimentary data scrape that parses Reddit's r/League of Legends subreddit
#               in order to find the main reasons for toxicity and hate in the game. Because I have not yet
#               learned how to use machine learning, this will use a rudimentary way of classifying toxic posts.

# Function to scrape Reddit posts (for different categories)


def reddit_scrape(subreddit, category, after='', data_list=None):
    url_template = 'https://www.reddit.com/r/{}/{}.json?{}'
    headers = {
        'User-Agent': 'NCCGaming'
    }

    params = ''
    if category == 'top':
        params += '/?t=all/'
    params += f'&after={after}' if after else ''

    while True:
        url = url_template.format(subreddit, category, params)
        response = requests.get(url, headers=headers)

        if response.ok:
            try:
                data = response.json()['data']
            except requests.exceptions.JSONDecodeError as e:
                print("JSON error: {e}")
                continue

            for post in data['children']:
                post_data = post['data']

                title = post_data['title']
                content = post_data['selftext']

                # Check if any keywords are present in the title or content
                if any(keyword in title.lower() or keyword in content.lower()
                       for keyword in wf_searchwords.search_words):
                    author = post_data['author']
                    date = post_data['created_utc']
                    url = post_data.get('url')
                    upvotes = post_data['score']
                    num_comments = post_data['num_comments']

                    data_list.append({
                        'Category': category,
                        'Title': title,
                        'Content': content,
                        'Author': author,
                        'Date': date,
                        'Upvotes': upvotes,
                        'Comment_Count': num_comments,
                        'URL': url
                    })

                    print(f'Category: {category}')
                    print(f'Title: {title}')
                    print(f'Author: {author}')
                    print(f'Date: {date}')
                    print(f'Upvotes: {upvotes}')
                    print(f'Comment Count {num_comments}')
                    print(f'URL: {url}')
                    print('---------------------')
            return data['after']

        elif response.status_code == 429:
            print("Max limit reached, waiting one minute...")
            time.sleep(60)
            continue
        else:
            print(f'Error {response.status_code}')
            return None


# Function to save data to a CSV file
def save_to_csv(data_list):
    csv_path = os.path.join('data_original', 'reddit_data.csv')
    with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Category', 'Title', 'Content', 'Author', 'Date', 'Upvotes', 'Comment_Count', 'URL']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for data in data_list:
            writer.writerow(data)
        print('Data has been saved to data_original')


def main():
    subreddit = 'leagueoflegends'
    categories = ['new', 'hot', 'top']
    data_list = []

    for category in categories:
        after = ''
        while True:
            after = reddit_scrape(subreddit, category, after, data_list)
            if not after:
                break

    save_to_csv(data_list)



