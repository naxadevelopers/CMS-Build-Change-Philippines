# Generated by Django 2.0 on 2018-09-23 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_constructionsubsteps_call_inspector'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrimaryPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='materials/primary_photo')),
            ],
        ),
    ]