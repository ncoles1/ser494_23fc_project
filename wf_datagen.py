from pprint import pprint
import requests
import re
# SER 494 - Data Science MS3
# Author: Nicolas Coles
# Date: 10/10/2023
# Description: This is a rudimentary data scrape that parses Reddit's r/League of Legends subreddit
#               in order to find the main reasons for toxicity and hate in the game. Because I have not yet
#               learned how to use machine learning, this will use a rudimentary way of classifying toxic posts.


def reddit_scrape(subreddit, after=''):
    url_template = 'https://www.reddit.com/r/{}/top.json?t=all{}'
    headers = {
        'User-Agent': 'NCCGaming'
    }

    params = f'&after={after}' if after else ''

    toxic_keywords = ["complain", "teammates", "champion", "item", "balance", "broken"]

    while True:
        url = url_template.format(subreddit, params)
        response = requests.get(url, headers=headers)

        if response.ok:
            data = response.json()['data']
            for post in data['children']:
                post_data = post['data']
                title = post_data['title']
                author = post_data['author']
                date = post_data['created_utc']
                url = post_data.get('url')
                upvotes = post_data['score']
                content = post_data['selftext']

                print(f'Title: {title}')
                print(f'Author: {author}')
                print(f'Date: {date}')
                print(f'Upvotes: {upvotes}')
                print(f'URL: {url}')
                print('---------------------')
            return data['after']
        else:
            print(f'Error {response.status_code}')
            return None


def main():
    subreddit = 'leagueoflegends'
    after = ''
    while True:
        after = reddit_scrape(subreddit, after)
        if not after:
            break  # Stop if end is reached


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Finished')
