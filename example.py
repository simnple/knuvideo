from datetime import datetime
from knuvideo import Lms
import pytz

lms = Lms("content-id")

print("video info")
print("title:", lms.title)
print("story_type:", lms.story_type)
print("story_duration:", format(lms.story_duration, ",") + "s")
print("author:", lms.author)
print("date:", datetime.fromtimestamp(lms.date, tz=pytz.timezone("Asia/Seoul")).strftime("%Y-%m-%d %H:%M:%S"))
print("size:", format(lms.size, ",d"), "bytes")

print("downloading video...")
lms.download("video.mp4")
print("done.")