from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from urimasapp.models import (Supervisor, School, User, Mission, Department, Role)

class StaffSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

        def save(self, commit=True):
            user = super().save(commit=False)
            user.is_member = True
            if commit:
                user.save()
                return user


#######################################supervisor signupForm #########################################################

class SupervisorSignUpForm(UserCreationForm):
    school = forms.ModelMultipleChoiceField(
        queryset=School.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_supervisor = True
        user.save()
        supervisor = Supervisor.objects.create(user=user)
        supervisor.school.add(*self.cleaned_data.get('school'))
        return user


#######################################authorizer signupForm ########################################################

class AuthorizerSignUpForm(UserCreationForm):
    school = forms.ModelMultipleChoiceField(
        queryset=School.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_authorizer = True
        user.save()
        supervisor = Supervisor.objects.create(user=user)
        supervisor.school.add(*self.cleaned_data.get('school'))
        return user


class SupervisorSchoolForm(forms.ModelForm):
    class Meta:
        model = Supervisor
        fields = ('school', )
        widgets = {
            'school': forms.CheckboxSelectMultiple
        }


class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission
        fields = (
                  'category',
                  'role',
                  'school',
                  'department',
                  'mission_purpose',
                  'mission_result',
                  'mission_destination',
                  'distance',
                  'departure_date',
                  'returning_date',
                  'mission_duration',
                  'transport',
                  'invitation')


#################################load schools based on category ###################################################

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['school'].queryset = School.objetcs.none()

            if 'category' in self.data:
                try:
                    category_id = int(self.data.get('category'))
                    self.fields['school'].queryset = School.objects.filter(category_id=category_id).order_by('name')

                except (ValueError, TypeError):
                    pass

            elif self.instance.pk:
                self.fields['school'].querset = self.instance.category.school_set.order_by('name')



#################################load department based on category ###################################################

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['department'].queryset = Department.objetcs.none()

            if 'category' in self.data:
                try:
                    category_id = int(self.data.get('category'))
                    self.fields['department'].queryset = Department.objects.filter(category_id=category_id).order_by('name')

                except (ValueError, TypeError):
                    pass

            elif self.instance.pk:
                self.fields['department'].querset = self.instance.category.department_set.order_by('name')



#################################load Roles based on category ###################################################
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['role'].queryset = Role.objetcs.none()

            if 'category' in self.data:
                try:
                    category_id = int(self.data.get('category'))
                    self.fields['role'].queryset = Role.objects.filter(category_id=category_id).order_by('name')

                except (ValueError, TypeError):
                    pass

            elif self.instance.pk:
                self.fields['role'].querset = self.instance.category.role_set.order_by('name')



