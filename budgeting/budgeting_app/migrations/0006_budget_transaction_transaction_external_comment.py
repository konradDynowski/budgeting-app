# Generated by Django 5.1.2 on 2024-11-02 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgeting_app', '0005_alter_category_quota_planned_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget_transaction',
            name='transaction_external_comment',
            field=models.CharField(max_length=4000, null=True),
        ),
    ]
