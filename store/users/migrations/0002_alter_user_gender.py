# Generated by Django 4.2.1 on 2023-05-17 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Мужчина'), ('F', 'Женщина'), ('O', 'Другое')], max_length=1, null=True),
        ),
    ]
