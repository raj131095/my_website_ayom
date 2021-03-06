# Generated by Django 3.1 on 2020-11-06 06:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aravalli', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Create_Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=64)),
                ('shopname', models.CharField(max_length=64)),
                ('shopadd1', models.CharField(max_length=100)),
                ('shopadd2', models.CharField(max_length=100)),
                ('latitude', models.TextField()),
                ('longitude', models.TextField()),
                ('contactno', models.IntegerField()),
                ('altcontact', models.CharField(max_length=12)),
                ('opentime', models.TimeField()),
                ('closetime', models.TimeField()),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
