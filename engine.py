from time import time

from checks import *
from get_input_args import get_input_args
from helpers import *

# entry point to engine
def main():
    start_time = time()

    # get arguments
    in_arg = get_input_args()

    # check command line arguments
    check_command_line_arguments(in_arg)

    # calc elapsed time
    end_time = time()
    print_elapsed_time(end_time - start_time)

if __name__ == "__main__":
    main()