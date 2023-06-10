# Generated by Django 4.2.1 on 2023-06-10 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=11, verbose_name='شماره تماس')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('address', models.CharField(max_length=100, verbose_name='آدرس مغازه')),
                ('instagram', models.URLField(verbose_name='اینستاگرام')),
                ('youtube', models.URLField(verbose_name='یوتوب')),
            ],
            options={
                'verbose_name': 'اطلاعات تماس',
                'verbose_name_plural': 'اطلاعات تماس',
            },
        ),
    ]
