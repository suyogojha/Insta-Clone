"""Posts Admins"""
from django.contrib import admin

# Register your models here.
from posts.models import Post
from users.models import Profile


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post Admin"""
    # Lista de los atributos que mostrara en el admin
    list_display = ('__str__', 'title', 'photo', 'created', 'modified')
    # Campos de solo lectura
    readonly_fields = ('created', 'modified')
    # Lista de editables in situ
    list_editable = ('title', 'photo')
    # Campos de busqueda
    search_fields = (
        'profile__user__email',
        'profile__user__username',
        'profile__user__first_name',
        'profile__user__last_name',
        'title'
    )
    # Campos por los que se puede filtrar
    list_filter = (
        'profile__user__is_active',
        'profile__user__is_staff',
        'created',
        'modified',
    )
