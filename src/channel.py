import os
import requests
import json
from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""




    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала.
        Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.api_key = "AIzaSyBaOVsm5nVNANKOv0JL_joAFxW0a6Zm9QE"
        self.fetch_channel_info()


    def fetch_channel_info(self) -> None:
        """Загружает информацию о канале через API и заполняет атрибуты."""
        url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={self.channel_id}&key={self.api_key}"
        response = requests.get(url)
        data = response.json()

        if "items" in data and len(data["items"]) > 0:
            snippet = data["items"][0]["snippet"]
            statistics = data["items"][0]["statistics"]

            self.title = snippet["title"]
            self.description = snippet["description"]
            self.url = f"https://www.youtube.com/channel/{self.channel_id}"
            self.subscriber_count = int(statistics["subscriberCount"])
            self.video_count = int(statistics["videoCount"])
            self.view_count = int(statistics["viewCount"])


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print("Информация о канале:")
        print(f"Название: {self.title}")
        print(f"Описание: {self.description}")
        print(f"Ссылка на канал: {self.url}")
        print(f"Количество подписчиков: {self.subscriber_count}")
        print(f"Количество видео: {self.video_count}")
        print(f"Общее количество просмотров: {self.view_count}")

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API."""
        api_key: str = os.getenv('YOUTUBE_API_KEY')
        return build('youtube', 'v3', developerKey=api_key)



    def to_json(self, filename: str) -> None:
        """Сохраняет информацию о канале в JSON файл."""
        channel_info = {
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "subscriber_count": self.subscriber_count,
            "video_count": self.video_count,
            "view_count": self.view_count
        }

        with open(filename, "w") as file:
            json.dump(channel_info, file, ensure_ascii=False, indent=2)

    def __str__(self):
        """
        Метод для вывода информации
        о канале в виде строки
        """
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        """
        Метод для сложения
        двух каналов по количеству подписчиков
        """
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        """
        Метод для вычитания количества
        подписчиков другого канала из текущего
        """
        return self.subscriber_count - other.subscriber_count

    def __lt__(self, other):
        """
        Метод для сравнения двух каналов
        (меньше) по количеству подписчиков
        """
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other):
        """
        Метод для сравнения двух каналов
        (меньше или равно) по количеству подписчиков
        """
        return self.subscriber_count <= other.subscriber_count

    def __eq__(self, other):
        """
        Метод для сравнения двух каналов
        (равно) по количеству подписчиков
        """
        return self.subscriber_count == other.subscriber_count

    def __ne__(self, other):
        """
        Метод для сравнения двух каналов
        (не равно) по количеству подписчиков
        """
        return self.subscriber_count != other.subscriber_count

    def __gt__(self, other):
        """
        Метод для сравнения двух каналов
        (больше) по количеству подписчиков
        """
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other):
        """Метод для сравнения двух каналов
        (больше или равно) по количеству подписчиков
        """
        return self.subscriber_count >= other.subscriber_count



# import json
# import os
# from googleapiclient.discovery import build
# from helper.youtube_api_manual import printj
#
#
# class Channel:
#     """Класс для ютуб-канала"""
#
#     def __init__(self, channel_id: str) -> None:
#         """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
#         self.__channel_id = channel_id
#         channel = self.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()
#         self.title = channel['items'][0]['snippet']['title']
#         self.description = channel['items'][0]['snippet']['description']
#         self.url = f"https://www.youtube.com/channel/{self.__channel_id}"
#         self.subscriber_count = channel['items'][0]['statistics']['subscriberCount']
#         self.video_count = channel['items'][0]['statistics']['videoCount']
#         self.view_count = channel['items'][0]['statistics']['viewCount']
#
#     def __str__(self):
#         return f'{self.title} ({self.url})'
#
#     def __add__(self, other):
#         return self.subscriber_count + other.subscriber_count
#
#     def __sub__(self, other):
#         return int(self.subscriber_count) - int(other.subscriber_count)
#
#     def __lt__(self, other):
#         return self.subscriber_count < other.subscriber_count
#
#     def __le__(self, other):
#         return self.subscriber_count <= other.subscriber_count
#
#     def __gt__(self, other):
#         return self.subscriber_count > other.subscriber_count
#
#     def __ge__(self, other):
#         return self.subscriber_count >= other.subscriber_count
#
#     def print_info(self) -> None:
#         """Выводит в консоль информацию о канале."""
#         channel_id = self.__channel_id
#         channel = self.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()
#         printj(channel)
#
#     @classmethod
#     def get_service(cls):
#         api_key: str = os.getenv('YT_API_KEY')
#         return build('youtube', 'v3', developerKey=api_key)
#
#     def to_json(self, file):
#         self.file = file
#         attrib_dict = {"channel_id": self.__channel_id,
#                        "title": self.title,
#                        "url": self.url,
#                        "subscriber_count": self.subscriber_count,
#                        "video_count": self.video_count,
#                        "view_count": self.view_count,
#                        }
#         with open(self.file, "w", encoding="utf-8") as f:
#             json.dump(attrib_dict, f, indent=2, ensure_ascii=False)