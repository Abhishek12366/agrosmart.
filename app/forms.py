from urllib import request
from attr import attrs
from django import forms
from django.contrib.auth.models import User
from .models import *

GENDER=(
    ("","---Select Gender---"),
    ("Female","Female"),
    ("Male","Male"),
    ("Other","Other"),
)

SECURITY=(
    ("","---Select the security question---"),
    ("1","In what city were you born?"),
    ("2","What is the name of your favorite pet?"),
    ("3","what is the name of your first school?"),
    ("4","what is your favorite food?"),
)

#<-----Admin Add Form----->#
class AdminUserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}), required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}), required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}), required=True)

    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'password', 'confirm_password']

    def clean(self):
        special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
        cleaned_data=super(AdminUserForm, self).clean()
        username=cleaned_data.get('username')
        password=cleaned_data.get("password")
        confirm_password=cleaned_data.get("confirm_password")

        if len(username) < 8:
            self.add_error('username','Username length must be greater than 8 character.')
        if not any (char in special_characters for char in password):
            self.add_error('password','Password must contain at least one special Character.')

        if len(password)  < 8:
            self.add_error('password','Password length must be greater than 8 character.')
        if not any (char.isdigit() for char in password):
            self.add_error('password','Password must contain at least one digit.')
        if not any (char in special_characters for char in password):
            self.add_error('password','Password must contain at least one special Character.')

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not Match")

        return cleaned_data

class AdminExtraForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email ID'}), required=True)
    gender = forms.ChoiceField(choices=GENDER,widget=forms.Select(attrs={'class':'form-control'}), required=True)
    district = forms.ModelChoiceField(queryset=District.objects.all(),widget=forms.Select(attrs={'class':'form-control'}), empty_label="---Select District---", required=True)

    class Meta:
        model=Admin
        fields=['email', 'gender', 'district']

#<-----Visistor Signup Form----->#
class VisitorUserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}), required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}), required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Conform Password'}), required=True)

    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'password', 'confirm_password']

    def clean(self):
        special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
        cleaned_data=super(VisitorUserForm, self).clean()
        password=cleaned_data.get("password")
        confirm_password=cleaned_data.get("confirm_password")
        username =cleaned_data.get('username')

        if len(username) < 8:
            self.add_error('username','Username length must be greater than 8 character.')
        if not any (char in special_characters for char in password):
            self.add_error('password','Password must contain at least one special Character.')

        if len(password)  < 8:
            self.add_error('password','Password length must be greater than 8 character.')
        if not any (char.isdigit() for char in password):
            self.add_error('password','Password must contain at least one digit.')
        if not any (char in special_characters for char in password):
            self.add_error('password','Password must contain at least one special Character.')

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not Match")

        return cleaned_data

class VisitorExtraForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email ID'}), required=True)
    gender = forms.ChoiceField(choices=GENDER,widget=forms.Select(attrs={'class':'form-control'}), required=True)
    security_question = forms.ChoiceField(choices=SECURITY,widget=forms.Select(attrs={'class':'form-control'}), required=True)
    answer = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Answer for Security Question'}), required=True)
    district = forms.ModelChoiceField(queryset=District.objects.all(),widget=forms.Select(attrs={'class':'form-control'}), empty_label="---Select District---", required=True)

    class Meta:
        model=Visitor
        fields=['email', 'gender', 'district','security_question','answer']

#<-----Visistor Login Form----->#
class VisitorLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Username'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}), required=True)

#<-----Admin Login Form----->#
class AdminLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Username'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}), required=True)

#<-----Officer Signup Form----->#
class OfficerUserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}), required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}), required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Conform Password'}), required=True)

    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'password', 'confirm_password']

    def clean(self):
        special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
        cleaned_data=super(OfficerUserForm, self).clean()
        password=cleaned_data.get("password")
        confirm_password=cleaned_data.get("confirm_password")
        username=cleaned_data.get('username')

        if len(username) < 8:
            self.add_error('username','Username length must be greater than 8 character.')
        if not any (char in special_characters for char in password):
            self.add_error('password','Password must contain at least one special Character.')

        if len(password)  < 8:
            self.add_error('password','Password length must be greater than 8 character.')
        if not any (char.isdigit() for char in password):
            self.add_error('password','Password must contain at least one digit.')
        if not any (char in special_characters for char in password):
            self.add_error('password','Password must contain at least one special Character.')

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not Match")

        return cleaned_data

class OfficerExtraForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email ID'}), required=True)
    gender = forms.ChoiceField(choices=GENDER,widget=forms.Select(attrs={'class':'form-control'}), required=True)
    security_question = forms.ChoiceField(choices=SECURITY,widget=forms.Select(attrs={'class':'form-control'}), required=True)
    answer = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Answer for Security Question'}), required=True)
    district = forms.ModelChoiceField(queryset=District.objects.all(),widget=forms.Select(attrs={'class':'form-control'}), empty_label="---Select District---", required=True)

    class Meta:
        model=Officer
        fields=['email', 'gender', 'district','security_question','answer']

#<-----Officer Login Form----->#
class OfficerLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Username'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}), required=True)

#<-----Soil adding Form----->#
class SoilAddForm(forms.ModelForm):
    district = forms.ModelChoiceField(queryset=District.objects.all(),widget=forms.Select(attrs={'class':'form-control'}), empty_label="---Select District---", required=True)
    region = forms.ModelChoiceField(queryset=Region.objects.all(),widget=forms.Select(attrs={'class':'form-control'}), empty_label="---------------------", required=True)
    soil = forms.ModelChoiceField(queryset=Soil.objects.all(),widget=forms.Select(attrs={'class':'form-control'}), empty_label="---Select Soil---", required=True)

    class Meta:
        model=SoilLocationDetail
        fields=['district','region','soil']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['region'].queryset = Region.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['region'].queryset = Region.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.instance['region'].queryset = self.instance.district.region_set.order_by('name')

#<-----Find Soil Form----->#
class FindSoilForm(forms.Form):
    district = forms.ModelChoiceField(queryset=District.objects.all(),widget=forms.Select(attrs={'class':'form-control'}), empty_label="---Select District---", required=True)

#<-----Add Soil Detail Form----->#
class SoilDetailAddForm(forms.ModelForm):
    soil = forms.ModelChoiceField(queryset=Soil.objects.all(),widget=forms.Select(attrs={'class':'form-control'}), empty_label="---Select Soil---", required=True)
    detail = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Add Detail About Soil'}), required=True)
    crop = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Add Crop that can grow (Seperate crop with comma)'}), required=True)

    class Meta:
        model=SoilDetail
        fields=['soil','detail','crop']

#<-----Rainfall adding Form----->#
class RainfallDetailAddForm(forms.ModelForm):
    district = forms.ModelChoiceField(queryset=District.objects.all(),widget=forms.Select(attrs={'class':'form-control'}), empty_label="---Select District---", required=True)
    year = forms.ModelChoiceField(queryset=Year.objects.all(),widget=forms.Select(attrs={'class':'form-control'}), empty_label="---Select Year---", required=True)
    rainfall = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Add Rainfall in Centimeter'}), required=True)

    class Meta:
        model=RainfallDetail
        fields=['district','year','rainfall']

#<-----Find Soil Detail Form----->#
class FindSoilDetailForm(forms.Form):
    soil = forms.ModelChoiceField(queryset=Soil.objects.all(),widget=forms.Select(attrs={'class':'form-control'}), empty_label="---Select Soil---", required=True)

#<-----Find Rainfall Form----->#
class FindRainfallForm(forms.Form):
    district = forms.ModelChoiceField(queryset=District.objects.all(),widget=forms.Select(attrs={'class':'form-control'}), empty_label="---Select District---", required=True)

