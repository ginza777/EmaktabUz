import datetime
import time

from celery import shared_task, Celery

from emaktab.log_chat import send_msg_log
from emaktab.models import UserData
from emaktab.req_sender import auto_post


app = Celery('task', broker='redis://localhost:6380/0')


@shared_task
def post_req():
    # time.sleep(10)
    users=UserData.objects.all()
    print("users..",users)
    for user in users:
        try:
            response=auto_post(user.login,user.password)
            if response:
                user.last_login=datetime.datetime.now()
                user.today_status=True
                send_msg_log(f"✅-{user.login}")
            else:
                send_msg_log(f"🛑-{user.login}")
        except Exception as e:
            send_msg_log(f"Error \n{e}")
