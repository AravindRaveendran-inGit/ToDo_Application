from django.urls import path
from .views import TaskDetail, TaskView, TaskCreate, TaskUpdate, TaskDelete, CustomLogin, RegisterPage
from django.contrib.auth.views import LogoutView


urlpatterns  = [

    path('login/', CustomLogin.as_view(), name='user-login'), 
    path('logout/', LogoutView.as_view(next_page='user-login'), name='user-logout'), 
    path('register/',RegisterPage.as_view(), name='register'),
    path('', TaskView.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    
] 