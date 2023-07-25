from time import time

from checks import *
from get_fantasy_roster import get_fantasy_roster
from get_input_args import get_input_args
from helpers import *

# entry point to engine
def main():

    # get arguments
    in_arg = get_input_args()

    # check command line arguments
    check_command_line_arguments(in_arg)

    # get fantasy roster
    get_fantasy_roster(in_arg.league)

    start_time = time()
    # read league files


    # calc elapsed time
    end_time = time()
    print_elapsed_time(end_time - start_time)

if __name__ == "__main__":
    main()