import tweepy
import datetime
import time
from background_task import background
from knowledgebase.models import Article
import os
BEARER_TOKEN = os.getenv('TWITTER_API')

# 驗證 Twitter API
client = tweepy.Client(bearer_token=BEARER_TOKEN)

@background(schedule=60*60)  # 每小時執行一次
def fetch_twitter_data():
    print("📢 開始執行 Twitter 爬蟲任務...")
    
    # 設定抓取範圍：過去一小時的推文
    one_hour_ago = datetime.datetime.utcnow() - datetime.timedelta(hours=1)
    
    # 搜尋關鍵字（例如 ADA）
    user1 = "IOHK_Charles"  # 更換為特定用戶
    user2 = "Cardano_CF"
    query = f"from:{user1} OR from:{user2} ADA crypto Cardano"
    
    max_retries = 5  # 最多重試 5 次
    retry_delay = 10  # 初始等待 10 秒

    for attempt in range(max_retries):
        try:
            # 取得推文
            tweets = client.search_recent_tweets(
                query=query,
                max_results=5,
                tweet_fields=["created_at"],
                expansions=["author_id"],  # 這樣才能取得 user 資訊
                user_fields=["username"]
            )

            new_articles = 0
            if tweets.data:
                user_dict = {user["id"]: user["username"] for user in tweets.includes.get("users", [])}

                for tweet in tweets.data:
                    if tweet.created_at and tweet.created_at >= one_hour_ago:
                        username = user_dict.get(str(tweet.author_id), f"User {tweet.author_id}")

                        # 建立文章標題與內容
                        title = f"{username} - {tweet.created_at.strftime('%Y-%m-%d %H:%M')}"
                        content = tweet.text
                        source = "Twitter ADA"

                        # 儲存到資料庫
                        Article.objects.create(
                            title=title,
                            content=content,
                            source=source,
                            published=True,
                            published_date=tweet.created_at
                        )
                        new_articles += 1

            print(f"🎉 爬取完成！新增文章 {new_articles} 篇。")
            return  # 成功執行，結束函數

        except tweepy.errors.TooManyRequests:
            print(f"⏳ API 過載，等待 {retry_delay} 秒後重試...")
            time.sleep(retry_delay)
            retry_delay *= 2  # 每次等待時間加倍

    print("❌ 達到最大重試次數，請稍後再試！")
