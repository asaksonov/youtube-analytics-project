import os
from datetime import timedelta

import isodate
from googleapiclient.discovery import build


class PlayList:
    api_key = "AIzaSyBaOVsm5nVNANKOv0JL_joAFxW0a6Zm9QE"
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, pl_id):
        self.pl_id = pl_id
        self.url = f'https://www.youtube.com/playlist?list={self.pl_id}'
        playlist_videos = self.youtube.playlists().list(part='snippet', id=self.pl_id).execute()
        self.title = playlist_videos['items'][0]['snippet']['title']



    @property
    def total_duration(self):
        """
        Функция получения данных о видеоролике, суммирование продолжительности роликов
        """
        playlist_videos = self.youtube.playlistItems().list(playlistId=self.pl_id, part='contentDetails',
                                                            maxResults=50).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]

        video_response = self.youtube.videos().list(part='contentDetails, statistics', id=','.join(video_ids)).execute()

        all_time = timedelta(seconds=0)
        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            all_time += duration
        print(all_time)
        return all_time



    def show_best_video(self):
        """
        Функция вывода самого популярного видео (по количеству лайков) и вывод ссылки
        """
        playlist_videos = self.youtube.playlistItems().list(playlistId=self.pl_id, part='contentDetails',
                                                            maxResults=50).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]

        video_response = self.youtube.videos().list(part='contentDetails, statistics', id=','.join(video_ids)).execute()

        best_likes = 0
        best_video_url = ''

        for video in video_response['items']:
            video_id = video['id']
            likes_video = int(video['statistics']['likeCount'])
            if likes_video > best_likes:
                best_likes = likes_video
                best_video_url = video_id
        print(f'https://youtu.be/{best_video_url}')
        return f'https://youtu.be/{best_video_url}'



pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
pl.total_duration

pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
pl.show_best_video()