#<-----Add Soil Detail Form----->#
class CropAddForm(forms.ModelForm):
    crop = forms.ModelChoiceField(queryset=Crop.objects.all(),widget=forms.Select(attrs={'class':'form-control'}), empty_label="---Select Crop---", required=True)
    soil = forms.ModelChoiceField(queryset=Soil.objects.all(),widget=forms.Select(attrs={'class':'form-control'}), empty_label="---Select Soil---", required=True)
    min_rainfall = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Add Minimun Rainfall (in Centimeter)'}), required=True)
    max_rainfall = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Add Maximun Rainfall (in Centimeter)'}), required=True)
    detail = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Add Detail About Crop'}), required=True)

    class Meta:
        model=CropDetail
        fields=['crop','soil','min_rainfall','max_rainfall','detail']

#<-----Find Crop Form----->#
class FindCropForm(forms.Form):
    nitrogen = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter level of Nitrogen'}), required=True)
    phosphorus = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter level of Phosphorus'}), required=True)
    potassium = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter level of Potassium'}), required=True)
    temperature = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Temperature (in Celsius)'}), required=True)
    humidity = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Humidity'}), required=True)
    ph = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter pH value'}), required=True)
    rainfall = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Rainfall (in mm)'}), required=True)

#<-----Form for Request Seed----->#
class RequestSeedForm(forms.Form):
    address = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Address with Pincode'}), required=True)
    crop = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Crop You Need'}), required=True)
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter quantity in grams'}), required=True)

    class Meta:
        model=RequestSeed
        fields=['address','crop','quantity']

FERTILIZER=(
    ("","---Select Fertilizer---"),
    ("Manure","Manure"),
    ("Compost","Compost"),
    ("Rock Phospate","Rock Phospate"),
    ("Chicken Litter","Chicken Litter"),
    ("Bone Meal","Bone Meal"),
    ("Vermicompost","Vermicompost"),
)

#<-----Form for Request Fertilizer----->#
class RequestFertilizerForm(forms.Form):
    address = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Address with Pincode'}), required=True)
    fertilizer = forms.ChoiceField(choices=FERTILIZER,widget=forms.Select(attrs={'class':'form-control'}), required=True)
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter quantity in grams'}), required=True)

    class Meta:
        model=RequestFertilizer
        fields=['address','fertilizer','quantity']

#<-----Seller Signup Form----->#
class SellerUserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}), required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}), required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Conform Password'}), required=True)

    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'password', 'confirm_password']

    def clean(self):
        special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
        cleaned_data=super(SellerUserForm, self).clean()
        password=cleaned_data.get("password")
        confirm_password=cleaned_data.get("confirm_password")
        username =cleaned_data.get('username')

        if len(username) < 8:
            self.add_error('username','Username length must be greater than 8 character.')
        if not any (char in special_characters for char in password):
            self.add_error('password','Password must contain at least one special Character.')

        if len(password)  < 8:
            self.add_error('password','Password length must be greater than 8 character.')
        if not any (char.isdigit() for char in password):
            self.add_error('password','Password must contain at least one digit.')
        if not any (char in special_characters for char in password):
            self.add_error('password','Password must contain at least one special Character.')

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not Match")

        return cleaned_data

class SellerExtraForm(forms.ModelForm):
    garden = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Brand Name'}), required=True)
    logo = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'form-control'}), required=True)
    describe = forms.CharField(widget=forms.Textarea(attrs={'class':'forms-control','placeholder':'Describe about your Garden..'}), required=True)
    address = forms.CharField(widget=forms.Textarea(attrs={'class':'forms-control','placeholder':'Address of your Garden..'}), required=True)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email ID'}), required=True)
    gender = forms.ChoiceField(choices=GENDER,widget=forms.Select(attrs={'class':'form-control'}), required=True)
    security_question = forms.ChoiceField(choices=SECURITY,widget=forms.Select(attrs={'class':'form-control'}), required=True)
    answer = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Answer for Security Question'}), required=True)
    district = forms.ModelChoiceField(queryset=District.objects.all(),widget=forms.Select(attrs={'class':'form-control'}), empty_label="---Select District---", required=True)

    class Meta:
        model=Seller
        fields=['garden','logo','describe','address','email', 'gender', 'district','security_question','answer']