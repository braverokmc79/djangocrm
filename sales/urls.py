from django.urls import path
from .views import 세일목록, 세일상세, 세일_입력


app_name="홈페이지"

urlpatterns = [
    path("", 세일목록),
    
    #http://127.0.0.1:8000/홈페이지/2/
    path("<int:pk>/", 세일상세),

    path("make/", 세일_입력),
]
