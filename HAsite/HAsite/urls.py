from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from account.views import login_user, register, logout_user, home

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('account/', include('account.urls')),
                  path('', home, name='home'),
                  path('register/', register, name='register'),
                  path('login/', login_user, name='login'),
                  path('logout/', logout_user, name='logout'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
