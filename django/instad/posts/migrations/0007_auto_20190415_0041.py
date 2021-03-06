# Generated by Django 2.1.8 on 2019-04-15 00:41

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_post_like_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', imagekit.models.fields.ProcessedImageField(upload_to=posts.models.post_image_path)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='tmppost',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post'),
        ),
    ]
