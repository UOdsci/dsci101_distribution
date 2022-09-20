OK_FORMAT = True

test = {   'name': 'q3_3',
    'points': 1,
    'suites': [   {   'cases': [   {
          'code': r"""
          >>> type(correct_products) == np.ndarray
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(correct_products)
          4
          """,
          'hidden': False,
          'locked': False
        }],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
