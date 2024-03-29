from django import forms



from .models import Vendor, Service, ReviewVender, ServiceDetails



class VenderRegistrationForm(forms.ModelForm):

    services = forms.ModelMultipleChoiceField(queryset=Service.objects.all(), widget=forms.CheckboxSelectMultiple)
    # services = forms.ModelMultipleChoiceField(queryset=Service.objects.all(), widget=forms.Select)

    class Meta:

        model = Vendor
        fields = ['services', 'vender_name', 'company_name','Vender_image', 'vender_phone', 'vender_email',
                 'vender_about','vender_address', 'vender_city', 'vender_state', 'vender_zip' ]
        # widgets = {
        #     'vender_name':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter Vender Name', 'required': True}),
        #     'company_name':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter Company Name', 'required': True}),
        #     'vender_phone':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter Phone Number', 'required': True}),
        #     'Vender_image':forms.FileInput(attrs={'class':'form-control', 'placeholder': 'Choose Image', 'required': True}),
        #     'vender_email':forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Enter Email', 'required': True}),
        #     'vender_address':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter Address', 'required': True}),
        #     'vender_about':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'About You', 'required': True}),
        #     'vender_city':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter City', 'required': True}),
        #     'vender_state':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter State', 'required': True}),
        #     'vender_zip':forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Enter Zipcode', 'required': True}),
        # }

class VenderUpdateForm(forms.ModelForm):

    services = forms.ModelMultipleChoiceField(queryset=Service.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:

        model = Vendor
        fields = ['services', 'vender_name', 'company_name', 'vender_phone', 'vender_email',
                 'vender_about','vender_address', 'vender_city', 'vender_state', 'vender_zip' ]
        # widgets = {

        #     'vender_name':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter Vender Name', 'required': True}),
        #     'company_name':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter Company Name', 'required': True}),
        #     'vender_phone':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter Phone Number', 'required': True}),

        #     'vender_about':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'About You', 'required': True}),
        #     'vender_email':forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Enter Email', 'required': True}),
        #     'vender_address':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter Address', 'required': True}),
        #     'vender_city':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter City', 'required': True}),
        #     'vender_state':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter State', 'required': True}),
        #     'vender_zip':forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Enter Zipcode', 'required': True}),
        # }



class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewVender
        fields = ['review', 'rating']

class servicesdetailform(forms.ModelForm):
    class Meta:

        model = ServiceDetails
        fields = ['service', 'image', 'start_price']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['service'].queryset = kwargs['initial'].get('service', None)


class updateservicesdetailform(forms.ModelForm):

    class Meta:
        model = ServiceDetails
        fields = ['service', 'image', 'start_price']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['image'].required = False
            service_queryset = kwargs.get('initial', {}).get('service', None)
            if service_queryset is not None:
                self.fields['service'].queryset = service_queryset




       
