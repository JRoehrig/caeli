SPEI
====

The Standardized Precipitation Evapotranspiration Index (SPI) method fits a loglogistic distribution to
the difference between precipitation and potential evapotranspiration values (P-PET), and maps the result
to a normal distribution (z values), which correspond to the SPEI values. P-PET is usually resampled to one ore
more months.

.. list-table::
   :widths: 50 50

   * - :math:`spei \geq 2.0`
     - extremely wet
   * - :math:`1.5 \leq spei < 2.0`
     - very wet
   * - :math:`1.0 \leq spei < 1.5`
     - moderately wet
   * - :math:`-1.0 \leq spei < 1.0`
     - near normal
   * - :math:`-1.5 \leq spei < -1.0`
     - moderately dry
   * - :math:`-2.0 \leq spei < -1.5`
     - severely  dry
   * - :math:`spei \leq  -2.0`
     - extremely dry


Tutorial
________

P-PET refers to a time series of differences between precipitation and evapotranspiration of any frequency not higher
than monthly (minutely, hourly, daily, weekly, or monthly).

spei()
++++++

Input is a list or numpy.array of P-PET values. The output is an array of same size with calculated SPEI values.
Gaps in the input data (numpy.nan) are ignored and result a numpy.nan at the same position in the output array.

.. code-block::

    >>> import numpy as np
    >>> import pandas as pd
    >>> from caeli.drought_indices import spei, spei_monthly
    >>> b = [236.78906908, 264.81174819, 206.07614488, 329.1471248, 229.76300328, 88.48107583,
    ...      222.12576411, 203.1740944, 194.24915861, 233.04840882, 203.03193236, 181.99807424,
    ...      228.55427209, 239.45338575, 316.16425044, 192.11761111, 173.18384051, 285.25591321,
    ...      275.19281235, 310.7161464, 348.84101779, 330.42774158, 163.55803563, 177.16544205,
    ...      359.67310805, 282.82742497, 191.03543726, 333.89194558, 163.25115185, 322.16858475]
    >>> spei(b)
    array([-0.05447834,  0.39161421, -0.55496029,  1.28044935, -0.16899123,
           -2.21208646, -0.29378891, -0.60177122, -0.74448836, -0.11538335,
           -0.60405976, -0.93656914, -0.18873257, -0.01121518,  1.11915418,
           -0.7782526 , -1.07149926,  0.69786961,  0.54963214,  1.04873009,
            1.50833784,  1.29587081, -1.21539086, -1.01091053,  1.62564314,
            0.66256868, -0.79534214,  1.33715757, -1.21991663,  1.19488129])

.. code-block::

    >>> b = [np.nan, 264.81174819, 206.07614488, 329.1471248, 229.76300328, 88.48107583,
    ...      222.12576411, 203.1740944, 194.24915861, 233.04840882, 203.03193236, 181.99807424,
    ...      228.55427209, 239.45338575, 316.16425044, 192.11761111, 173.18384051, 285.25591321,
    ...      275.19281235, 310.7161464, 348.84101779, 330.42774158, 163.55803563, 177.16544205,
    ...      359.67310805, 282.82742497, 191.03543726, 333.89194558, np.nan, 322.16858475]
    >>> spei(b).round(1)
    array([  nan,  0.32, -0.61,  1.24, -0.23, -2.18, -0.36, -0.65, -0.79,
           -0.18, -0.66, -0.98, -0.25, -0.08,  1.07, -0.82, -1.1 ,  0.64,
            0.48,  1.  ,  1.47,  1.25, -1.24, -1.05,  1.6 ,  0.6 , -0.84,
            1.3 ,   nan,  1.15])



spei_monthly()
++++++++++++++

Generating a pandas.DataFrame with random daily P-PET values:

.. code-block::

    >>> np.random.seed(1)
    >>> index = pd.date_range('1990-01-01', '2019-12-31', freq='1d')
    >>> values = np.random.normal(100, 70, len(index))
    >>> values[values < 0] = 0.0
    >>> df = pd.DataFrame({'P-PET': values}, index=index)


Given daily data, calculate monthly SPEI:

.. code-block::

    >>> df_spei = spei_monthly(df).round(1)
    >>> with pd.option_context('display.max_rows', 4, 'display.max_columns', 8):
    ...     print(df_spei)
    ... 
           P01   P02   P03   P04  ...  SPEI09  SPEI10  SPEI11  SPEI12
    year                          ...                                
    1990  30.3  29.5  35.5  29.4  ...     0.4    -0.3     1.2    -1.4
    1991  32.1  28.7  39.4  29.7  ...    -0.4    -0.3     0.0    -0.6
    ...    ...   ...   ...   ...  ...     ...     ...     ...     ...
    2018  32.1  25.5  33.2  33.9  ...     1.8     0.9    -1.0    -0.8
    2019  23.9  28.7  30.8  37.6  ...     0.8    -0.7     0.7     1.3
    
    [30 rows x 24 columns]


Given daily data, calculate monthly SPEI for accumulated three months:

.. code-block::

    >>> df_spei = spei_monthly(df, aggregation=3).round(1)
    >>> with pd.option_context('display.max_rows', 4, 'display.max_columns', 8):
    ...     print(df_spei)
    ...
          P01-03  P02-04  P03-05  P04-06  ...  SPEI09-11  SPEI10-12  SPEI11-01  SPEI12-02
    year                                  ...
    1990    95.3    94.3   100.1    97.4  ...        0.7       -0.6       -0.2       -0.8
    1991   100.2    97.8    98.5    91.5  ...       -0.4       -0.6       -0.4       -0.7
    ...      ...     ...     ...     ...  ...        ...        ...        ...        ...
    2018    90.9    92.6    97.0    96.7  ...        1.2       -0.6       -2.0       -1.8
    2019    83.3    97.0    99.2    97.4  ...        0.5        0.8        NaN        NaN

    [30 rows x 24 columns]

Given daily data and list of months, calculate monthly SPI aggregating three months:

.. code-block::

    >>> df_spei = spei_monthly(df, aggregation=3, months=[1, 4, 7, 10]).round(1)
    >>> with pd.option_context('display.max_rows', 4, 'display.max_columns', 8):
    ...     print(df_spei)
    ...
          P01-03  P04-06  P07-09  P10-12  SPEI01-03  SPEI04-06  SPEI07-09  SPEI10-12
    year
    1990    95.3    97.4   101.1    91.9        0.6        0.8        0.8       -0.6
    1991   100.2    91.5   100.0    92.0        1.4       -0.3        0.6       -0.6
    ...      ...     ...     ...     ...        ...        ...        ...        ...
    2018    90.9    96.7   100.8    91.7       -0.3        0.6        0.7       -0.6
    2019    83.3    97.4    90.8    99.2       -1.8        0.7       -0.8        0.8

    [30 rows x 8 columns]
