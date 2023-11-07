#!/usr/bin/python3
""" a script to query Reddit API """

import requests


def top_ten(subreddit: str) -> None:
    """
    query Reddit API and prints the first 10 hot posts
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(
        url, headers={'User-Agent': 'Agent Sunny'}, allow_redirects=False
    )
    results = response.json()
    try:
        for i in range(10):
            print(results['data']['children'][i]['data']['title'])

    except Exception:
        print('None')
