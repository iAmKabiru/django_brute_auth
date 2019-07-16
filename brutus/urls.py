from django.contrib import admin
from django.urls import path
from django.contrib.auth import views
from brute import views as bview
from .import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static

urlpatterns = [
	path('', bview.home, name="home_page"),
    path('admin/', admin.site.urls),
    path('accounts/login/', views.LoginView.as_view(), name='login_url'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout_url'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)