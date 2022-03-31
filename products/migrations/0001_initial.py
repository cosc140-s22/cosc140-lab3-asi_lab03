# Generated by Django 4.0.3 on 2022-03-24 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('minimum_age_appropriate', models.IntegerField(default=0)),
                ('maximum_age_appropriate', models.IntegerField(default=-1)),
            ],
        ),
    ]
