# Generated by Django 4.1.1 on 2022-10-08 15:39

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_category_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]