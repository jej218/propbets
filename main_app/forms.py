from django import forms
from .models import Profile

NATIONAL_ANTHEM_LENGTHS = (
    ('Over 95.5 Seconds', 'Over 95.5 Seconds ($25)'),
    ('Under 95.5 Seconds', 'Under 95.5 Seconds ($25)'),
)
ANTHEM_FIRST_QBS = (
    ('Matthew Stafford', 'Matthew Stafford ($25)'),
    ('Joe Burrow', 'Joe Burrow ($25)'),
)
ANTHEM_FIRST_COACHES = (
    ('Sean McVay', 'Sean McVay ($35)'),
    ('Zac Taylor', 'Zac Taylor ($15)'),
)
COIN_TOSS_RESULTS = (
    ('Heads', 'Heads ($25)'),
    ('Tails', 'Tails ($25)'),
)
FIRST_UNCOMMON_PLAYS = (
    ('Sack', 'Sack ($30)'),
    ('Touchdown', 'Touchdown ($20)'),
)
FIRST_HOLDING_TEAMS = (
    ('Bengals', 'Bengals ($25)'),
    ('Rams', 'Rams ($25)'),
)
FIRST_FAIR_CATCHES = (
    ('Bengals', 'Bengals ($25)'),
    ('Rams', 'Rams ($25)'),
)
TIE_AFTER_STARTS = (
    ('Yes', 'Yes ($30)'),
    ('No', 'No ($20)'),
)
FIRST_QUARTER_POINTS = (
    ('Odd', 'Odd ($25)'),
    ('Even', 'Even ($25)'),
)
FIRST_HALF_POINTS = (
    ('Odd', 'Odd ($25)'),
    ('Even', 'Even ($25)'),
)
LONGEST_GAME_PENALTIES = (
    ('Over 15.5 yards', 'Over 15.5 yards ($10)'),
    ('Under 15.5 yards', 'Under 15.5 yards ($40)'),
)
LONGEST_GAME_SCORES = (
    ('Touchdown', 'Touchdown ($25)'),
    ('Field Goal', 'Field Goal ($25)'),
)
FIRST_CHALLENGE_RESULTS = (
    ('Play Stands/Confirmed', 'Play Stands/Confirmed ($25)'),
    ('Play Overturned', 'Play Overturned ($25)'),
)
SONGS_DURING_HALFTIMES = (
    ('Over 8.5', 'Over 8.5 ($15)'),
    ('Under 8.5', 'Under 8.5 ($35)'),
)
EMINEMS_PERFORMANCE_CENSOREDS = (
    ('Yes', 'Yes ($30)'),
    ('No', 'No ($20)'),
)
GOODELL_SHOWNS = (
    ('Over 1.5', 'Over 1.5 ($25)'),
    ('Under 1.5', 'Under 1.5 ($25)'),
)
GAME_WINNERS = (
    ('Cincinnati Bengals', 'Cincinnati Bengals ($200)'),
    ('Los Angeles Rams', 'Los Angeles Rams ($200)'),
)


class ProfileForm(forms.ModelForm):
    anthem_length = forms.ChoiceField(
        choices=NATIONAL_ANTHEM_LENGTHS, widget=forms.RadioSelect(), help_text='National Anthem Length')
    anthem_qb = forms.ChoiceField(
        choices=ANTHEM_FIRST_QBS, widget=forms.RadioSelect(), help_text='Who Will Be Shown First During the National Anthem?')
    anthem_coach = forms.ChoiceField(
        choices=ANTHEM_FIRST_QBS, widget=forms.RadioSelect(), help_text='Who Will Be Shown First During the National Anthem?')
    coin_toss = forms.ChoiceField(
        choices=COIN_TOSS_RESULTS, widget=forms.RadioSelect(), help_text='Coin Toss Result')
    uncommon_play = forms.ChoiceField(
        choices=FIRST_UNCOMMON_PLAYS, widget=forms.RadioSelect(), help_text='What Will Happen First in the Game?')
    first_holding = forms.ChoiceField(
        choices=FIRST_HOLDING_TEAMS, widget=forms.RadioSelect(), help_text='Who Will be the First Team Penalized for Holding?')
    fair_catch = forms.ChoiceField(
        choices=FIRST_FAIR_CATCHES, widget=forms.RadioSelect(), help_text='Which Team Will Call for a Fair Catch First?')
    multiple_tie = forms.ChoiceField(
        choices=TIE_AFTER_STARTS, widget=forms.RadioSelect(), help_text='Will the Score Be Tied After 0-0?')
    first_quarter = forms.ChoiceField(
        choices=FIRST_QUARTER_POINTS, widget=forms.RadioSelect(), help_text='Total Points in the First Quarter Will Be?')
    first_half = forms.ChoiceField(
        choices=FIRST_HALF_POINTS, widget=forms.RadioSelect(), help_text='Total Points in the First Half Will Be?')
    longest_penalty = forms.ChoiceField(
        choices=LONGEST_GAME_PENALTIES, widget=forms.RadioSelect(), help_text='Distance Of Longest Penalty in Game')
    longest_score = forms.ChoiceField(
        choices=LONGEST_GAME_SCORES, widget=forms.RadioSelect(), help_text='What Will be the Longest Score in the Game?')
    challenge_result = forms.ChoiceField(
        choices=FIRST_CHALLENGE_RESULTS, widget=forms.RadioSelect(), help_text='Result of First Coaches Challenge')
    halftime_songs = forms.ChoiceField(
        choices=SONGS_DURING_HALFTIMES, widget=forms.RadioSelect(), help_text='How Many Songs Will Be Played During the Halftime Show?')
    eminem_censored = forms.ChoiceField(
        choices=EMINEMS_PERFORMANCE_CENSOREDS, widget=forms.RadioSelect(), help_text="Will Any Part of Eminem's Performance be Censored?")
    goodell_appearances = forms.ChoiceField(
        choices=GOODELL_SHOWNS, widget=forms.RadioSelect(), help_text='How Many Times Will Roger Goodell Be Shown?')
    game_winner = forms.ChoiceField(
        choices=GAME_WINNERS, widget=forms.RadioSelect(), help_text='Who will Win the Super Bowl?')

    class Meta:
        model = Profile
        exclude = ['points']
