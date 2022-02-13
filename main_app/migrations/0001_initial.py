# Generated by Django 4.0.1 on 2022-02-13 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('anthem_length', models.CharField(choices=[('Over 95.5 Seconds', 'Over 95.5 Seconds ($25)'), ('Under 95.5 Seconds', 'Under 95.5 Seconds ($25)')], help_text='National Anthem Length', max_length=50)),
                ('anthem_qb', models.CharField(choices=[('Matthew Stafford', 'Matthew Stafford ($25)'), ('Joe Burrow', 'Joe Burrow ($25)')], help_text='Which QB Will Be Shown First During the National Anthem?', max_length=50)),
                ('anthem_coach', models.CharField(choices=[('Sean McVay', 'Sean McVay ($35)'), ('Zac Taylor', 'Zac Taylor ($15)')], help_text='Which Coach Will Be Shown First During the National Anthem?', max_length=50)),
                ('coin_toss', models.CharField(choices=[('Heads', 'Heads ($25)'), ('Tails', 'Tails ($25)')], help_text='Coin Toss Result', max_length=50)),
                ('uncommon_play', models.CharField(choices=[('Sack', 'Sack ($30)'), ('Touchdown', 'Touchdown ($20)')], help_text='Which of these Plays Will Happen First in the Game?', max_length=50)),
                ('first_holding', models.CharField(choices=[('Bengals', 'Bengals ($25)'), ('Rams', 'Rams ($25)')], help_text='Who Will be the First Team Penalized for Holding?', max_length=50)),
                ('fair_catch', models.CharField(choices=[('Bengals', 'Bengals ($25)'), ('Rams', 'Rams ($25)')], help_text='Which Team Will Call for a Fair Catch First?', max_length=50)),
                ('multiple_tie', models.CharField(choices=[('Yes', 'Yes ($30)'), ('No', 'No ($20)')], help_text='Will the Score Be Tied After 0-0?', max_length=50)),
                ('first_quarter', models.CharField(choices=[('Odd', 'Odd ($25)'), ('Even', 'Even ($25)')], help_text='Total Points in the First Quarter Will Be?', max_length=50)),
                ('first_half', models.CharField(choices=[('Odd', 'Odd ($25)'), ('Even', 'Even ($25)')], help_text='Total Points in the First Half Will Be?', max_length=50)),
                ('longest_penalty', models.CharField(choices=[('Over 15.5 yards', 'Over 15.5 yards ($10)'), ('Under 15.5 yards', 'Under 15.5 yards ($40)')], help_text='Distance Of Longest Penalty in Game', max_length=50)),
                ('longest_score', models.CharField(choices=[('Touchdown', 'Touchdown ($25)'), ('Field Goal', 'Field Goal ($25)')], help_text='What Will be the Longest Score in the Game?', max_length=50)),
                ('challenge_result', models.CharField(choices=[('Play Stands/Confirmed', 'Play Stands/Confirmed ($25)'), ('Play Overturned', 'Play Overturned ($25)')], help_text='Result of First Coaches Challenge', max_length=50)),
                ('halftime_songs', models.CharField(choices=[('Over 8.5', 'Over 8.5 ($15)'), ('Under 8.5', 'Under 8.5 ($35)')], help_text='How Many Songs Will Be Played During the Halftime Show?', max_length=50)),
                ('eminem_censored', models.CharField(choices=[('Yes', 'Yes ($30)'), ('No', 'No ($20)')], help_text="Will Any Part of Eminem's Performance be Censored?", max_length=50)),
                ('goodell_appearances', models.CharField(choices=[('Over 1.5', 'Over 1.5 ($25)'), ('Under 1.5', 'Under 1.5 ($25)')], help_text='How Many Times Will Roger Goodell Be Shown?', max_length=50)),
                ('game_winner', models.CharField(choices=[('Cincinnati Bengals', 'Cincinnati Bengals ($200)'), ('Los Angeles Rams', 'Los Angeles Rams ($200)')], help_text='Who will Win the Super Bowl?', max_length=50)),
                ('points', models.IntegerField(default=0)),
            ],
        ),
    ]
