from django import forms

from .models import Document


class DocumentForm(forms.ModelForm):
    document = forms.FileField(
        label="Subir CV",
        widget=forms.FileInput(
            attrs={"class": "form-control form-control-lg"},
        ),
    )
    motivation_document = forms.FileField(
        label="Subir carta de motivación",
        widget=forms.FileInput(
            attrs={"class": "form-control form-control-lg"},
        ),
        required=False,
    )

    class Meta:
        model = Document
        fields = ("document","motivation_document",)
