from django.urls import path


from .views import AttedanceRecordList, AttedanceRecordDetail


urlpatterns = [
    path('', AttedanceRecordList.as_view()),
    path('<int:pk>/', AttedanceRecordDetail.as_view()),
]