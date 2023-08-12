import json
import os
from googleapiclient.discovery import build
from helper.youtube_api_manual import printj


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        channel = self.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()
        self.title = channel['items'][0]['snippet']['title']
        self.description = channel['items'][0]['snippet']['description']
        self.url = f"https://www.youtube.com/channel/{self.__channel_id}"
        self.subscriber_count = channel['items'][0]['statistics']['subscriberCount']
        self.video_count = channel['items'][0]['statistics']['videoCount']
        self.view_count = channel['items'][0]['statistics']['viewCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel_id = self.__channel_id
        channel = self.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()
        printj(channel)

    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('YT_API_KEY')
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self, file):
        self.file = file
        attrib_dict = {"channel_id": self.__channel_id,
                       "title": self.title,
                       "url": self.url,
                       "subscriber_count": self.subscriber_count,
                       "video_count": self.video_count,
                       "view_count": self.view_count,
                       }
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(attrib_dict, f, indent=2, ensure_ascii=False)