from django.db import models

from user_app.models import User

# Create your models here.

class Expense(models.Model):

    category_choices = [('Food', 'Food'),
                        ('Travel','Travel'),
                        ('Shopping', 'Shopping'),
                        ('Rent','Rent'),
                        ('Other','Other')
                        ]

    category = models.CharField(max_length=30,choices= category_choices)

    user = models.ForeignKey(to=User,on_delete=models.CASCADE)

    title = models.CharField(max_length=30)

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    payment_date = models.DateField()

    created_date = models.DateTimeField(auto_now_add= True)

