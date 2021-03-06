from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^questions$', views.getQuestionList),
  url(r'^questions/(?P<question_id>[0-9]+)$', views.getQuestionById),
  url(r'^answers$', views.postAnswer),
]