OK_FORMAT = True

test = {
  'name': 'q1_6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> first_half_score(2, 3)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> first_half_score(-2,3)
          1
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
