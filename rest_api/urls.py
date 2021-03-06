from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_api import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView,TokenVerifyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.homepage,name="homepage"), #working
    
    path("admins/advisor",views.Admin), #working
    path("user/register",views.users,name="users"),  #working
    path("user/login",views.login,name="login"), #working
    path("user/<int:user_id>/advisor",views.fetch_advisor),  #working
    path("user/<int:user_id>/advisor/<int:advisor_id>",views.book_call), # working
    path("user/<int:user_id>/advisor/booking",views.booking_fetch),  #working
          
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
