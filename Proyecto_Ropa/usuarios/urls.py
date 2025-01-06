# usuarios/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import DesignCreateView, DesignListView, DesignDeleteView, TipoPrendaListView, RegisterUser, LoginUser


urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh token
    path('designs/', DesignListView.as_view(), name='design-list'),  # List designs
    path('designs/create/', DesignCreateView.as_view(), name='design-create'),  # Create design
    path('designs/<int:pk>/delete/', DesignDeleteView.as_view(), name='design-delete'),  # Delete design
    path('tipos-prenda/', TipoPrendaListView.as_view(), name='tipos-prenda'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
