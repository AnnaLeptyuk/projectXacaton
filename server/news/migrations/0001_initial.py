# Generated by Django 3.2.9 on 2021-11-04 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('autor', models.CharField(max_length=50)),
                ('news', models.SlugField()),
                ('text', models.TextField(max_length=500)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
