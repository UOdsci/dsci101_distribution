OK_FORMAT = True

test = {
  'name': 'q13',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> disemvowel("Datascience rules!") == "Dtscnc rls!"
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
