OK_FORMAT = True

test = {
  'name': 'q42',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> proportion_in_20th_century == 0.684
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> proportion_in_21st_century == 0.316
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
