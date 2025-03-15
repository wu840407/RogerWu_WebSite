from apscheduler.schedulers.background import BackgroundScheduler
import atexit
from knowledgebase.tasks import fetch_twitter_data  # 請確保此函式已正確定義

def start_scheduler():
    scheduler = BackgroundScheduler(timezone="UTC")
    # 每1小時執行一次 fetch_twitter_data 任務
    scheduler.add_job(fetch_twitter_data, 'interval', hours=12)
    scheduler.start()
    # 註冊退出時關閉排程器
    atexit.register(lambda: scheduler.shutdown())