from django.conf.urls import url
from . import views as boards_views

urlpatterns = [
    url(r'^question/(?P<question_id>[0-9]+)/$', boards_views.question, name='view_question'),
    # url(r'^question/(?P<question_id>[0-9]/\
    #     comment/(?P<comment_id>[0-9]+)/(?P<status>up|down)/$', 'popularity',
    #     name='comment_popularity'),
    url(r'^question/comment/(?P<comment_id>[0-9]+)/(?P<status>up|down)/$', boards_views.popularity, name='comment_popularity'),
    url(r'^post/$', boards_views.post, name='post'),
    url(r'^upload/$', boards_views.upload, name='upload'),
]
