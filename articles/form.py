from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
    
    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = Article.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error('title', f"\"{title}\" is already taken")
        return data










class ArticleFormOld(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea)

    def clean(self):
        cleaned_data = self.cleaned_data
        print('all data', cleaned_data)
        title = cleaned_data.get('title')
        content = cleaned_data.get("content")
        if title and title.lower().strip() == "the office":
            self.add_error('title', 'This title is taken.')
        if "office" in content or (title and "office" in title.lower()):
            self.add_error('content', "Office cannot be in content")
            raise forms.ValidationError("Office is not allowed")
        return cleaned_data
