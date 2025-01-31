from django.urls import path
from .views import 세일목록, 세일상세


app_name="홈페이지"

urlpatterns = [
    path("", 세일목록),
    
    #http://127.0.0.1:8000/홈페이지/2/
    path("<pk>/", 세일상세)
]
