OK_FORMAT = True

test = {
  'name': 'q1_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 'did_oregon_win' in globals()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> did_oregon_win(final_scores.row(1))
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
