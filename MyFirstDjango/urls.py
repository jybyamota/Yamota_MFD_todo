
from django.contrib import admin
from django.urls import path

from todo_list import views as todo_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo_views.home, name='home'),
    path('add/', todo_views.add, name='add'),
    path('strike/<int:item_id>/', todo_views.strike, name='strike'),
    path('unstrike/<int:item_id>/', todo_views.unstrike, name='unstrike'),
    path('delete/<int:item_id>/', todo_views.delete, name='delete'),
    path('about/', todo_views.about, name='about'),
]
