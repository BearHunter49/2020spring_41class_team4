# Generated by Django 3.0.6 on 2020-05-24 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0002_auto_20200524_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locker',
            name='l_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='locker',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='hits',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='p_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.IntegerField(default=0),
        ),
    ]
