# Generated by Django 4.2 on 2024-02-03 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_produtos_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='url',
            field=models.TextField(max_length=10000),
        ),
    ]