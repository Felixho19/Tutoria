from django.db import models
from django.forms import ModelForm
from tutoria.models import Tutor, TutoriaUser

class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor