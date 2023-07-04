# Generated by Django 4.2.2 on 2023-07-04 13:38

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0007_alter_blogs_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blogapp.category'),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name=django.db.models.fields.TextField),
        ),
    ]
