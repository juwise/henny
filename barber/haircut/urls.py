from django.conf.urls import url
from haircut import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'haircut'

urlpatterns = [
    url(r'^contact/',views.contact,name="contact"),
    url(r'^gallery/',views.gallery,name="gallery"),
    url(r'^about/',views.about,name="about"),


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
