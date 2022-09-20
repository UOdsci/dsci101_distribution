OK_FORMAT = True

test = {
  'name': 'q2_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> bbgames.num_columns == 16
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bbgames.row(7).item('Result') == False
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bbgames.row(2).item('Result') == True
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
