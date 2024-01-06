from dataCollections import RosterTemplates as RT
from dataCollections import ScoringByPosition as SP

class ScoringSheet:
    
    def __init__(self, league):
        self.roster_template = None
        self.scoring_rules = []

        if league == 'nfl':
            self.roster_template = RT.nfl_roster_template
            self.assign_pos_scoring_rules(league)
        else:
            print(f'League {league} is not supported yet for a Scoring Sheet') 
        
    def assign_pos_scoring_rules(self, league):
        if league == 'nfl':
            self.scoring_rules = SP.nfl_scoring_dict
        else:
            print(f'WARNING: {league}\'s scoring sheet is not supported')