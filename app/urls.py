from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.questions_listing, name='questions_listing'),
    path('tag/<str:tag>/', views.tag_questions, name='tag_questions'),
    path('question/<int:id>/', views.question, name='question'),
    path('ask/', views.new_question, name='ask'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('settings/', views.settings, name='settings'),
    path('admin/', admin.site.urls),
    path('<str:is_hot>/', views.hot_questions, name='hot_questions'),
]
