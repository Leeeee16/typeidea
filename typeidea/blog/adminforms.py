from dal import autocomplete
from django import forms
# from ckeditor.widgets import CKEditorWidget
# from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Category, Tag, Post


class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=autocomplete.ModelSelect2(url='category-autocomplete'),
        label='分类',
    )
    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='tag-autocomplete'),
        label='标签',
    )

    # content = forms.CharField(widget=CKEditorUploadingWidget(), label='正文', required=False)

    class Meta:
        model = Post
        fields = ('category', 'tag', 'title', 'desc',
                  'content', 'status')
