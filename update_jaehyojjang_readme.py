import feedparser as fd
import time
from datetime import datetime, timedelta

URL: str = "https://jaehyojjang.dev/feed.xml"
RSS_FEED: fd.FeedParserDict = fd.parse(URL)
MAX_POST: int = 5

CUSTOM_MARKDOWN: str = """
<p align="center">
    Visitor count<br>
    <img src="https://profile-counter.glitch.me/JaehyoJJAng/count.svg" />
</p>

[<img src="https://img.shields.io/badge/My BLOG-%23009639?style=for-the-badge&logo=Bloglovin&logoColor=white">][blog] [![mail](https://img.shields.io/badge/MAIL-Aff230?style=for-the-badge&logo=GMAIL&logoColor=%23000005)](mailto:yshrim12@naver.com) [<img src="https://img.shields.io/badge/jaehyo-7289da?style=for-the-badge&logo=DISCORD&logoColor=fff">][discord]

[blog]: https://jaehyojjang.github.io
[discord]: https://discord.gg/rm2y7rZmBS

## 💜 Stats

| [<img src="https://github-readme-stats.vercel.app/api?username=JaehyoJJAng&theme=onedark&hide_border=true&count_private=true" height="185" />](https://github.com/anuraghazra/github-readme-stats) |[<img src="https://streak-stats.demolab.com/?user=JaehyoJJAng&theme=dark" height="185" />](https://git.io/streak-stats)
| ------ | ------ |

## ✒️ Recent Blog Posts
"""

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    feed_date = datetime.fromtimestamp(time.mktime(feed['published_parsed'])) + timedelta(hours=9)
    CUSTOM_MARKDOWN+= f"[{feed_date.strftime('%Y.%m.%d')} - {feed['title']}]({feed['link']}) <br/>\n"

NOW_DATE = datetime.now().strftime('%Y/%m/%d_%H:%M')
CUSTOM_MARKDOWN+=f'\n\n<img src=\"https://img.shields.io/badge/최근%20배포일-{NOW_DATE}-%23121212?style=flat\">'

with open('README.md', mode='w', encoding='utf-8') as f: 
    f.write(CUSTOM_MARKDOWN)
