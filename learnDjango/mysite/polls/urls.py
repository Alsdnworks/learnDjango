from django.urls import path,include,re_path
from . import views

urlpatterns = [
    #path를 수정할때 하드코딩을 제거
    path(r'', views.index, name='index'),
    re_path(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    re_path(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    re_path(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]