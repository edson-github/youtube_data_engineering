import os
from dotenv import load_dotenv

load_dotenv()

# YouTube API Configuration
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')

# Search Configuration
SEARCH_QUERY = 'data engineer projects portfolio'
MAX_RESULTS = 75  # Updated to fetch 75 results