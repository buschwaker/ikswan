# Generated by Django 3.2.9 on 2022-07-08 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_alter_url_full_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='full_url',
            field=models.URLField(help_text='Введите ссылку', verbose_name='Ссылка'),
        ),
    ]