from django import forms


class PostForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=32, disabled=False, error_messages={'required': 'Please'})
    title = forms.CharField(label="Заголовок", min_length=2, max_length=64, error_messages={'required': 'Please'})
    body = forms.CharField(label="Пост", widget=forms.Textarea, error_messages={'required':'Ошибка, не введено сообщение'})


