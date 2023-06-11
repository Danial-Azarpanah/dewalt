# Generated by Django 4.2.1 on 2023-06-10 13:36

from django.conf import settings
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone_number', models.CharField(max_length=11, unique=True, verbose_name='شماره موبایل')),
                ('fullname', models.CharField(max_length=100, verbose_name='نام و نام خوانوادگی')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ عضویت')),
                ('is_active', models.BooleanField(default=True, verbose_name='وضعیت کاربر')),
                ('is_admin', models.BooleanField(default=False, verbose_name='مدیر')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
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
        migrations.CreateModel(
            name='Otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=155, null=True, verbose_name='توکن اعتبارسنجی')),
                ('phone_number', models.CharField(max_length=11, verbose_name='شماره موبایل')),
                ('fullname', models.CharField(blank=True, max_length=50, null=True, verbose_name='نام و نام خانوادگی')),
                ('password', models.CharField(max_length=100, null=True, verbose_name='گذرواژه')),
                ('code', models.CharField(max_length=6, verbose_name=' کد فعالسازی')),
                ('expiration', models.DateTimeField(blank=True, null=True, verbose_name='تاریخ انقضا')),
            ],
            options={
                'verbose_name': 'کد اعتبارسنجی',
                'verbose_name_plural': 'کدهای اعتبارسنجی',
            },
        ),
        migrations.CreateModel(
            name='EditedUser',
            fields=[
                ('otp_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.otp')),
                ('new_phone_number', models.CharField(max_length=11, verbose_name='شماره موبایل جدید')),
            ],
            options={
                'verbose_name': 'کد تایید ویرایش پروفایل',
                'verbose_name_plural': 'کدهای تایید ویرایش پروفایل',
            },
            bases=('accounts.otp',),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=300, verbose_name='آدرس')),
                ('postal_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='کد پستی')),
                ('fullname', models.CharField(max_length=55, verbose_name='نام و نام خانوادگی')),
                ('phone_number', models.CharField(max_length=11, verbose_name='شماره تماس')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='ایمیل')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'آدرس',
                'verbose_name_plural': 'آدرس ها',
            },
        ),
    ]
