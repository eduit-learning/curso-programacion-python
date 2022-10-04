from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('greetings', views.greetings, name='greetings'),
    path('execute-post', views.execute_post, name='execute_post'),
    path('execute-put', views.execute_put, name='execute_put'),
    path('execute-delete', views.execute_delete, name='execute_delete'),
    path('greetings-message/<message>/', views.greetings_message, name='greetings_message'),
    path('greetings-age/<int:age>/', views.greetings_age, name='greetings_age'),
    path('greetings-query', views.greetings_query_string, name='greetings_query_string'),
    path('index-html', views.index_html, name='index_html')
]