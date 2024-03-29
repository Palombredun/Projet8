# Generated by Django 2.2.2 on 2019-06-28 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20190620_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='carbohydrates_100g',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='energy_100g',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='fat_100g',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='fibers_100g',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='proteins_100g',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='purchase_places',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='salt_100g',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='saturated_fats_100g',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sugars_100g',
            field=models.FloatField(null=True),
        ),
    ]
