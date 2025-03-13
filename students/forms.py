from django import forms
from .models import PersonalDetails, County, SubCounty



class PersonalDetailsForm(forms.ModelForm):
    county = forms.ModelChoiceField(queryset=County.objects.all(), empty_label="Select County")
    sub_county = forms.ModelChoiceField(queryset=SubCounty.objects.none(), empty_label="Select Sub-County")

    class Meta:
        model = PersonalDetails
        fields = '__all__'

        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Enter your full name"}),
            "reg_no": forms.TextInput(attrs={"placeholder": "Enter your registration number"}),
            "school": forms.TextInput(attrs={"placeholder": "Enter your school name"}),
            "gender": forms.Select(attrs={"placeholder": "Select your gender"}),
            "home_address": forms.TextInput(attrs={"placeholder": "Enter your home address"}),
            "phone_number": forms.TextInput(attrs={"placeholder": "Enter your phone number"}),
            "next_of_kin": forms.TextInput(attrs={"placeholder": "Enter next of kin's name"}),
            "next_of_kin_address": forms.TextInput(attrs={"placeholder": "Enter next of kin's address"}),
            "next_of_kin_phone": forms.TextInput(attrs={"placeholder": "Enter next of kin's phone"}),
            "chief_name": forms.TextInput(attrs={"placeholder": "Enter chief's name"}),
            "chief_address": forms.TextInput(attrs={"placeholder": "Enter chief's address"}),
            "chief_phone": forms.TextInput(attrs={"placeholder": "Enter chief's phone"}),
            "disability_details": forms.TextInput(attrs={"placeholder": "If yes, specify your disability"}),
    }
    def __init__(self, *args, **kwargs):
        super(PersonalDetailsForm, self).__init__(*args, **kwargs)
        if 'county' in self.data:
            try:
                county_id = int(self.data.get('county'))
                self.fields['sub_county'].queryset = SubCounty.objects.filter(county_id=county_id)
            except (ValueError, TypeError):
                self.fields['sub_county'].queryset = SubCounty.objects.none()

PARENTAL_STATUS_CHOICES = [
    ("both", "Have both parents"),
    ("one", "Have one parent"),
    ("orphan", "Total orphan"),
]

class FamilyBackgroundForm(forms.Form):
    parental_status = forms.ChoiceField(
        choices=PARENTAL_STATUS_CHOICES,
        widget=forms.RadioSelect,
        required=True
    )
    death_certificate = forms.FileField(required=False)

    father_age = forms.IntegerField(widget=forms.NumberInput(attrs={"min": 0}), required=False)
    father_occupation = forms.CharField(max_length=100, required=False)
    father_employer = forms.CharField(max_length=100, required=False)
    father_health_status = forms.FileField(required=False)

    mother_age = forms.IntegerField(widget=forms.NumberInput(attrs={"min": 0}), required=False)
    mother_occupation = forms.CharField(max_length=100, required=False)
    mother_employer = forms.CharField(max_length=100, required=False)
    mother_health_status = forms.FileField(required=False)

    total_siblings = forms.IntegerField(widget=forms.NumberInput(attrs={"min": 0}), required=True)
    university_siblings = forms.IntegerField(widget=forms.NumberInput(attrs={"min": 0}), required=False)
    secondary_siblings = forms.IntegerField(widget=forms.NumberInput(attrs={"min": 0}), required=False)
    out_of_school_siblings = forms.IntegerField(widget=forms.NumberInput(attrs={"min": 0}), required=False)
    out_of_school_reason = forms.CharField(max_length=255, required=False)
    working_siblings_occupation = forms.CharField(max_length=255, required=False)