import argparse

def get_input_args():
    """
    Retrieves and parses the command line arguments provided by the user when
    they run the engine from a terminal window. 

    Command Line Arguments:
        1. League as --league with default value 'nfl'
    Parameters:
        None
    Returns: 
        parse_args(): - data structure that stores the command line arguments object
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--league', type=str, default='nfl', help='The league to analyze (nfl is currently only one supported)')

    return parser.parse_args()
