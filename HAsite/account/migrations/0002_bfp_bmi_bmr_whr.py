# Generated by Django 3.2 on 2023-06-16 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Whr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waist', models.CharField(max_length=10)),
                ('hip', models.CharField(max_length=10)),
                ('gender', models.SmallIntegerField(choices=[(1, 'male'), (2, 'female')], default=1)),
                ('result', models.CharField(max_length=80)),
                ('created_time', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='whrs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bmr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=10)),
                ('weight', models.CharField(max_length=10)),
                ('height', models.CharField(max_length=10)),
                ('gender', models.SmallIntegerField(choices=[(1, 'male'), (2, 'female')], default=1)),
                ('result', models.CharField(max_length=80)),
                ('created_time', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bmrs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bmi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.CharField(max_length=10)),
                ('height', models.CharField(max_length=10)),
                ('result', models.CharField(max_length=80)),
                ('created_time', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bmis', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bfp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.CharField(max_length=10)),
                ('waist', models.CharField(max_length=10)),
                ('hip', models.CharField(max_length=10)),
                ('neck', models.CharField(max_length=10)),
                ('gender', models.SmallIntegerField(choices=[(1, 'male'), (2, 'female')], default=1)),
                ('result', models.CharField(max_length=80)),
                ('created_time', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bfps', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
