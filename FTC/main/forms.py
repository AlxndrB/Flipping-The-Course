from django import forms
from .models import UserProfile, Questions, Modules


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('firstname', 'lastname', 'questions',)


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = '__all__'

class ModuleForm(forms.ModelForm):
    class Meta:
        model = Modules
        fields = '__all__'
