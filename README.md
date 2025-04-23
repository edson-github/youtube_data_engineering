# YouTube Data Engineering Projects Scraper

This project scrapes YouTube for data engineering project videos using the YouTube Data API v3.

## Setup

1. Create a virtual environment:
```python
python3 -m venv venv
source venv/bin/activate

2. Install the required packages:
pip install -r requirements.txt

3. Set up your YouTube Data API v3 credentials:
Create a project in the Google Cloud Console.
Enable the YouTube Data API v3 for your project.
Create credentials for the YouTube Data API v3.
Download the JSON key file and save it as `client_secret.json`.

4. Run the scraper:
python main.py