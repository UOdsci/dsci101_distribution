OK_FORMAT = True

test = {
  'name': 'q1_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Number of columns should be 2;
          >>> california_burritos.num_columns == 2
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Number of rows should be 46;
          >>> california_burritos.num_rows == 46
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
