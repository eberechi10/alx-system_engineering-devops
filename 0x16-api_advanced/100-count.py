#!/usr/bin/python3
""" script to query Reddit API """

import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """queries the Reddit API, based on order of count,
    """
    if after is None:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    else:
        url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
            subreddit, after
        )

    headers = {'User-Agent': 'Agent Sunny'}
    params = {'after': after} if after else {}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        return

    results = response.json()
    posts = results.get('data', {}).get('children', [])

    for post in posts:
        title = post['data']['title'].lower()

        for keywd in wd_list:
            keywd = keywd.lower()
            if (
                keywd in title
                and not title.startswith(keywd + '.')
                and not title.startswith(keywd + '!')

                and not title.startswith(keywd + '_')
            ):
                counts[keywd] = counts.get(keywd, 0) + 1

    next_page = results.get('data', {}).get('after')
    if next_page:
        count_wds(subreddit, wd_list, after=next_page, counts=counts)
    else:
        sorted_counts = sorted(
            counts.items(), key=lambda item: (-item[1], item[0])
        )
        for wd, count in sorted_counts:
            print("{}: {}".format(wd, count))
