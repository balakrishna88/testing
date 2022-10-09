# Generated by Django 4.1.1 on 2022-10-07 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogs_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogs',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='blogs',
            name='category',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blogs',
            name='pub_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='blogs',
            name='sub_category',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]