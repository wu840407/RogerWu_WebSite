import tweepy
import datetime
from background_task import background
from knowledgebase.models import Article

@background(schedule=60*60)  # 每小時執行一次
def fetch_twitter_data():
    print("開始執行 Twitter 爬蟲任務...")
    consumer_key = 'ZRwYdyAH0z5B7sIzh1eM3c3Kb'
    consumer_secret = 'UK0WREo3LkvMBZg619kkBdp3udz1AhjODutq0lUYBgAWtQFDq0'
    access_token = '1899791300645584896-ZUbVg17nGzOfInsv6vBVqx38e2StVe'
    access_token_secret = 'rhOh4nDRAKYgo7PuFqX1bWQwplirRtPV3vnUHkT3aweYU'
    
    # 驗證 Twitter API
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
    api = tweepy.API(auth)
    
    # 設定抓取範圍：過去一小時的推文
    one_hour_ago = datetime.datetime.now() - datetime.timedelta(hours=1)
    
    # 搜尋關鍵字（例如 ADA）
    user1 = "IOHK_Charles"  # 更換為特定用戶
    user2 = "Cardano_CF"
    query = f"from:user1 OR from:user2 ADA crypto Cardano"
    
    # 取得推文（注意：Twitter API v1.1 沒有直接的時間參數，所以你可以先抓取一定數量後，依據 tweet.created_at 過濾）
    tweets = tweepy.Cursor(api.search_tweets, q=query, lang="zh", tweet_mode="extended").items(100)
    
    new_articles = 0
    for tweet in tweets:
        # 只保留過去一小時的推文
        if tweet.created_at >= one_hour_ago:
            # 檢查是否已存在（可以根據 tweet.id 判斷，這裡簡單示例不做重複檢查）
            title = f"{tweet.user.screen_name} - {tweet.created_at.strftime('%Y-%m-%d %H:%M')}"
            content = tweet.full_text
            source = "Twitter ADA"
            
            # 建立一篇新文章
            Article.objects.create(
                title=title,
                content=content,
                source=source,
                published = True,
                published_date=tweet.created_at  # 或 auto_now_add
            )
            new_articles += 1
    
    print(f"爬取完成！新增文章 {new_articles} 篇。")
