from googleapiclient.discovery import build


class Video:

    def __init__(self, video_id):
        self.video_id = video_id
        self.fetch_video_info()

    def fetch_video_info(self):
        service = build('youtube', 'v3', developerKey="AIzaSyBaOVsm5nVNANKOv0JL_joAFxW0a6Zm9QE")
        video_response = service.videos().list(part='snippet, statistics', id=self.video_id).execute()
        self.title = video_response['items'][0]['snippet']['title']
        self.video_link = f"https://youtu.be/{self.video_id}"
        self.view_count = video_response['items'][0]['statistics']['viewCount']
        self.like_count = video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
