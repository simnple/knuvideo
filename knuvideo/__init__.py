from datetime import datetime
from bs4 import BeautifulSoup
import requests
import pytz

class Lms():
    def __init__(self, content_id: str):
        self.content_id = content_id
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
            "Referer": "https://kools.kongju.ac.kr/"
        }
        self.__data = self.__get_data()
        self.size = self.__get_size()

    def __get_data(self):
        response = requests.get(f"https://kools.kongju.ac.kr/viewer/ssplayer/uniplayer_support/content.php?content_id={self.content_id}", headers=self.headers)

        if response.status_code == 200:
            return BeautifulSoup(response.text, "xml")

        else:
            raise ValueError("Failed to get date: invalid content id or internet connection error")

    def __get_size(self):
        response = requests.head(self.media_uri, headers=self.headers)

        if response.status_code != 200:
            raise ValueError("Failed to get size: invalid content id or internet connection error")

        return int(response.headers["Content-Length"])

    @property
    def info(self):
        return {
            "title": self.title,
            "type": self.story_type,
            "duration": self.story_duration,
            "author": self.author,
            "date": self.date,
            "size": self.size
        }

    @property
    def media_uri(self):
        return self.__data.find("media_uri").get_text().replace("[MEDIA_FILE]", self.main_media)

    @property
    def main_media(self):
        return self.__data.find("main_media").get_text()

    @property
    def title(self):
        return self.__data.find("title").get_text()
    
    @property
    def story_type(self):
        return self.__data.find("story_type").get_text()

    @property
    def story_duration(self):
        return float(self.__data.find("story_duration").get_text())

    @property
    def author(self):
        return self.__data.find("name").get_text()

    @property
    def date(self):
        kst = pytz.timezone("Asia/Seoul")
        dt = datetime.strptime(self.__data.find("date").get_text(), "%Y-%m-%d %H:%M:%S")
        dt_kst = kst.localize(dt)
        return int(dt_kst.timestamp())

    def download(self, path):
        response = requests.head(self.media_uri, headers=self.headers)

        if response.status_code != 200:
            raise ValueError("Failed to download: invalid content id or internet connection error")

        headers = self.headers.copy()
        headers["Range"] = "bytes=0-"

        response = requests.get(self.media_uri, headers=headers)

        if response.status_code != 206:
            raise ValueError("Failed to download: invalid content id or internet connection error")

        open(path, "wb").write(response.content)
