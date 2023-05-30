# Generated by Django 4.1.5 on 2023-04-05 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realapp', '0003_productdb_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='messagedb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Email', models.EmailField(blank=True, max_length=50, null=True)),
                ('Mobile', models.IntegerField(blank=True, null=True)),
                ('Message', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
