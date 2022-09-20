OK_FORMAT = True

test = {
  'name': 'q1_1',
  'points': 1,
  'suites': [
    {
      'cases': [
      {   'code': '>>> import numpy as np;\n'
                                               ">>> # It looks like you didn't "
                                               'make an array.;\n'
                                               '>>> type(weird_numbers) == '
                                               'np.ndarray\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False
                                       },
        {
          'code': r"""
          >>> # Make sure you have four elements in your array;
          >>> len(weird_numbers) == 4
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
