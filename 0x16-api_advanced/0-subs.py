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
        "User-Agent": "linux:api.subscriber.counter:v1.0.0 (by /u/Virtual-Tap-6806)"
    }

    try:
        # Perform a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the response status code indicates an error
        if response.status_code == 404:
            return 0
        
        # Check for other HTTP error status codes
        response.raise_for_status()
        
        # Extract the JSON data from the response
        data = response.json().get("data", {})
        
        # Return the number of subscribers, default to 0 if not present
        return data.get("subscribers", 0)
    
    except requests.RequestException:
        # Catch any request-related errors and return 0
        return 0
