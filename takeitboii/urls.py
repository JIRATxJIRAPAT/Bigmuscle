"""takeitboii URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',include('about.urls')),
    path('',include('home.urls')),
    path('Users/',include('Users.urls')),
    path('News/',include('News.urls')),
    path('feature/',include('feature.urls')),
    path('tracking/',include('Tracking.urls')),
    path('trainer/',include('Trainer.urls')),
    path('Courses/',include('Courses.urls')),
    path('administrator/',include('administrator.urls')),
    path('social/',include('social.urls')),
    path('shop/',include('Shop.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)