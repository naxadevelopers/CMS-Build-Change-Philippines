# Generated by Django 2.0 on 2018-12-31 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0073_auto_20181231_0516'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='reports/')),
                ('date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('0', 'Pending'), ('1', 'Responded'), ('2', 'Rejected')], default=0, max_length=50)),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='site_reports', to='core.Site')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='site_reports', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]