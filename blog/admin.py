from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from blog.models import Category, Tag, Post

class PostAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',), }


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',), }


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',), }
    save_on_top = True
    save_as = True
    save_as_continue = True
    list_display = ('title', 'category', 'url', 'draft', 'created_at', 'created_up')
    list_filter = ('category', 'tag', 'created_at',)
    search_fields = ('title', 'category__title',)
    form = PostAdminForm
    """Для дублирование фильма"""
    list_editable = ('draft', 'category',)
    fields = (('title', 'url'), 'text', ('tag', 'category'), 'draft',)
    # readonly_fields = ('get_image',)
    # fieldsets = (
    #     (None, {
    #         'fields': (('title', 'url'),)
    #     }),
    #     (None, {
    #         'fields': ('text',)
    #     }),
    #     (None, {
    #         'fields': (('tag', 'category',), ('draft', 'created_up'),)
    #     }),
    #
    # )



    def unpublish(self, request, queryset):
        """ Снять с публикации """
        row_update = queryset.update(draft=True)
        if row_update == 1:
            massege_bit = '1 запесь обновлена'
        else:
            massege_bit = f"{row_update} записей были обновлены"
            self.message_user(request, f'{massege_bit}')

    def publish(self, request, queryset):
        """ Опубликовать """
        row_update = queryset.update(draft=False)
        if row_update == 1:
            massege_bit = '1 запесь обновлена'
        else:
            massege_bit = f"{row_update} записей были обновлены"
            self.message_user(request, f'{massege_bit}')

    publish.short_description = 'Опубликовать'
    publish.allowed_permission = ('change',)
    unpublish.short_description = 'Снять с публикации'
    unpublish.allowed_permission = ('change',)
    # get_image.short_description = "Постер"
