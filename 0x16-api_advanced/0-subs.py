#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests  # Import the requests library for making HTTP requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.
        
    Returns:
        int: The number of subscribers for the subreddit. Returns 0 if the subreddit is invalid or not found.
    """
    # Construct the URL to fetch subreddit information using the given subreddit name
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    # Set up headers to include a User-Agent to avoid request rejection
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    
    # Make a GET request to the specified URL with the custom headers and no redirects
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # If the status code is 404, the subreddit does not exist or is invalid, so return 0
    if response.status_code == 404:
        return 0
    
    # Extract the JSON data from the response and get the number of subscribers
    results = response.json().get("data")
    
    # Return the number of subscribers from the data
    return results.get("subscribers")
