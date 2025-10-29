from django import forms
from expense_app.models import Expense

class ExpenseForm(forms.ModelForm):

    class Meta:

        model = Expense

        fields = ["category","title","amount","payment_date"]





