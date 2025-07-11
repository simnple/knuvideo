# knuvideo
국립공주대학교 LMS에서 제공하는 강의 영상을 쉽게 다운로드할 수 있도록 도와주는 파이썬 비공식 라이브러리입니다.

> [!WARNING]
> 이 프로젝트는 교육용 목적으로 개발되었습니다.</br>
> 프로젝트 사용에 대한 모든 책임은 사용자 본인에게 있으며, 사용 중 발생하는 모든 문제에 대해서는 책임지지 않습니다. 

## 예시 코드
```python
>>> from knuvideo import Lms
>>> lms = Lms("6864dd934****")
>>> lms.info
{
  'title': '5-1. ******',
  'type': 'video1',
  'duration': 3044.33,
  'author': '정**',
  'date': 1751440787,
  'size': 87185822
}
>>> lms.download("video.mp4")
```

그 외 예시 코드는 `example.py` 에서 확인하실 수 있습니다.
