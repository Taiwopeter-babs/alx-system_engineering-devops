#!/usr/bin/python3
"""This module queries the reddit API"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """This function queries the reddit API for number
    of subscribers of a subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Python/requests"}

    try:
        req = requests.get(url, headers=headers, allow_redirects=False)

        if req.status_code == 200:
            data = req.json()
            return data.get("data")["subscribers"]
        else:
            return 0
    except requests.exceptions.JSONDecodeError:
        pass
