# Generated by Django 2.0 on 2018-05-15 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20180515_0526'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklist',
            name='text_de',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='checklist',
            name='text_en',
            field=models.TextField(blank=True, null=True),
        ),
    ]