# Generated by Django 3.0.2 on 2020-01-26 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offapi', '0003_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='nutriments',
            field=models.TextField(null=True),
        ),
    ]