# Generated by Django 3.1 on 2020-11-06 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aravalli', '0006_watchlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=64)),
                ('time', models.CharField(max_length=64)),
                ('comment', models.TextField()),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploadimages', to='aravalli.uploadedimage')),
            ],
        ),
    ]
