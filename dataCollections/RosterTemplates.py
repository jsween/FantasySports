from collections import namedtuple

Position = namedtuple('Position', 'name shortname starters max scoringrules')

nfl_roster_template = {
    'pos1' : Position('Quarterback', 'QB', 1, 4, 'QB'),
    'pos2' : Position('Runningback', 'RB', 2, 4, 'IOP'),
    'pos3' : Position('Wide Receiver', 'WR', 2, 4, 'IOP'),
    'pos4' : Position('Tight End', 'TE', 1, 3, 'IOP'),
    'pos5' : Position('Flex', 'FLX', 1, -1, 'IOP'),
    'pos6' : Position('Defense Special Teams', 'DST', 1, 2, 'DST'),
    'pos7' : Position('Kicker', 'K', 1, 2, 'K'),
    'pos8' : Position('Defensive Player', 'IDP', 1, 3, 'IDP'),
    'pos9' : Position('Bench', 'BE', 0, 5, 'ANY')
}