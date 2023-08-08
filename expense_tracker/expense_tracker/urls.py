## urls.py
from django.urls import path
from .views import ExpenseViewSet

urlpatterns = [
    path('expenses/', ExpenseViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='expense-list'),
    path('expenses/<int:pk>/', ExpenseViewSet.as_view({
        'delete': 'destroy'
    }), name='expense-detail')
]
