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
To know about more built-in convert API, please read :model:`this API document <convert2.convert>`.

And more examples can be found in unit test code.

- `any2int example <https://github.com/MacHu-GWU/convert2-project/blob/master/tests/test_parse_int.py>`_
- `any2float example <https://github.com/MacHu-GWU/convert2-project/blob/master/tests/test_parse_float.py>`_
- `any2str example <https://github.com/MacHu-GWU/convert2-project/blob/master/tests/test_parse_str.py>`_
- `any2datetime example <https://github.com/MacHu-GWU/convert2-project/blob/master/tests/test_parse_datetime.py>`_
- `any2date example <https://github.com/MacHu-GWU/convert2-project/blob/master/tests/test_parse_date.py>`_

If it's not able to parse `datetime` or `date` from string, you can: `submit issue, request more template <https://github.com/MacHu-GWU/rolex-project/issues>`_.


.. include:: about.rst


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

