nfl_scoring_dict = {
    'IOP' : { 
        'PY' : .04, 'PTD' : 6, 
        'RY' : 0.1, 'RTD' : 6, '2PR' : 2,
        'REY' : 0.1, 'RETD' : 6, '2PRE' : 2,
        'FUML': -2, 'INT' : -2,
    },
    'K' : { 
        'PAT': 1, 'PATM': -1, 
        'FGM': -1, 'FG0': 3, 'FGM40': 4, 'FGM50': 5, 'FGM60': 7
    },
    'DST' : { 
        'SK': 1, 'INT': 3, 'FR': 2, 'FF': 1, 'SF': 2,
        'INTTD': 6, 'FRTD': 6, 'KRTD': 6, 'PRTD': 6, 'BLKKRTD': 6,
        'BLKK': 2,
        'PA0': 8, 'PA1': 7, 'PA7': 6, 'PA14': 5, 'PA18': 3, 'PA22': 1,
        'PA35': -1, 'PA46': -5,
        'YA100': 6, 'YA199': 5, 'YA249': 4, 'YA349': 3, 'YA399': 2, 
        'YA499': -1, 'YA549': -2, 'YA550': -4,
        '2PTRET': 2, '1PSF': 1 
    },
    'IDP' : { 
        'SK': 4, 'TK': 1, 'BLKK': 2, 'INT': 5, 'FR': 5, 'SF': 2, 'TD': 6
    }
}