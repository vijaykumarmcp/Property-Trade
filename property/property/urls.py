
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('',include('pages.urls')),
    path('listings/',include('listings.urls')),
    path('accounts/',include('accounts.urls')),
    path('contacts/',include('contacts.urls')),
    path('admin/', admin.site.urls),
    path('api/token',TokenObtainPairView.as_view()),
    path('api/token/refresh',TokenRefreshView.as_view())
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
