from django import forms
from django.forms import ModelForm
from creatures_ranking.models import Creature


class CreatureForm(ModelForm):
    class Meta:
        model = Creature
        fields = '__all__'


class RegisterForm(forms.Form):
    Username = forms.CharField(max_length=255)
    Password = forms.CharField(widget=forms.PasswordInput)
    Repeat_password = forms.CharField(widget=forms.PasswordInput)
    Email = forms.EmailField()

    def clean(self):
        form_data = self.cleaned_data
        if form_data['Password'] != form_data['Repeat_password']:
            self._errors["Password"] = ["Password do not match"]  # Will raise a error message
            del form_data['Password']
        return form_data


class LoginForm(forms.Form):
    Username = forms.CharField(max_length=255)
    Password = forms.CharField(widget=forms.PasswordInput)


ORDER_LIST = (
    ("fight_value", "Fight_value"),
    ("name", "Alphabetical"),
    ("castle_name", "Castle name"),
    ("lvl", "Level"),
    ("attack", "Attak"),
    ("defence", "Defence"),
    ("min_dmg", "Minimal Dmg"),
    ("max_dmg", "Maximal Dmg"),
    ("health", "Health"),
    ("speed", "Speed"),
    ("growth", "Growth"),
    ("AI_value", "AI value"),
)


class OrderForm(forms.Form):
    order = forms.ChoiceField(choices=ORDER_LIST)
