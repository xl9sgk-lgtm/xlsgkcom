import feedparser
from datetime import datetime
import re


README = "README.md"


START = "<!-- QUOTE-START -->"
END = "<!-- QUOTE-END -->"


# 隐私/网络安全新闻源

RSS_LIST = [

    "https://feeds.feedburner.com/TheHackersNews",

    "https://www.bleepingcomputer.com/feed/",

    "https://www.cisa.gov/news.xml"

]



def get_news():

    news=[]


    for rss in RSS_LIST:

        feed = feedparser.parse(rss)


        for item in feed.entries[:5]:

            news.append({

                "title": item.title,

                "link": item.link

            })


    return news[:3]




def update_readme(news):


    with open(
        README,
        "r",
        encoding="utf-8"
    ) as f:

        content=f.read()



    now=datetime.utcnow().strftime(
        "%Y-%m-%d %H:%M:%S UTC"
    )


    block=f"""

{START}

## 🔐 今日隐私与网络安全动态


更新时间：{now}


"""


    for item in news:

        block += f"""

- {item['title']}



"""


    block += END



    pattern = (
        START
        +
        ".*?"
        +
        END
    )


    new_content=re.sub(
        pattern,
        block,
        content,
        flags=re.S
    )


    with open(
        README,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(new_content)



if __name__=="__main__":


    news=get_news()


    if news:

        update_readme(news)

        print(
            "README 更新成功"
        )

    else:

        print(
            "没有获取新闻"
        )
