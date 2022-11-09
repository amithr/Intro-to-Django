from django.urls import path

from . import views

app_name = 'guests'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('create/', views.create, name='create_guest'),
    # ex: /polls/5/results/
    path('list/', views.list, name='guest_list'),
    # ex: /polls/5/vote/
    path('<int:id>/', views.individual, name='individual_guest'),
    path('delete/<int:id>/', views.delete, name='delete_guest'),
]
