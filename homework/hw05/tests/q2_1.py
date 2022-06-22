test = {
  'name': 'q2_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> bbgames.num_columns
          15
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> set(['Opponent', 'Location', 'Date', 'OrQ1', 'OrQ2', 'OrQ3', 'OrQ4', 'OpQ1', 'OpQ2', 'OpQ3', 'OpQ4', 'OrOT1', 'OpOT1', 'OrTotal', 'OpTotal']) == set(bbgames.labels)
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
