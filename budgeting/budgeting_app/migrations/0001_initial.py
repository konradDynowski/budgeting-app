# Generated by Django 4.2.16 on 2024-09-12 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budget_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_code', models.CharField(max_length=10)),
                ('category_name', models.CharField(max_length=32)),
                ('category_description', models.CharField(max_length=100)),
                ('active_flag', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Budget_Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_code', models.CharField(max_length=10)),
                ('group_name', models.CharField(max_length=32)),
                ('group_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category_Quota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quota_date', models.DateField()),
                ('planned_amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('quota_comment', models.CharField(max_length=100)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budgeting_app.budget_category')),
            ],
        ),
        migrations.CreateModel(
            name='Budget_Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateField()),
                ('transaction_amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('transaction_description', models.CharField(max_length=100)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budgeting_app.budget_category')),
            ],
        ),
        migrations.AddField(
            model_name='budget_category',
            name='group_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budgeting_app.budget_group'),
        ),
    ]
