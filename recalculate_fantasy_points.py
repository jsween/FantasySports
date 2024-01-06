def recalculate_fantasy_points(df, scoring_sheet):

    df['FantasyPointsPerGame'].values[:] = 0
    df['FantasyPoints'].values[:] = 0

    df = df.sort_values('Position')

    df['FantasyPoints'] = df.apply(calculate_fantasy_points_by_position, args=(scoring_sheet,), axis=1)

    print(df.query('Position == "QB"'))

def calculate_fantasy_points_by_position(row, ss):
    if row['Position'] == 'QB':
        calculate_nfl_qb_fantasy_points(row, ss)
    elif row['Position'] in ['RB', 'WR', 'TE']:
        pass
    elif row['Position'] == 'DST':
        pass
    elif row['Position'] == 'K':
        pass
    elif row['Position'] in ['CB', 'LB', 'S', 'DT', 'DL', 'DE', 'OLB', 'ILB', 'DB', 'NT', 'FS', 'SS']:
        pass
    elif row['Position'] in ['FB', 'LS']:
        pass
    else:
        print(f'WARNING: Unhandled position {row["Position"]}')

def calculate_nfl_qb_fantasy_points(row, ss):
    temp_points = 0
    ss_dict = ss.scoring_rules['QB']
    print(ss_dict)
    # temp_points += ss.scoring_rules['QB']['PY'] * row['PassingYards']
    # temp_points += ss.scoring_rules['QB']['PTD'] * row['PassingTouchdowns']
    # temp_points += ss.scoring_rules['QB']['2PC'] * row['PassingInterceptions']
    # temp_points += ss.scoring_rules['QB']['RY'] * row['RushingYards']
    # temp_points += ss.scoring_rules['QB']['RTD'] * row['RushingTouchdowns']
    return temp_points
