from django.db import models


# Base models for cashflow registering
class Budget_Group(models.Model):
    group_code = models.CharField(max_length=10)
    group_name = models.CharField(max_length=32)
    group_description = models.CharField(max_length=100)
    active_flag = models.BooleanField(default=True)

    def __str__(self):
        return self.group_code + "." + self.group_name


class Budget_Category(models.Model):
    group_id = models.ForeignKey(Budget_Group, null=True, on_delete=models.SET_NULL)
    category_code = models.CharField(max_length=10)
    category_name = models.CharField(max_length=32)
    category_description = models.CharField(max_length=100)
    active_flag = models.BooleanField(default=True)

    def __str__(self):
        return self.category_code + "." + self.category_name


class Budget_Transaction(models.Model):
    category_id = models.ForeignKey(
        Budget_Category, null=True, on_delete=models.SET_NULL
    )
    transaction_date = models.DateField()
    transaction_amount = models.DecimalField(decimal_places=2, max_digits=12)
    transaction_description = models.CharField(max_length=100)
    transaction_external_comment = models.CharField(max_length=4000, null=True)
    active_flag = models.BooleanField(default=True)

    def __str__(self):
        return "Amount: {};\tDate{};\tDescription: {}".format(
            self.transaction_amount,
            self.transaction_date,
            self.transaction_description,
        )


# Base models for cashflow planning
class Category_Quota(models.Model):
    category_id = models.ForeignKey(
        Budget_Category, null=True, on_delete=models.SET_NULL
    )
    quota_date = models.DateField()
    planned_amount = models.DecimalField(default=100, decimal_places=2, max_digits=12)
    quota_comment = models.CharField(max_length=100, default="comment")

    def __str__(self) -> str:
        return (
            str(Budget_Category.objects.get(pk=self.category_id.id))
            + " "
            + str(self.quota_date)
            + " "
            + str(self.planned_amount)
        )

    class Meta:
        unique_together = ("category_id", "quota_date")
