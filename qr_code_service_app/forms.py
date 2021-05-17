from django import forms
from django.core import validators

QrKindTypes = [
    ('svg', 'Svg'),
    ('png', 'Png'),
    ('pdf', 'Pdf')
]

kind_content_types = dict(
    svg='image/svg+xml',
    png='image/png',
    pdf='application/pdf'
)


class HexField(forms.CharField):
    def __init__(self, **kwargs):
        super(HexField, self).__init__(max_length=6, min_length=3, **kwargs)
        self.validators.append(validators.RegexValidator(regex='^[0-9A-Fa-f]{3}(?:[0-9A-Fa-f]{3})?$'))


class QrGenerateForm(forms.Form):
    query = forms.CharField(required=True)
    kind = forms.ChoiceField(choices=QrKindTypes, required=False, initial='svg')
    light = HexField(required=False, initial='#FFFFFF', widget=forms.TextInput(attrs={'type': 'color'}))
    dark = HexField(required=False, initial='#000000', widget=forms.TextInput(attrs={'type': 'color'}))
    scale = forms.IntegerField(required=False, initial=3)

    def get_content_type(self):
        ctype = self.cleaned_data['kind']
        return kind_content_types[ctype]

    def clean_kind(self):
        if not self['kind'].html_name in self.data:
            return self.fields['kind'].initial
        return self.cleaned_data['kind']

    def clean_light(self):
        if not self['light'].html_name in self.data:
            return self.fields['light'].initial
        return self.cleaned_data['light']

    def clean_dark(self):
        if not self['dark'].html_name in self.data:
            return self.fields['dark'].initial
        return self.cleaned_data['dark']

    def clean_scale(self):
        if not self['scale'].html_name in self.data:
            return self.fields['scale'].initial
        return self.cleaned_data['scale']
