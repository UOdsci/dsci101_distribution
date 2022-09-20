OK_FORMAT = True

test = {   'name': 'q1_1',
    'points': 1,
    'suites': [   {   'cases': [   {  'code': r"""
                                    >>> set(["fruit name", "count"]) == set(fruits.labels)
                                    True
                                    """,
                                       'hidden': False,
                                       'locked': False},
                                    {  'code': r"""
                                    >>> len(fruits.column(0)) == 3
                                    True
                                    """,
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
