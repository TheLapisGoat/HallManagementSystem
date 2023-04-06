# Generated by Django 4.1.7 on 2023-04-06 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_boarderroom_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmenityRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomNumber', models.CharField(max_length=100, verbose_name='Room Number')),
                ('rent', models.FloatField(default=0, verbose_name='Rent')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amenityRoom', to='main.hall')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]