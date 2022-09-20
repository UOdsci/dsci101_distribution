OK_FORMAT = True

test = {
  'name': 'q5_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure you assign histogram_difference to 1, 2 or 3!;
          >>> type(histogram_difference) == int
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> histogram_difference >= 1 and histogram_difference <= 3
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
