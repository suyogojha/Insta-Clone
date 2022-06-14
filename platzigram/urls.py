# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

# Views
from users import views as users_views

# Para poder visualizar las imgs durante desarrollo se agrega el mas y la linea
# Ademas se deben cambiar la mediaurl y media root en settings
urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    # Users
    path('users/', include(('users.urls', 'users'), namespace='users')),    
    # Posts
    path('', include(('posts.urls', 'posts'), namespace='posts')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
