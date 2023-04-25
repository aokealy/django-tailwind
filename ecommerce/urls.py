from django.conf import settings
from django.conf.urls.static import static 
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView





urlpatterns = [

    path('', include('core.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    path('admin/', admin.site.urls),
    path('robots.txt', TemplateView.as_view(template_name='core/robots.txt', content_type='text/plain')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
