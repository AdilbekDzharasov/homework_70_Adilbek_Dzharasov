from django import forms
from django.forms import widgets
from webapp.models import Type, Status, Task
from webapp.models.projects import Project
from webapp.widgets import DatePickerInput


class TaskForm(forms.ModelForm):
    status = forms.ModelChoiceField(required=True, label='Status', queryset=Status.objects.all(), initial=[0])
    project = forms.ModelChoiceField(required=True, label='Project', queryset=Project.objects.all(), initial=[0])

    class Meta:
        model = Task
        fields = ('summary', 'description', 'status', 'type', 'project')
        widgets = {
            'type': widgets.CheckboxSelectMultiple
        }


class ProjectForm(forms.ModelForm):
    beginning_date = forms.DateField(required=True, label='Beginning date', widget=DatePickerInput)
    expiration_date = forms.DateField(required=False, label='Expiration date', widget=DatePickerInput)

    class Meta:
        model = Project
        fields = ('title', 'description', 'beginning_date', 'expiration_date', 'user')


class ProjectTaskForm(forms.ModelForm):
    status = forms.ModelChoiceField(required=True, label='Status', queryset=Status.objects.all(), initial=[0])

    class Meta:
        model = Task
        fields = ('summary', 'description', 'status', 'type')
        widgets = {
            'type': widgets.CheckboxSelectMultiple
        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Search")


class ProjectAddUserForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['user']
        widgets = {
            'user': forms.CheckboxSelectMultiple
        }

