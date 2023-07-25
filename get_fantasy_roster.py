from classes.Roster import Roster
from dataCollections import RosterTemplates

def get_fantasy_roster(league):
    """
    Gets the fantasy roster template

    Parameters:
        league - the fantasy sport's league (e.g. nfl)
    Returns:
        roster_template - Roster with numbered and named positions 
    """
    use_default_roster = input(f'Would you like to use the default roster for {league.upper()}? y/n\n').strip().lower()
    if use_default_roster != 'y':
        print('WARNING: Customizable roster not implemented yet. Using default roster')
        roster_template = RosterTemplates.nfl_roster_template
    else:
        roster_template = RosterTemplates.nfl_roster_template
    roster = Roster(league, roster_template)
    print(roster)