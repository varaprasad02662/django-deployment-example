from django.conf.urls import url
# from django.conf.urls import path
from basic_app import views


#Template tagging
app_name = 'basic_app'

urlpatterns = [
    url(r'^relative/',views.relative,name='relative'),
    url(r'^other/',views.other,name='other'),


]
