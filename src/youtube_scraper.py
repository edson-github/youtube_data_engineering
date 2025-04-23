from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pandas as pd
from config import YOUTUBE_API_KEY, SEARCH_QUERY, MAX_RESULTS

def create_youtube_client():
    """Create YouTube API client."""
    return build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

def search_videos():
    """Search for videos related to data engineering projects."""
    try:
        youtube = create_youtube_client()
        
        request = youtube.search().list(
            part='snippet',
            q=SEARCH_QUERY,
            type='video',
            maxResults=MAX_RESULTS,
            relevanceLanguage='en',
            order='relevance'
        )
        
        response = request.execute()
        
        videos = []
        for item in response['items']:
            video = {
                'title': item['snippet']['title'],
                'description': item['snippet']['description'],
                'published_at': item['snippet']['publishedAt'],
                'channel_title': item['snippet']['channelTitle'],
                'video_id': item['id']['videoId'],
                'video_url': f"https://www.youtube.com/watch?v={item['id']['videoId']}"
            }
            videos.append(video)
            
        return pd.DataFrame(videos)
    
    except HttpError as e:
        print(f'An HTTP error {e.resp.status} occurred: {e.content}')
        return None

def get_video_statistics(df):
    """Get additional statistics for each video."""
    try:
        youtube = create_youtube_client()
        
        video_stats = []
        for video_id in df['video_id']:
            request = youtube.videos().list(
                part='statistics',
                id=video_id
            )
            response = request.execute()
            
            if response['items']:
                stats = response['items'][0]['statistics']
                stats['video_id'] = video_id
                video_stats.append(stats)
        
        stats_df = pd.DataFrame(video_stats)
        return df.merge(stats_df, on='video_id')
    
    except HttpError as e:
        print(f'An HTTP error {e.resp.status} occurred: {e.content}')
        return None

def main():
    # Search for videos
    videos_df = search_videos()
    if videos_df is not None:
        # Get video statistics
        final_df = get_video_statistics(videos_df)
        if final_df is not None:
            # Save results to CSV
            final_df.to_csv('data_engineering_projects.csv', index=False)
            print(f"Successfully scraped {len(final_df)} videos!")
            print("Results saved to 'data_engineering_projects.csv'")

if __name__ == "__main__":
    main()