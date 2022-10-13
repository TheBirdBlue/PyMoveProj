'''

TEMPLATE FOR EASY COPY/PASTE

    'NAME ID': {
        'name': TEXT,
        'rank': INT,
        'level': INT,
        'hp': INT,
        'sp': INT,
        'attack': INT,
        'defense': INT,
        'special': INT,
        'experience': INT,
        'skillOne': INT,
        'skillTwo': INT,
        'skillThree': INT
    },

'''

growth = {
    'fight': {
        'include': 'Squire',
        'hpup': 4,
        'spup': 1,
        'attackup': 2,
        'defenseup': 2,
        'specialup': 1
    },
    'magic': {
        'include': 'Apprentice',
        'hpup': 2,
        'spup': 3,
        'attackup': 1,
        'defenseup': 1,
        'specialup': 3
    },
    'skill': {
        'include': 'Theif',
        'hpup': 3,
        'spup': 2,
        'attackup': 2,
        'defenseup': 1,
        'specialup': 2
    }
}

player = {
    'squire': {
        'name': 'Squire',
        'rank': 1,
        'level': 1,
        'hp': 10,
        'sp': 10,
        'attack': 5,
        'defense': 5,
        'special': 3,
        'experience': 0,
        'skillOne': 0,
        'skillTwo': 1,
        'skillThree': 0
    },
    'apprentice': {
        'name': 'Apprentice',
        'rank': 1,
        'level': 1,
        'hp': 8,
        'sp': 15,
        'attack': 3,
        'defense': 5,
        'special': 8,
        'experience': 0,
        'skillOne': 0,
        'skillTwo': 0,
        'skillThree': 0
    },
    'thief': {
        'name': 'Thief',
        'rank': 1,
        'level': 1,
        'hp': 8,
        'sp': 5,
        'attack': 3,
        'defense': 5,
        'special': 5,
        'experience': 0,
        'skillOne': 0,
        'skillTwo': 1,
        'skillThree': 2
    },
}
