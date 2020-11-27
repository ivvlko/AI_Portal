from django import forms
from Models.models import FaceDetection, SpamFilter, MovieReviewer, UserModel, FaceProtection


class FaceDetectionForm(forms.ModelForm):

    class Meta:
        model = FaceDetection
        fields = '__all__'
        widgets = {'strength': forms.NumberInput(attrs={'type': 'range', 'min': 1.01,
                                                        'max': 1.5, 'step': 0.01, 'id': 'slidebar'})}


class FaceProtectionForm(forms.ModelForm):

    class Meta:
        model = FaceProtection
        fields = '__all__'
        widgets = {'strength': forms.NumberInput(attrs={'type': 'range', 'min': 1.01,
                                                        'max': 1.5, 'step': 0.01, 'id': 'slidebar'})}


class SpamFilterForm(forms.ModelForm):

    class Meta:
        model = SpamFilter
        fields = '__all__'


class MovieReviewerForm(forms.ModelForm):

    class Meta:
        model = MovieReviewer
        fields = '__all__'


class UserModelForm(forms.ModelForm):

    class Meta:
        model = UserModel
        fields = '__all__'
        exclude = ['sender']