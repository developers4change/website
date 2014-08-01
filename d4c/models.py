from mongoengine import *
from django.conf import settings
from time import time
connect('fashion',host=settings.MONGO_HOST,port=settings.MONGO_PORT)
# Create your models here.

class FormRequest(Document):
    data                    =   DictField(required=True,db_field='data')
    created_at              =   IntField(required=False,db_field='ca',default=int(time()))
