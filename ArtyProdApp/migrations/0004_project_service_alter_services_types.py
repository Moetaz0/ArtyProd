# Generated by Django 4.2 on 2023-05-06 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ArtyProdApp', '0003_project_signup_remove_contact_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='service',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ArtyProdApp.services'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='services',
            name='TypeS',
            field=models.CharField(choices=[('G', 'Graphic charts'), ('M', '3D Modeling'), ('S', 'Scriptwriting')], max_length=1),
        ),
    ]