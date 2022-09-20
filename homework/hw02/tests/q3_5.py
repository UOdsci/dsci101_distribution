OK_FORMAT = True

test = {   'name': 'q3_5',
    'points': 1,
    'suites': [   {   'cases': [   {
          'code': r"""
          >>> type(celsius_temperature_ranges) == np.ndarray
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> type(celsius_temperature_ranges.item(0)) == float
          True
          """,
          'hidden': False,
          'locked': False
        }],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
