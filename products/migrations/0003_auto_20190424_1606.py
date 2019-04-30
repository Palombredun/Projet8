# Generated by Django 2.1.7 on 2019-04-24 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190418_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id_category',
        ),
        migrations.AlterField(
            model_name='product',
            name='id_subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Category'),
        ),
    ]