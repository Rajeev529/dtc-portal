# Generated by Django 5.1 on 2024-08-31 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_atend_bus_p_alter_atend_name_p'),
    ]

    operations = [
        migrations.AddField(
            model_name='atend',
            name='uid',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='atend',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
