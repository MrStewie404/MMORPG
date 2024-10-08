# Generated by Django 3.2.6 on 2024-08-11 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('ads_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('responses', models.JSONField(default=[])),
                ('materials_paths', models.JSONField(default=[])),
                ('title', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=9000)),
                ('categories', models.CharField(choices=[('TN', 'Танки'), ('HL', 'Хилы'), ('DD', 'ДД'), ('MH', 'Торговцы'), ('PM', 'Зельевар'), ('SC', 'Мастера заклинаний')], default='OT', max_length=2)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
    ]
