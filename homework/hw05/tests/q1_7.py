OK_FORMAT = True

test = {
  'name': 'q1_7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> big_table.num_columns == 14
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> big_table.row(6).item('Oregon 1st Half Score') == 35
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> big_table.row(0).item('Opponent 1st Half Score') == 6
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
