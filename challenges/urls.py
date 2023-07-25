from django.urls import path
from challenges import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:month>', views.monthly_challenges_by_number,
         name="monthly-challenges-by-number"),
    path('<str:month>', views.monthly_challenges, name="monthly-challenges"),
]
