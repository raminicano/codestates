# 스케쥴러 선언
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler({'apscheduler.timezone':'UTC'})

# 스케쥴러에 사용될 job 선언하기

def hello():
    print("안녕하세요 전 5초마다 실행됨")

scheduler.add_job(func=hello,trigger='interval',seconds=5)

# 스케쥴러 시작하기
scheduler.start()