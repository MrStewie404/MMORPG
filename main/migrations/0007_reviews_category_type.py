# Generated by Django 3.2.6 on 2024-08-17 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20240817_0551'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='category_type',
            field=models.CharField(choices=[('AT', 'Принято'), ('RJ', 'Отклонено')], default='AT', max_length=2),
        ),
    ]
