from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from stories import views as story_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^stories/',include('stories.urls')),
    url(r'^about/$',views.about),
    url(r'^$',story_views.story_list,name="home"),
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
