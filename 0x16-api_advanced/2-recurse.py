#!/usr/bin/python3
"""This module queries the reddit API"""
import requests
from sys import argv


def recurse(subreddit, hot_list=[], after=None):
    """This function queries the reddit API for number
    of subscribers of a subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    payload = {"after": after, "limit": 100}
    headers = {"User-Agent": "Python/requests"}

    try:
        req = requests.get(url, headers=headers, params=payload,
                           allow_redirects=False)
        if req.status_code == 200:
            data = req.json()
            after = data.get("data")["after"]
            for post in data.get("data")["children"]:
                hot_list.append(post.get("data")["title"])
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.exceptions.JSONDecodeError:
        pass
