from django.urls import path
from . import views
from .views import PortfolioCreateView, register, login_view, home, portfolio_list, PortfolioEditView

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('portfolio/', portfolio_list, name='portfolio_list'),
    path('portfolio/add/', PortfolioCreateView.as_view(), name='portfolio_add'),
    path('portfolio/edit/<int:pk>/', PortfolioEditView.as_view(), name='portfolio_edit')
]
