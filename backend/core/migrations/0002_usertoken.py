# Generated by Django 3.2.5 on 2022-08-28 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('user_id', models.IntegerField()),
                ('token', models.CharField(max_length=255)),
                ('expired_at', models.DateTimeField()),
            ],
        ),
    ]
