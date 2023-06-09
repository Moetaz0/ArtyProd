# Generated by Django 4.2 on 2023-05-16 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ArtyProdApp', '0019_alter_project_services_alter_team_personnel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='services',
            new_name='service',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='username',
        ),
        migrations.RemoveField(
            model_name='personnel',
            name='services',
        ),
        migrations.RemoveField(
            model_name='project',
            name='team',
        ),
        migrations.AddField(
            model_name='personnel',
            name='service',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ArtyProdApp.services'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ArtyProdApp.project'),
        ),
        migrations.AlterField(
            model_name='services',
            name='description',
            field=models.TextField(),
        ),
    ]
