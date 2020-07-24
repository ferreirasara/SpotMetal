from django import forms


class SearchForm(forms.Form):
    STATUS_CHOICES = [
        ("(Any)", "(Any)"),
        ("Active", "Active"),
        ("On hold", "On hold"),
        ("Split-up", "Split-up"),
        ("Unknown", "Unknown"),
        ("Changed name", "Changed name"),
        ("Disputed", "Disputed")
    ]
    name = forms.CharField(label='Band Name', max_length=200, required=False)
    genre = forms.CharField(label='Genre', max_length=200, required=False)
    country = forms.CharField(label='Country', max_length=200, required=False)
    status = forms.ChoiceField(label='Status', choices=STATUS_CHOICES, required=False)
    yearFrom = forms.IntegerField(label='From', required=False)
    yearTo = forms.IntegerField(label='To', required=False)
    lyricalThemes = forms.CharField(label='Lyrical Themes', max_length=300, required=False)
    city = forms.CharField(label='City/state/province', max_length=200, required=False)
    label = forms.CharField(label='Label', max_length=200, required=False)
    additionalNotes = forms.CharField(label='Additional notes', max_length=300, required=False)
