#!/usr/bin/python3
"""Module to query the number of subscribers of a given Reddit subreddit."""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers for the subreddit. Returns 0 if the subreddit is invalid or not found.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "youBot/1.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the subreddit is not found or redirected
        if response.status_code in [301, 404]:
            return 0
        
        # Raise an HTTPError for other bad responses (4xx and 5xx)
        response.raise_for_status()
        
        # Extract JSON data from the response
        data = response.json().get("data", {})
        
        # Return the number of subscribers, defaulting to 0 if not present
        return data.get("subscribers", 0)
    
    except requests.RequestException:
        # Return 0 if any request error occurs
        return 0

