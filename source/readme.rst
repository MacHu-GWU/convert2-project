Welcome to typarse documentation
================================================================================

Get freadked out with handling data type?

.. code-block:: python

    int <-> np.int64, np.int32 <-> float <-> np.float32, np.float64 <-> np.nan
    str <-> datetime <-> np.datetime64 <-> pd.tslib.Timestamp
    int <-> str <-> float
    ...  

It's completely a disaster and always happen if you do a lots of data wrangling using ``numpy`` and ``pandas``. 

You may also have a crawler harvesting data from internet, but you have to convert it to structured data, so you have to manually handle the ``None`` returns, string to int, float, datetime.

Trust me, ``typarse`` can save you from these.

Quick Link:

- `Homepage <https://github.com/MacHu-GWU/typarse-project>`_
- `PyPI download <https://pypi.python.org/pypi/typarse>`_
- `Online document <http://typarse.readthedocs.org/>`_
- `Usage example <example_>`_
- `API reference <http://typarse.readthedocs.org/typarse/__init__.html#module-typarse>`_
- `Download and install <install_>`_
- `Submit bugs and feature request <https://github.com/MacHu-GWU/typarse-project/issues>`_

Quick Guide
--------------------------------------------------------------------------------

First let's import ``typarse``:

.. code-block:: python

	>>> from typarse import TypeParser
	>>> p = TypeParser()

Let's see how it works:

.. code-block:: python

	>>> p.parse_int(1)
	1

	>>> p.parse_int(1.0000001) # fix the decimal accuracy error
	1

	>>> p.parse_int(0.9999999) # fix the decimal accuracy error
	1

	>>> p.parse_int(np.int64(2 ** 48)) # 281474976710656 in python3
	281474976710656L 

	>>> p.parse_int("1")
	1

	>>> p.parse_int("1.001")
	1

	>>> p.parse_int("0.999")
	1

for datetime-like type (includes ``datetime.datetime``, ``numpy.datetime64``, ``pd.tslib.Timestamp`` ), we get the timestamp, for date-like type, we get the days from ordinary.

.. code-block:: python

	>>> from datetime import datetime
	>>> p.parse_int(datetime(1969, 12, 31, 19, 0, 1))
	1

	>>> p.parse_int(date(1, 1, 1)))
	1

typarse has a powerful feature can automatically extract `numbers` from `string`.  For example you have something like: ``"temp is 13 degree"`` or ``"my house is 2540 sqft"``, you just want to get the numbers. Of course this features also works for `float`.

.. code-block:: python

	>>> p.parse_int(" a1b ")
	1

	>>> p.parse_int(" a1.001c ")
	1

If you don't want this feature and worry about mistakes, you can call this to disable that:

.. code-block:: python

	>>> p.setting.extract_number_from_text = False # use True when you need it again


.. _example:

More Usage Example
--------------------------------------------------------------------------------

So for more examples about ``parse_float``, ``parse_str``, ``parse_datetime``, ``parse_date``, go check these links:

- `parse_int example <https://github.com/MacHu-GWU/typarse-project/blob/master/typarse/tests/test_parse.py>`_
- `parse_float example <https://github.com/MacHu-GWU/typarse-project/blob/master/typarse/tests/test_parse.py>`_
- `parse_str example <https://github.com/MacHu-GWU/typarse-project/blob/master/typarse/tests/test_parse.py>`_
- `parse_datetime example <https://github.com/MacHu-GWU/typarse-project/blob/master/typarse/tests/test_parse.py>`_
- `parse_date example <https://github.com/MacHu-GWU/typarse-project/blob/master/typarse/tests/test_parse.py>`_

For `datetime` and `date` parser, if my parser doens't recognize the format, you can:

1. `submit issue, request more template <https://github.com/MacHu-GWU/typarse-project/issues>`_ 
2. add your own template to the `source code <https://github.com/MacHu-GWU/typarse-project/blob/master/typarse/timewrapper.py>`_. `datetime` format reference is `here <https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior>`_.

.. _install:

Download and Install
--------------------------------------------------------------------------------

``typarse`` requires ``numpy >= 1.6.1``, ``pandas >= 0.12.1``.

``typarse`` is released on PyPI, so all you need is:

.. code-block:: console

	$ pip install typarse

To upgrade to latest version:

.. code-block:: console
	
	$ pip install --upgrade typarse

If you want to build the source by your self, `download the source code <https://github.com/MacHu-GWU/typarse-project/archive/master.zip>`_ and:

.. code-block:: console
	
	$ cd typarse-project
	$ python setup.py build
	$ python setup.py install