# Generated by Django 4.2.2 on 2023-07-08 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0008_blogs_category_alter_blogs_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='category',
        ),
        migrations.AddField(
            model_name='blogs',
            name='categories',
            field=models.ManyToManyField(to='blogapp.category'),
        ),
    ]
