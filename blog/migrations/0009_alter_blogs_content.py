# Generated by Django 4.1.2 on 2022-10-08 16:35

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_blogs_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
