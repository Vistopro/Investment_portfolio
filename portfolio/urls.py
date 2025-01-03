from django.urls import path
from portfolio.views import (
    PortfolioCreateView,
    RegisterView,
    PortfolioListView,
    PortfolioEditView,
    PortfolioDeleteView,
    TransactionCreateView,
    TransactionDeleteView,
    TransactionEditView,
    TransactionListView,
    SearchFinancialInstrumentView,
    HomeView,
    LoginView,
    LogoutView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('portfolio/', PortfolioListView.as_view(), name='portfolio_list'),
    path('portfolio/add/', PortfolioCreateView.as_view(), name='portfolio_add'),
    path('portfolio/edit/<int:pk>/', PortfolioEditView.as_view(), name='portfolio_edit'),
    path('portfolio/delete/<int:pk>/', PortfolioDeleteView.as_view(), name='portfolio_delete'),
    path('transaction/', TransactionListView.as_view(), name='transaction_list'),
    path('transaction/add/', TransactionCreateView.as_view(), name='transaction_add'),
    path('transaction/edit/<int:pk>/', TransactionEditView.as_view(), name='transaction_edit'),
    path('transaction/delete/<int:pk>/', TransactionDeleteView.as_view(), name='transaction_delete'),
    path('search/', SearchFinancialInstrumentView.as_view(), name='search'),
]
