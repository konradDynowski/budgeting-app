from django.db import models


# Base models for cashflow registering
class Budget_Group(models.Model):
    group_code = models.CharField(max_length=10)
    group_name = models.CharField(max_length=32)
    group_description = models.CharField(max_length=100)


class Budget_Category(models.Model):
    group_id = models.ForeignKey(Budget_Group, on_delete=models.CASCADE)
    category_code = models.CharField(max_length=10)
    category_name = models.CharField(max_length=32)
    category_description = models.CharField(max_length=100)
    active_flag = models.BooleanField(default=True)

    def __str__(self):
        return self.category_code + "." + self.category_name


class Budget_Transaction(models.Model):
    category_id = models.ForeignKey(Budget_Category, on_delete=models.CASCADE)
    transaction_date = models.DateField()
    transaction_amount = models.DecimalField(decimal_places=2, max_digits=12)
    transaction_description = models.CharField(max_length=100)


# Base models for cashflow planning
class Category_Quota(models.Model):
    category_id = models.ForeignKey(Budget_Category, on_delete=models.CASCADE)
    quota_date = models.DateField()
    planned_amount = models.DecimalField(decimal_places=2, max_digits=12)
    quota_comment = models.CharField(max_length=100)
