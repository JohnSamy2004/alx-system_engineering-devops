#!/usr/bin/python3
"""Module to query the number of subscribers of a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers for a given subreddit."""
    base_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "python:api.subscriber.counter:v1.0.0 (by /u/your_username)"
    }
    
    try:
        response = requests.get(base_url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        data = response.json().get("data", {})
        return data.get("subscribers", 0)
    except requests.RequestException:
        return 0
