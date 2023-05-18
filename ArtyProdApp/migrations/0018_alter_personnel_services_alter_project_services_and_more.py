# Generated by Django 4.2 on 2023-05-16 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ArtyProdApp', '0017_alter_project_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='services',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ArtyProdApp.services'),
        ),
        migrations.AlterField(
            model_name='project',
            name='services',
            field=models.ManyToManyField(null=True, to='ArtyProdApp.services'),
        ),
        migrations.AlterField(
            model_name='project',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ArtyProdApp.team'),
        ),
        migrations.AlterField(
            model_name='team',
            name='personnel',
            field=models.ManyToManyField(null=True, to='ArtyProdApp.personnel'),
        ),
    ]