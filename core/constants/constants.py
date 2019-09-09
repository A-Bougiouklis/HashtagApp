UNEXCEPTABLE_PART_OF_SPEECH = ['CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'LS', 'MD', \
                               'PRP', 'PRP$', 'TO', 'WDT', 'WP', 'WP$', 'WRB']

VERB_SUFFIX = ['ing', 'ed', 's']
VERB_TAGS = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']

IRREGULAR_COMPARATIVE_ADJECTIVES = {
    'worse' : 'bad',
    'farther': 'far',
    'better': 'good',
    'later': 'late',
    'less': 'little',
    'more': 'many'
}
IRREGULAR_SUPERLATIVE_ADJECTIVES = {
    'worst' : 'bad',
    'farthest': 'far',
    'best': 'good',
    'last': 'late',
    'latest': 'late',
    'least': 'little',
    'most': 'many'
}

STANDARD_DEVIATION_MULTIPLIER = 22