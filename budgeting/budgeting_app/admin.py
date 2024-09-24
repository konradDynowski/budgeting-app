from django.contrib import admin
from .models import Budget_Group, Budget_Category, Budget_Transaction, Category_Quota

# Register your models here.
admin.site.register(Budget_Group)
admin.site.register(Budget_Category)
admin.site.register(Budget_Transaction)
admin.site.register(Category_Quota)
