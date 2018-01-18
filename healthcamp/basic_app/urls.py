from django.conf.urls import url
from basic_app import views


app_name ='basic_app'

urlpatterns = [
    url(r'^$', views.index),
    url(r'^patient/', views.patient,name="patient"),
    url(r'^registration/', views.registration,name="registration"),
    url(r'^pharmacy/', views.pharmacy,name="pharmacy"),
    url(r'^villages/', views.villages,name="villages"),
    url(r'^villagespop/', views.villagespop,name="villagespop"),
    url(r'^person/', views.person,name="person"),
    url(r'^admin/', views.admin,name="admin"),
    url(r'^staff/', views.staff,name="staff"),
    url(r'^user_login/', views.user_login,name="user_login"),


]
