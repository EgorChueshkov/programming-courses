from .models import Student, Courses
from django.forms import ModelForm, TextInput, EmailInput, Select, ModelChoiceField



class StudentForm(ModelForm):
    class Meta:
        model = Student
        course = ModelChoiceField(queryset=Courses.objects.all(),
                                  widget=Select(attrs={'class': 'form-control'}))
        fields = ['first_name', 'last_name', 'email', 'course']
        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш email'
            }),


        }
