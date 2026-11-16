from django import forms

class DonationForm(forms.Form):
    first_name = forms.CharField(label='Nume', max_length=100, required=True)
    last_name = forms.CharField(label='Prenume', max_length=100, required=True)
    phone = forms.CharField(label='Telefon', max_length=20, required=True)
    email = forms.EmailField(label='Email', required=True)
    amount = forms.DecimalField(label='Vreau să donez', max_digits=10, decimal_places=2, required=True)
    currency = forms.ChoiceField(label='Monedă', choices=[('RON', 'RON'), ('EUR', 'EUR'), ('USD', 'USD')], required=True)
    message = forms.CharField(label='Mesaj', widget=forms.Textarea, required=False)
