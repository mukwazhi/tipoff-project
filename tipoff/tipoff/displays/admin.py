from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from .models import Information, Brand, Article
from django import forms


# --------------------------Information--Admin-------------------#
class InformationForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Information
        fields = '__all__'


class InformationAdmin(admin.ModelAdmin):
    form = InformationForm


admin.site.register(Information, InformationAdmin)

# --------------------Brand--Admin-------------------------#
admin.site.register(Brand)


# ----------------------Article--Admin---------------------#
class ArticleForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Article
        fields = '__all__'


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = ArticleForm

admin.site.register(Article, ArticleAdmin)
