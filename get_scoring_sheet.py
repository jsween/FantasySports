from classes import ScoringSheet as SS

def get_scoring_sheet(league):
    """
    Gets the scoring sheet for the league

    Parameters: 
        league - sports league to analyze data
    Returns:
        scoring_sheet ScoringSheet to calculate points by position
    """
    scoring_sheet = SS.ScoringSheet(league)
    return scoring_sheet