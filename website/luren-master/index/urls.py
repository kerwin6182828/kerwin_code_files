from django.conf.urls import url
from .views import *
urlpatterns = [
    #访问路径是 /
    url(r'^$',index_views),
    url(r'^index/$',index_views),
    #访问路径是 /login
    # url(r'^login/$',login_views),
    # #访问路径是 /register
    # url(r'^register/$',register_views),
    # url(r'^check_uphone/$',check_uphone_views),
    # url(r'^check_login/$',check_login_views),
    # url(r'^logout/$',logout_views),
    # url(r'^show/$',show_views),
]

urlpatterns += [
    url(r'^article/(\d+)/$',article_views),
    url(r'^show/$',show_views),
    url(r'^content/$',content_views),
    url(r'^test/$',test_views),
    url(r'^comment_show/$',comment_show_views),
    url(r'^insert_reply/$',insert_reply_views),
    url(r'^log_out/(.*)/$',log_out_views),
    url(r'^like/$', like_views),
    url(r'^collect/$', collect_views),


    url(r'^article/a_id=(\d+)$', article_views),
]
# 我的视图


# 老王的视图
urlpatterns += [
    url(r'^login/$',login_views),
    url(r'^register/$',register_views),
    url(r'^check_uphone/$',check_uphone_views),
    url(r'^find_password/$',find_password_views),
]






