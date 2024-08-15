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
    headers = {
        "User-Agent": "python:api.subscriber.counter:v1.0.0 (by /u/Virtual-Tap-6806)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check for a 404 status code indicating the subreddit does not exist
        if response.status_code == 404:
            return 0
        
        # Raise an HTTPError for bad responses (4xx and 5xx)
        response.raise_for_status()
        
        # Extract JSON data from the response
        data = response.json().get("data", {})
        
        # Return the number of subscribers, defaulting to 0 if not present
        return data.get("subscribers", 0)
    
    except requests.RequestException as e:
        # Print the exception if needed for debugging
        print(f"An error occurred: {e}")
        return 0
