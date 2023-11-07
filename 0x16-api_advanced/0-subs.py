#!/usr/bin/python3
""" a script to query Reddit API and returns the number of subscribers """

import requests


def number_of_subscribers(subreddit) -> int:
    """
    Queries the Reddit API and returns the number of subscribers
    """

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    try:
        response = requests.get(url, headers={'User-Agent': 'Agent Sunny'})
        results = respones.json()

        return results['data']['subscribers']
    except Exception:
        return 0
