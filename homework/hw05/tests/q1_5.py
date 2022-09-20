OK_FORMAT = True

test = {
  'name': 'q1_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> big_table.num_columns
          12
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> set(['Opponent', 'Oregon 1Q', 'Oregon 2Q', 'Oregon 3Q', 'Oregon 4Q', 'Opp 1Q', 'Opp 2Q', 'Opp 3Q', 'Opp 4Q', 'Oregon Score', 'Opponent Score', 'Results']) == set(big_table.labels)
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
