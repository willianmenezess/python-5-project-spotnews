# Generated by Django 4.2.3 on 2023-11-30 20:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0005_news"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="created_at",
            field=models.DateField(),
        ),
    ]
