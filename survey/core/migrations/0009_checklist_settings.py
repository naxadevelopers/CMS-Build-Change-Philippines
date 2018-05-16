# Generated by Django 2.0 on 2018-05-14 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_merge_20180514_0624'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(max_length=250)),
                ('education_material', models.CharField(max_length=250)),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='core.Step')),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, max_length=250, null=True)),
                ('site_display', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]