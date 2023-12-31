# Generated by Django 4.2.3 on 2023-08-27 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbotApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('open', 'Abierto'), ('closed', 'Cerrado')], max_length=20)),
            ],
        ),
    ]
