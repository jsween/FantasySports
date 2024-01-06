from time import time

from checks import *
from get_data import get_data
from get_fantasy_roster import get_fantasy_roster
from get_input_args import get_input_args
from get_scoring_sheet import get_scoring_sheet
from helpers import *
from recalculate_fantasy_points import recalculate_fantasy_points

# entry point to engine
def main():

    # get arguments
    in_arg = get_input_args()

    # check command line arguments
    check_command_line_arguments(in_arg)

    # get fantasy roster
    roster = get_fantasy_roster(in_arg.league)
    scoring_sheet = get_scoring_sheet(in_arg.league)

    start_time = time()
    # read league files
    df = get_data(in_arg.league)

    # generate new fantasy points
    df = recalculate_fantasy_points(df, scoring_sheet)


    # calc elapsed time
    end_time = time()
    print_elapsed_time(end_time - start_time)

if __name__ == "__main__":
    main()