# Generated by Django 4.1.3 on 2023-04-06 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.AddField(
            model_name='category',
            name='color_code',
            field=models.CharField(default='black', max_length=50, verbose_name='Color Code'),
        ),
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Creation Date'),
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, default='expense', max_length=200, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Update Date'),
        ),
        migrations.AlterModelTable(
            name='category',
            table='category',
        ),
    ]
