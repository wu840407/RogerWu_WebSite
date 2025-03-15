import tweepy
import datetime
import time
from background_task import background
from knowledgebase.models import Article
import os

BEARER_TOKEN = os.getenv('TWITTER_API')

client = tweepy.Client(bearer_token=BEARER_TOKEN)

def fetch_twitter_data():
    print("📢 開始執行 Twitter 爬蟲任務...")

    # 過去24小時的推文
    one_day_ago = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=12)

    user1 = "IOHK_Charles"
    user2 = "Cardano_CF"
    query = f"from:{user1} OR from:{user2} ADA Cardano"

    max_retries = 5
    retry_delay = 10

    for attempt in range(max_retries):
        try:
            tweets = client.search_recent_tweets(
                query=query,
                max_results=10,  # 10~100
                tweet_fields=["created_at"],
                expansions=["author_id"],
                user_fields=["username"]
            )

            new_articles = 0

            # 如果 tweets.data 不為空
            if tweets.data:
                # 建立 author_id -> username 的字典
                user_dict = {}
                if tweets.includes and "users" in tweets.includes:
                    user_dict = {
                        user["id"]: user["username"] for user in tweets.includes["users"]
                    }

                for tweet in tweets.data:
                    # 確保 tweet 有 created_at，且在過去24小時內
                    if tweet.created_at and tweet.created_at >= one_day_ago:
                        # 找出使用者名稱
                        username = user_dict.get(str(tweet.author_id), f"User {tweet.author_id}")

                        # 拆分推文，把「第一行」作為標題，其餘行數組成內容
                        lines = tweet.text.splitlines()
                        if lines:
                            first_line = lines[0]
                            rest_content = "\n".join(lines[1:]) if len(lines) > 1 else ""
                        else:
                            first_line = tweet.text
                            rest_content = ""

                        # 將第一行當作標題，發文者名字當作「副標」放在 source
                        # 全文存入 content
                        Article.objects.create(
                            title=first_line,            # 第一行作為標題
                            content=tweet.text,          # 整篇推文當作內容
                            source=username,             # 發文者名字當作副標
                            published=True,
                            published_date=tweet.created_at  # 直接存 datetime 物件
                        )
                        new_articles += 1

            print(f"🎉 爬取完成！新增文章 {new_articles} 篇。")
            return

        except tweepy.errors.TooManyRequests:
            print(f"⏳ API 過載，等待 {retry_delay} 秒後重試...")
            time.sleep(retry_delay)
            retry_delay *= 2

    print("❌ 達到最大重試次數，請稍後再試！")
