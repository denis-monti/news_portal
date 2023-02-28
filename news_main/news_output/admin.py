from django.contrib import admin
from django.db.models import F
from .models import *


from .forms import *


class RubricAdmin(admin.ModelAdmin):
    search_fields = ('name',)



class SubRubricInline(admin.TabularInline):
    model = SubRubric

class SuperRubricAdmin(admin.ModelAdmin):
    exclude = ('super_rubric',)
    inlines = (SubRubricInline,)

class SubRubricAdmin(admin.ModelAdmin):
    form = SubRubricForm

class AdditionalImageInline(admin.TabularInline):
    model = AdditionalImage

class NewsAdmin(admin.ModelAdmin):
    list_display = ('rubric', 'title', 'description', 'author', 'image', 'published')
    list_display_links = ('title', 'description')
    fields = (('rubric', 'author'), 'title', 'description', 'image',)
    inlines = (AdditionalImageInline,)
    readonly_fields = ('published',)

    # def get_fieldsets(self, request, obj=None):
    #     fieldsets = (
    #         (None, {'fields': ('title', 'description', 'rubric'), 'classes': ('wide',),}),
    #         ('Дополнительные сведения', {'fields': ('file_path',),
    #          'description': 'Параметры, необязательные для указания.',}),
    #         ('Автоматически присваиваемое поля', {
    #          'fields': ('published',), }))
    #     return fieldsets
   # autocomplete_fields = ('rubric',)

# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('news', 'author', 'content', 'is_active', 'created_at')
#     list_display_links = ('news', 'author',)
#     fields = (('news', 'author',), 'content', 'is_active', 'created_at',)
#     readonly_fields = ('created_at',)

# class CommentUserInline(admin.TabularInline):
#     model = CommentUser
#     exclude = ('main_comment',)

class CommentPublicationAdmin(admin.ModelAdmin):
    exclude = ('target_comment', 'main_comment',)
    # inlines = (CommentUserInline,)

class CommentUserAdmin(admin.ModelAdmin):
    form = CommentUserForm

class LikeDislikeAdmin(admin.ModelAdmin):
    form = LikeDislikeForm

admin.site.register(Rubric,  RubricAdmin)
admin.site.register(SubRubric, SubRubricAdmin)
admin.site.register(SuperRubric, SuperRubricAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(CommentPublication, CommentPublicationAdmin)
admin.site.register(CommentUser, CommentUserAdmin)
admin.site.register(LikeDislike, LikeDislikeAdmin)


