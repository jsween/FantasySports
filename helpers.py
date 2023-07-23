def print_elapsed_time(tot_time):
    """
    Converts and prints the elapsed amount of time into a human-readable format
    Parameters:
        tot_time - amount of time that has elapsed in epoch format
    Returns:
        None
    """
    print(f'\n*** Total Elapsed Runtime: {str(int((tot_time/3600)))}:{str(int(tot_time%3600)/60)}:{str(int(tot_time%3600)%60)} ***')