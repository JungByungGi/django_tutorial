from django.urls import path
from . import views

urlpatterns = [
    # 숫자형이 변수 명으로 받아서 url을 띄운다.
    path('detail/<int:pk>/', views.board_detail),
    path('list/', views.board_list),
    path('write/', views.board_write)
]
