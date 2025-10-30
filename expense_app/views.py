from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import View,UpdateView

from expense_app.forms import ExpenseForm

from expense_app.models import Expense

from django.shortcuts import get_object_or_404

from django.urls import reverse_lazy


class Add_Expense_View(View):

    def get(self,request):

        form = ExpenseForm()

        return render(request,"expense_add.html",{"form":form})
    
    def post(self,request):

        print(request.POST)

        form = ExpenseForm(request.POST)

        if form.is_valid():

            print(form.cleaned_data)

            expense = form.save(commit = False)

            expense.user = request.user

            expense.save()

        return render(request,"expense_add.html",{"form":form})

#expenselist view

class ExpenseList(View):

    def get(self,request):

        expenses = Expense.objects.filter(user= request.user)

        return render(request,"expense_list.html",{"expenses":expenses})


#update view
#get post

class ExpenseUpdate(UpdateView):

    model = Expense

    form_class = ExpenseForm

    template_name = "expense_update.html"

    success_url = reverse_lazy("home")

    def get_queryset(self):
        
        return  Expense.objects.filter(user = self.request.user)
    

    


class ExpenseDelete(View):

    def get (self,request,**kwargs):

        id = kwargs.get("pk")

        expense = get_object_or_404(Expense, id = id,user = request.user)

        expense.delete()

        return redirect("home")
        



