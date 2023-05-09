#!/usr/bin/python3
"""This module queries the reddit API"""
import requests
from sys import argv


def top_ten(subreddit):
    """This function queries the reddit API for number
    of subscribers of a subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    payload = {"limit": 10}
    headers = {"User-Agent": "Python/requests"}

    try:
        req = requests.get(url, headers=headers, params=payload,
                           allow_redirects=False)
        if req.status_code == 200:
            data = req.json()
            for post in data.get("data")["children"]:
                print("{}".format(post.get("data")["title"]))
                print()
        else:
            print(None)
    except requests.exceptions.JSONDecodeError:
        pass
