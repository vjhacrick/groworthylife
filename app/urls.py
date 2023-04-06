from django.urls import path
from . import views
from .views import *

urlpatterns = [
	path('', views.welcomePage, name="welcome"),
	path('home/', views.homePage, name="home"),
	path('game/', views.gamePage, name="game"),
	path('mad-block/', views.madBlockPage, name="mad-block"),
	path('academics/', views.academicsPage, name="academics"),
	path('subjects/<class_id>/', views.subjectPage, name="subjects"),
	path('chapters/<subject_id>/', views.chapterPage, name="chapters"),
]