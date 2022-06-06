from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="expenses"),
    path('authentication/', include('authentication.urls')),
    path('add-expense/', views.add_expense, name='add-expense')
]
