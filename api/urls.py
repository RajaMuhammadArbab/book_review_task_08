from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, ReviewViewSet, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
    
    
    path('books/<int:book_id>/reviews/', ReviewViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    
    
    path('reviews/<int:pk>/', ReviewViewSet.as_view({
        'get': 'retrieve',  
        'put': 'update',
        'delete': 'destroy'
    })),

    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
