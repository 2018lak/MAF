"""MAF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from boards.forms import LoginForm
from boards import views as boards_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', boards_views.home, name='home'),
    url(r'^tag/(?P<tag>[\w.@+-]+)$', boards_views.home, name='tag_search'),
    url(r'^boards/', include('boards.urls', namespace='boards')),

    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^signup/$', boards_views.signup, name='signup'),

    # session
    url(r'^login/$', auth_views.login, {'authentication_form': LoginForm}, name='login_url'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login/'}, name='logout_url'),
    url(r'^signup_ok/$', TemplateView.as_view(template_name='registration/signup_ok.html'), name='signup_ok'),

    url(r'^summernote/', include('django_summernote.urls')),
]
