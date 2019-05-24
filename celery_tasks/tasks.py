from django.core.mail import EmailMessage
from celery import Celery
import os,platform

if platform.system()!='Windows':
	import django
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ebookstore.settings')
	django.setup()

app = Celery('celery_tasks.tasks', broker='redis://192.168.126.129:6379/2')

@app.task
def celery_send_code(title,content_html,email_from,reciever):
	msg=EmailMessage(title,content_html,email_from,reciever)
	msg.content_subtype='html'
	msg.send()