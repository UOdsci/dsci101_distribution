OK_FORMAT = True

test = {
  'name': 'q26',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> eugene_markets.num_rows == 5
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list(eugene_markets.column('city')) == ['Eugene', 'Eugene', 'Eugene', 'Eugene', 'Eugene']
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
