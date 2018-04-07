from django.urls import path
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'blogapp'
urlpatterns = [
    path('',views.article_list,name='list'),
    path('create/',views.article_create,name='create'),
    url(r'^(?P<slug>[\w-]+)/$',views.article_details, name="details"),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)