#!/usr/bin/python3
""" script to query Reddit API """

import requests


def recurse(subreddit, hot_list=[], after=None, max_pages=None):
    """
    recursive query Reddit API and returns a list
    """
    if max_pages is not None and max_pages <= 0:
        return hot_list  # Base case: Stop when max_pages is reached or None

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'after': after} if after else {}

    response = requests.get(
        url,
        params=params,
        headers={'User-Agent': 'Agent Sunny'},

        allow_redirects=False
    )

    if response.status_code != 200:
        return None

    results = response.json()
    posts = results.get('data', {}).get('children', [])

    for post in posts:
        hot_list.append(post['data']['title'])

    next_page = results.get('data', {}).get('after')
    if next_page:
        return recurse(

            subreddit, hot_list, after=next_page, max_pages=max_pages
        )

    return hot_list if len(hot_list) > 0 else None
