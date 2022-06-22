test = {
  'name': 'q2_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> set(interval_ranges) == set([70,90,99])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> interval_ranges.item(0) == 90
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> interval_ranges.item(1) == 70
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
