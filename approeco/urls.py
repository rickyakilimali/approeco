"""approeco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from .views import HomePageView, login_success, LoginView, LogOutView
from django.conf.urls.static import static
from django.conf import settings
from pub.views import imageviewer,imageviewer2,imageviewer3,imageviewer1
from sendemail.views import emailView,successView


urlpatterns = [
    url(r'^admin/', include('smuggler.urls')),
    url(r'^admin/', admin.site.urls),
    url('^$', HomePageView.as_view(), name='home'),
    url(r'^login_success/$', login_success, name='login_success'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogOutView.as_view(), name='logout'),



    url(r'^category/', include('category.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^product/', include('product.urls')),
    url(r'^quotation/', include('quotation.urls')),

    url(r'^image/$', imageviewer, name='image.html'),
	url(r'^page1/$', imageviewer1, name='image.html'),
	url(r'^page2/$', imageviewer2, name='image.html'),
	url(r'^page3/$', imageviewer3, name='image.html'),
	url(r'^email/$', emailView, name='email.html'),
	url(r'^email/succes/$', successView, name='success'),
	url(r'^consultation/',include('consultation.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
