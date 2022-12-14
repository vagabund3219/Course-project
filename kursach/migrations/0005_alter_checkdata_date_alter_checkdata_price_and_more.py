# Generated by Django 4.1.3 on 2022-12-07 15:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kursach', '0004_alter_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkdata',
            name='date',
            field=models.DateField(default=datetime.date(2022, 12, 7)),
        ),
        migrations.AlterField(
            model_name='checkdata',
            name='price',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to='images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='news',
            name='subtitle',
            field=models.CharField(default='2', max_length=50),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(default='2', max_length=30),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Цена'),
        ),
    ]
