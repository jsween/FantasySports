from collections import namedtuple

Position = namedtuple('Position', 'name shortname starters max')

nfl_roster_template = {
    'pos1' : Position('Quarterback', 'QB', 1, 4),
    'pos2' : Position('Runningback', 'RB', 2, 4),
    'pos3' : Position('Wide Receiver', 'WR', 2, 4),
    'pos4' : Position('Tight End', 'TE', 1, 3),
    'pos5' : Position('Flex', 'FLX', 1, -1),
    'pos6' : Position('Defense Special Teams', 'DST', 1, 2),
    'pos7' : Position('Kicker', 'K', 1, 2),
    'pos8' : Position('Defensive Player', 'DP', 1, 3),
    'pos9' : Position('Bench', 'BE', 0, 5)
}