# Generated by Django 2.0 on 2017-12-27 11:31

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('buysell', '0010_auto_20171227_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='', verbose_name='Enter description and contact infos'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('buy', 'Buy'), ('sell', 'Sell'), ('exchange', 'Exchange')], max_length=17, verbose_name='Product Type'),
        ),
    ]
