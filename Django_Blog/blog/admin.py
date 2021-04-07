from django.contrib import admin
from .models import Tag, Post

# Register your models here.

class TagAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

    """ def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = user.request.id
        obj.save() """


# Register your models here.
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
