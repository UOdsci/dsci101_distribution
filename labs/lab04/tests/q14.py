OK_FORMAT = True

test = {
  'name': 'q14',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> num_non_vowels("Go bears!") == 6
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
