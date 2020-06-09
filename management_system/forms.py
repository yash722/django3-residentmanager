from django.forms import ModelForm
from .models import Resident, visitor

class OutgoingForm(ModelForm):
    class Meta:
        model = Resident
        fields = ['name','mobile_no','flat','vehicle_no','reason']

class VisitorForm(ModelForm):
    class Meta:
        model = visitor
        fields = ['name','mobile_no','flat_vis','reason', 'family',]

class IsolatedForm(ModelForm):
    class Meta:
        model = Resident
        fields = ['name', 'flat','mobile_no','vehicle_no', 'corona_screening_positive',]
