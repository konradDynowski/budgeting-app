# populate_data.py
import os
import django
from datetime import datetime, timedelta
from decimal import Decimal

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "budgeting.settings")
django.setup()

# Import models
from budgeting_app.models import Budget_Group, Budget_Category, Budget_Transaction, Category_Quota

# Sample data for population
def populate_data():
    # 1. Create some Budget Groups
    groups = [
        {"group_code": "GRP1", "group_name": "General Expenses", "group_description": "All general expenses"},
        {"group_code": "GRP2", "group_name": "Savings", "group_description": "Long-term savings"},
    ]
    for group in groups:
        Budget_Group.objects.get_or_create(
            group_code=group["group_code"],
            defaults={
                "group_name": group["group_name"],
                "group_description": group["group_description"],
                "active_flag": True,
            },
        )

    # 2. Create Categories under each group
    categories = [
        {"category_code": "CAT1", "category_name": "Rent", "category_description": "Monthly rent", "group_code": "GRP1"},
        {"category_code": "CAT2", "category_name": "Groceries", "category_description": "Food and essentials", "group_code": "GRP1"},
        {"category_code": "CAT3", "category_name": "Investments", "category_description": "Investment accounts", "group_code": "GRP2"},
    ]

    for cat in categories:
        group = Budget_Group.objects.get(group_code=cat["group_code"])
        Budget_Category.objects.get_or_create(
            category_code=cat["category_code"],
            defaults={
                "category_name": cat["category_name"],
                "category_description": cat["category_description"],
                "group_id": group,
                "active_flag": True,
            },
        )

    # 3. Add Transactions for each category
    today = datetime.today().date()
    transactions = [
        {"category_code": "CAT1", "transaction_date": today, "transaction_amount": Decimal("1500.00"), "transaction_description": "Monthly rent"},
        {"category_code": "CAT2", "transaction_date": today - timedelta(days=5), "transaction_amount": Decimal("200.00"), "transaction_description": "Weekly groceries"},
        {"category_code": "CAT3", "transaction_date": today - timedelta(days=10), "transaction_amount": Decimal("500.00"), "transaction_description": "Stock purchase"},
    ]

    for trans in transactions:
        category = Budget_Category.objects.get(category_code=trans["category_code"])
        Budget_Transaction.objects.get_or_create(
            category_id=category,
            transaction_date=trans["transaction_date"],
            defaults={
                "transaction_amount": trans["transaction_amount"],
                "transaction_description": trans["transaction_description"],
                "transaction_external_comment": "Automated entry",
                "active_flag": True,
            },
        )

    # 4. Add Category Quotas
    quotas = [
        {"category_code": "CAT1", "quota_date": today, "planned_amount": Decimal("1500.00"), "quota_comment": "Rent budget"},
        {"category_code": "CAT2", "quota_date": today, "planned_amount": Decimal("250.00"), "quota_comment": "Grocery budget"},
        {"category_code": "CAT3", "quota_date": today, "planned_amount": Decimal("500.00"), "quota_comment": "Investment budget"},
    ]

    for quota in quotas:
        category = Budget_Category.objects.get(category_code=quota["category_code"])
        Category_Quota.objects.get_or_create(
            category_id=category,
            quota_date=quota["quota_date"],
            defaults={
                "planned_amount": quota["planned_amount"],
                "quota_comment": quota["quota_comment"],
            },
        )

    print("Database populated with sample data!")

# Run the function
if __name__ == "__main__":
    populate_data()

