OK_FORMAT = True

test = {
  'name': 'q8_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Please actually go on Slack and look at the threads.;
          >>> # Looks like you didn't make a string.;
          >>> type(secret) == str
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(secret)
          22
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
