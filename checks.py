import sys

from dataCollections.Leagues import Leagues

def check_command_line_arguments(in_arg):
    """
    Checks the values passed into the engine to ensure only supported
    values are passed in.

    Parameters:
        in_arg - data structure that stores the command line arguments object
    Returns:
        None 
    """
    if in_arg is None:
        print('Does not check the command line arguments because \'get_input_args\' has not been defined.')
    else:
        print(f'Command Line Arguments: \n   league = {in_arg.league}')
        # check if league is supported yet
        if Leagues.get(in_arg.league):
            if Leagues[in_arg.league]['supported']:
                print(f'   League: {in_arg.league.upper()} is supported.')
            else:
                print(f'WARNING: League "{in_arg.league} is not supported yet.')
                sys.exit(0)
        else:
            print(f'WARNING: League "{in_arg.league}" is unknown.')
            sys.exit(0)
        