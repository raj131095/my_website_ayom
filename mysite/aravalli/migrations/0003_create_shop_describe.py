# Generated by Django 3.1 on 2020-11-06 06:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('aravalli', '0002_create_shop'),
    ]

    operations = [
        migrations.AddField(
            model_name='create_shop',
            name='describe',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]