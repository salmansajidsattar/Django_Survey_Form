from django.contrib import admin
from django.urls import path
from Survey import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/admin/',admin.site.urls),
    path('',views.index),
    path('main/',views.index),
    path('main/PDF_FILE',views.PDF_FILE),
    path('PDF_FILE',views.PDF_FILE),
    path('main/Temp_data',views.Temp_data),
    path('Temp_data',views.Temp_data),
    path('return_pdf/',views.return_pdf),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)