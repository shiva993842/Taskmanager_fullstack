# Generated by Django 5.1.3 on 2024-11-15 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='low', max_length=10),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('yet-to-start', 'Yet-to-start'), ('in-progress', 'In-progress'), ('completed', 'Completed'), ('hold', 'Hold')], default='yet-to-start', max_length=20),
        ),
    ]
