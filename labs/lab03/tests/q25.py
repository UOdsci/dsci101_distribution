OK_FORMAT = True

test = {
  'name': 'q25',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(farmers_markets_locations_by_latitude) == tables.Table
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(farmers_markets_locations_by_latitude.take(range(3)).column('y'), np.array([64.86275, 64.8459, 64.844414])).all()
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
