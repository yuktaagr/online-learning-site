from django.urls import path
from . import views

app_name = 'lms'
urlpatterns = [
    path('a/', views.course1, name='course1'),
    path('b/', views.course2, name='course2'),
    path('course3/', views.course3, name='course3'),
    path('course4/', views.course4, name='course4'),
    path('course5/', views.course5, name='course5'),
    path('course6/', views.course6, name='course6'),
    path('register/', views.register, name='register'),
path('register1/', views.register1, name='register1'),
    path('dash/', views.dashboard, name='dashboard'),
    path('use/', views.user_login, name='user_login'),
path('use1/', views.user_login1, name='user_login1'),
    path('logout/', views.user_logout, name='user_logout'),
    path('dash2/',views.dashboard2,name="dashboard2"),
path('dash3/',views.dashboard3,name="dashboard3"),
    path('profile/',views.profile,name='profile'),
path('profile2/',views.profile2,name='profile2'),
    path('option/',views.option,name='option'),
path('option2/',views.option2,name='option2'),
    path('coursesenrolled/',views.coursesenrolled,name= 'coursesenrolled'),
    path('achievement/',views.achievement,name='achievement'),
path('coursesenrolled1/',views.coursesenrolled1,name= 'coursesenrolled1'),
    path('achievement1/',views.achievement1,name='achievement1'),
path('v/',views.v,name='v'),
    path('courseregister/',views.courseregister,name='courseregister'),
    path('courseinfo/',views.courseinfo,name='courseinfo'),


]
