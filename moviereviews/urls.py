from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from movie import views as movieViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', movieViews.home, name='home'),
    path('about/', movieViews.about, name='about'),
    path('statistics/', movieViews.statistics, name='statistics'),  # 👈 AÑADIDO
    path('statistics/genre/', movieViews.statistics_genre, name='statistics_genre'),
    path('statistics/combined/', movieViews.statistics_combined, name='statistics_combined'),
    path('news/', include('news.urls')),
]

# Configuración para servir archivos multimedia en desarrollo
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



 



