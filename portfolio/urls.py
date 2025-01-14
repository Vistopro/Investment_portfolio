from django.urls import path
from portfolio.views import (
    PortfolioCreateView,
    RegisterView,
    PortfolioListView,
    PortfolioEditView,
    PortfolioDeleteView,
    HomeView,
    LoginView,
    EditView,
    LogoutView
)
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('edit/', EditView.as_view(), name='edit'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('portfolio/', PortfolioListView.as_view(), name='portfolio_list'),
    path('portfolio/add/', PortfolioCreateView.as_view(), name='portfolio_add'),
    path('portfolio/edit/<int:pk>/', PortfolioEditView.as_view(), name='portfolio_edit'),
    path('portfolio/delete/<int:pk>/', PortfolioDeleteView.as_view(), name='portfolio_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)