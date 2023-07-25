class Roster:
    """
    A class used to represent a fantasy roster

    Attributes
    ----------
    league : str
        the league the fantasy roster belongs to (e.g. nfl, nba, mlb)
    roster_template : RosterTemplate
        a dictionary that contains the number of slots per position (e.g. Position('Position', 'ShortName', Starters, Max))
    """
    def __init__(self, league, roster_template):
        self.league = league
        self.roster_template = roster_template

    def __repr__(self) -> str:
        output = f'Roster Template Used\n\nLeague: {self.league.upper()}\n'
        output += '\tPOS  STRS  MAX\n'
        output += '-----------------------\n'
        
        for key, value in self.roster_template.items():
            output += f'{key} : {value.shortname: >4} {value.starters: 4} {value.max: 4}\n'
        
        return output