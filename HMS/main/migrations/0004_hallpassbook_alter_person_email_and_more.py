# Generated by Django 4.1.7 on 2023-04-08 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_alter_messaccount_last_update"),
    ]

    operations = [
        migrations.CreateModel(
            name="HallPassbook",
            fields=[
                (
                    "hall",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="passbook",
                        serialize=False,
                        to="main.hall",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="person",
            name="email",
            field=models.EmailField(max_length=254, verbose_name="email address"),
        ),
        migrations.AlterField(
            model_name="person",
            name="first_name",
            field=models.CharField(max_length=150, verbose_name="first name"),
        ),
        migrations.AlterField(
            model_name="person",
            name="last_name",
            field=models.CharField(max_length=150, verbose_name="last name"),
        ),
        migrations.CreateModel(
            name="SalaryExpense",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "timestamp",
                    models.DateTimeField(auto_now_add=True, verbose_name="Timestamp"),
                ),
                (
                    "demand",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=8, verbose_name="Demand"
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                ("job", models.CharField(max_length=100, verbose_name="Job")),
                (
                    "passbook",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="salaryexpenses",
                        to="main.hallpassbook",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PettyExpense",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "timestamp",
                    models.DateTimeField(auto_now_add=True, verbose_name="Timestamp"),
                ),
                (
                    "demand",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=8, verbose_name="Demand"
                    ),
                ),
                (
                    "description",
                    models.CharField(max_length=100, verbose_name="Description"),
                ),
                (
                    "passbook",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pettyexpenses",
                        to="main.hallpassbook",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
