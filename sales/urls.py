from django.urls import path
from .views import 세일목록, 세일상세, 세일_입력 , 세일_업데이트, 세일_지우기 , 세일_입력View ,세일_목록View ,세일_상세View, 세일_업데이트View, 세일_지우기View

app_name="홈페이지"

urlpatterns = [ 
    #path("", 세일목록 , name="목록"),
    path("", 세일_목록View.as_view() , name="목록"),

    #http://127.0.0.1:8000/홈페이지/2/
    #path("<int:pk>/", 세일상세 , name="상세"),
    path("<int:pk>/", 세일_상세View.as_view() , name="상세"),

    #path("<int:pk>/업데이트/", 세일_업데이트, name="업뎃"),
    path("<int:pk>/업데이트/", 세일_업데이트View.as_view(), name="업뎃"),


    #path("<int:pk>/지우기/", 세일_지우기, name="지우기"),
     path("<int:pk>/지우기/", 세일_지우기View.as_view(), name="지우기"),
  
  
    #path("make/", 세일_입력, name="생성"),
    path("ma_monde/", 세일_입력View.as_view(), name="생성"),

]
