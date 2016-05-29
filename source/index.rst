.. include:: ../README.rst


Quick Guide
-------------------------------------------------------------------------------
First, import ``convert2``::

	>>> import convert2


Parse anything to int
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Process integer and float::

	>>> convert2.any2int(1)
	1

	>>> convert2.any2int(1.001) # round to closest int
	1

	>>> convert2.any2int(0.999) # round to closest int
	1

	>>> convert2.any2int(np.int64(2 ** 48)) # 281474976710656 in python3
	281474976710656

	>>> convert2.any2int(np.int64(2 ** 48)) # 281474976710656 in python2
	281474976710656L

Process string::

	>>> convert2.any2int("1") 
	1

	>>> convert2.any2int("1.001")
	1

	>>> convert2.any2int("0.999")
	1

	>>> convert2.any2int("The house size is 2283 sqft.") # extract numbers
	2283

	# if you don't want this feature, you can disable it by
	>>> convert2.any2int.EXTRACT_NUMBER_FROM_TEXT = False

Process datetime::

	>>> from datetime import datetime
	>>> import numpy as np
	>>> import pandas as pd
	>>> convert2.any2int(datetime(1970, 1, 1, 0, 0, 1)) # get utc timestamp
	1

	>>> convert2.any2int(np.datetime64("1970-01-01 00:00:01Z")) # get utc timestamp
	1

	>>> convert2.any2int(pd.tslib.Timestamp("1970-01-01 00:00:01Z")) # get utc timestamp
	1

Process date::

	>>> from datetime import date
	>>> convert2.any2int(date())

.. code-block:: python

	>>> from datetime import datetime
	>>> p.parse_int(datetime(1969, 12, 31, 19, 0, 1))
	1

	>>> p.parse_int(date(2000, 1, 1)))
	730120

.. _example:

More Usage Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

So for more examples about ``parse_float``, ``parse_str``, ``parse_datetime``, ``parse_date``, go check these links:

- `parse_int example <https://github.com/MacHu-GWU/typarse-project/blob/master/typarse/tests/test_parse.py>`_
- `parse_float example <https://github.com/MacHu-GWU/typarse-project/blob/master/typarse/tests/test_parse.py>`_
- `parse_str example <https://github.com/MacHu-GWU/typarse-project/blob/master/typarse/tests/test_parse.py>`_
- `parse_datetime example <https://github.com/MacHu-GWU/typarse-project/blob/master/typarse/tests/test_parse.py>`_
- `parse_date example <https://github.com/MacHu-GWU/typarse-project/blob/master/typarse/tests/test_parse.py>`_

For `datetime` and `date` parser, if my parser doens't recognize the format, you can:

1. `submit issue, request more template <https://github.com/MacHu-GWU/typarse-project/issues>`_ 
2. add your own template to the `source code <https://github.com/MacHu-GWU/typarse-project/blob/master/typarse/timewrapper.py>`_. `datetime` format reference is `here <https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior>`_.


.. include:: about.rst


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

