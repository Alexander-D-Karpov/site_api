# Generated by Django 4.0.1 on 2022-01-04 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_person_managers_person_date_joined_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(blank=True, upload_to='user_icons/'),
        ),
    ]
