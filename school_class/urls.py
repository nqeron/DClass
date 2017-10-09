from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'classes'

urlpatterns = [
    url(r'^$',views.ListSchoolClass.as_view(),name="all"),
    url(r'^conflict/$',views.Conflict.as_view(),name="conflict"),
    url(r'^student/(?P<username>[-\w]+)/class/(?P<pk>\d+)/$',views.SingleSchoolClass.as_view(),name="single"),
    url(r'^student/(?P<username>[-\w]+)/class/(?P<pk>\d+)/add/$',views.addClass,name="add"),
    url(r'^student/(?P<username>[-\w]+)/class/(?P<pk>\d+)/remove/$',views.removeClass,name="remove"),
    url(r'^student/(?P<username>[-\w]+)/$',views.StudentClasses.as_view(),name="for_student"),
]
