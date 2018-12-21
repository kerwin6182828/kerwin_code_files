from django.conf.urls import url
from .views import *











# 小忠的视图

from django.conf.urls import url
from .views import *
urlpatterns =[
	url('^index/',personal_index_views),
	url('^articleEdit/',articleEdit_views),
	url('^about/',about_views),
	url('^board/',board_views),
	url('^mood/',mood_views),
] + [
	url('^upload_portrait/', upload_portrait_views),
	url('^load_articles/', load_articles_views),
	url('^load_about/',load_about_views),
	url('^load_mood/', load_mood_views),
	url('^load_board/', load_board_views),
	url('^userinfos/',userinfos_views),
]

