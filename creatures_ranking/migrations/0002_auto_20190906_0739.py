# Generated by Django 2.2.5 on 2019-09-06 07:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('creatures_ranking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='creature',
            name='number_of_votes',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vote_minus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creature2', to='creatures_ranking.Creature')),
                ('vote_plus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creature1', to='creatures_ranking.Creature')),
            ],
        ),
    ]
