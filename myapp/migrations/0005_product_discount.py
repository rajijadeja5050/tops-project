# Generated by Django 4.1.1 on 2022-10-01 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
