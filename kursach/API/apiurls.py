from django.urls import path
from .apiview import *

urlpatterns = [
    path('v1/TypeOfTransactionApiList', TypeOfTransactionApiList.as_view(), name='TransactionsAPIView'),
    path('v1/NewsApiList', NewsApiList.as_view(), name='NewsAPIView'),
    path('v1/BillApiGetUpdate/<int:pk>/', BillApiGetUpdate.as_view(), name='BillApiGetUpdate'),
    path('v1/BillApiCreate/', BillApiCreate.as_view(), name='BillApiCreate'),
    path('v1/CategoriesApiList', CategoriesApiList.as_view(), name='CategoriesApiList'),
    path('v1/CategoriesApiDelete/<int:pk>/', CategoriesApiDelete.as_view(), name='CategoriesApiDelete'),
    path('v1/TransactionsApiDelete/<int:pk>/', TransactionsApiDelete.as_view(), name='TransactionsApiDelete'),
    path('v1/TransactionsApiList', TransactionsApiList.as_view(), name='TransactionsAPIView'),
    path('v1/transactions_list/<int:pk>/', TransactionsAPIView.as_view()),
    path('v1/CheckApiList', CheckApiList.as_view(), name='CheckApiList'),
    path('v1/CheckApiList/<int:pk>/', CheckApiList.as_view()),
    ]