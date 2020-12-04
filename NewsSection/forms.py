from django import forms
from NewsSection.models import News, Comment


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        exclude = ['author', 'date_posted']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['date_posted', 'news', 'name']





