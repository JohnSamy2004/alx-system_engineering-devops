#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    # Define the URL for the subreddit's about.json endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set up the headers with a custom User-Agent
    headers = {'User-Agent': 'myRedditApp/0.1'}
    
    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the response is valid (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Return the number of subscribers
            return data['data']['subscribers']
        else:
            # If the subreddit does not exist or other error occurred, return 0
            return 0
    
    except requests.RequestException:
        # Handle any request exceptions and return 0
        return 0
