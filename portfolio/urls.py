from django.urls import path
from portfolio.views import(PortfolioCreateView,
                            RegisterView,
                            PortfolioListView,
                            PortfolioEditView,
                            PortfolioDeleteView,
                            HomeView,
                            LoginView,
                            EditView,
                            LogoutView,
                            AssetSearchView,
                            PortfolioView,
                            TransactionEditView,
                            TransactionDeleteView)
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('edit/', EditView.as_view(), name='edit'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('portfolio/<int:pk>/search/', AssetSearchView.as_view(), name='asset_search'),
    path('portfolios/', PortfolioListView.as_view(), name='portfolio_list'),
    path('portfolio/<int:pk>/', PortfolioView.as_view(), name='portfolio'),
    path('portfolios/add/', PortfolioCreateView.as_view(), name='portfolio_add'),
    path('portfolios/edit/<int:pk>/', PortfolioEditView.as_view(), name='portfolio_edit'),
    path('portfolios/delete/<int:pk>/', PortfolioDeleteView.as_view(), name='portfolio_delete'),
    path('portfolio/<int:pk_portfolio>/edit/<int:pk_transaction>/',TransactionEditView.as_view(), name='transaction_edit'),
    path('portfolio/<int:pk_portfolio>/delete/<int:pk_transaction>/', TransactionDeleteView.as_view(), name='transaction_delete')

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)