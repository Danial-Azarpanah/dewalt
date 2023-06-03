# Generated by Django 4.2.1 on 2023-06-03 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_product_discounted_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='درصد تخفیف'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discounted_price',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='قیمت تخفیف خورده (تومان)'),
        ),
    ]
