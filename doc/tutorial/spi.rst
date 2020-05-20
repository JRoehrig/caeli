SPI
===

The Standardized Precipitation Index (SPI) method fits a gamma distribution to precipitation values and maps the result
to a normal distribution (z values), which correspond to the SPI values. Precipitation is usually resampled to one ore
more months.

.. list-table::
   :widths: 50 50

   * - :math:`spi \geq 2.0`
     - extremely wet
   * - :math:`1.5 \leq spi < 2.0`
     - very wet
   * - :math:`1.0 \leq spi < 1.5`
     - moderately wet
   * - :math:`-1.0 \leq spi < 1.0`
     - near normal
   * - :math:`-1.5 \leq spi < -1.0`
     - moderately dry
   * - :math:`-2.0 \leq spi < -1.5`
     - severely  dry
   * - :math:`spi \leq  -2.0`
     - extremely dry

From `European Drought Observatory <https://edo.jrc.ec.europa.eu/documents/factsheets/factsheet_spi.pdf>`_: The SPI
indicator shows the anomalies (deviations from the mean) of the observed total precipitation, for any given
location and accumulation period of interest. The magnitude of the departure from the mean is a probabilistic measure
of the severity of a wet or dry event. Since SPI can be calculated over different precipitation accumulation periods
(typically ranging from 1 to 48 months), the resulting different SPI indicators allow for estimating different
potential impacts of a meteorological drought:

* SPI-1 to SPI-3: When SPI is computed for shorter accumulation periods (e.g.,1 to 3 months), it can be  used as an
  indicator for immediate  impacts such as reduced soil moisture, snowpack, and flow in smaller creeks.
* SPI-3 to SPI-12: When SPI is computed for medium accumulation periods (e.g.,3 to 12 months), it can be used as an
  indicator for reduced stream flow and reservoir storage.
* SPI-12 to SPI-48: When SPI is computed for longer accumulation periods (e.g.,12 to 48 months), it can be used as an
  indicator for reduced reservoir and groundwater recharge.

Tutorial
________


spi()
+++++

Input is a list or numpy.array of precipitation values of any frequency (e.g., weekly, monthly, bimonthly, etc.). The output
is an array of same size with calculated SPI values. Gaps in the input data (numpy.nan) are ignored and return a
numpy.nan at the same position in the output array.

.. code-block::

    >>> import numpy as np
    >>> import pandas as pd
    >>> from caeli.drought_indices import spi, spi_monthly
    >>> p = [286.08, 321.11, 260.34, 383.07, 277.56, 150.5, 272.63, 246.31, 254.92, 288.5,
    ...      267.12, 242.51, 286.56, 285.43, 370.03, 241.54, 233.65, 336.29, 330.73, 360.46,
    ...      407.13, 381.74, 217.2, 232.68, 418.64, 338.96, 246.49, 391.28, 223.81, 387.61]
    >>> spi(p)
    array([-0.09871128,  0.40370729, -0.49477568,  1.21005166, -0.22705906,
           -2.5764311 , -0.3025364 , -0.72186805, -0.58150079, -0.06272324,
           -0.38798647, -0.78487656, -0.09155701, -0.10841216,  1.04789177,
           -0.80106745, -0.93443395,  0.6101345 ,  0.53525523,  0.92648763,
            1.50004374,  1.19367916, -1.22268976, -0.95104038,  1.6348398 ,
            0.64580242, -0.71889983,  1.31030572, -1.10512868,  1.26566184])

.. code-block::

    >>> p = [np.nan, 321.11, 260.34, 383.07, 277.56, 150.5, 272.63, 246.31, 254.92, 288.5,
    ...      267.12, 242.51, 286.56, 285.43, 370.03, 241.54, 233.65, 336.29, 330.73, 360.46,
    ...      407.13, 381.74, 217.2, 232.68, 418.64, 338.96, 246.49, 391.28, np.nan, 387.61]
    >>> spi(p).round(1)
    [ nan  0.4 -0.5  1.2 -0.3 -2.6 -0.3 -0.8 -0.6 -0.1 -0.4 -0.8 -0.1 -0.2
      1.  -0.8 -1.   0.6  0.5  0.9  1.4  1.1 -1.3 -1.   1.6  0.6 -0.8  1.3
      nan  1.2]


spi_monthly()
+++++++++++++

spi_monthly() requires a pandas.DataFrame as input data with pandas.DatetimeIndex as index in any frequency
(e.g., minutely, hourly, subdaily, daily, etc.).

We first generate a pandas.DataFrame with random daily precipitation values as example:

.. code-block::

    >>> np.random.seed(1)
    >>> index = pd.date_range('1990-01-01', '2019-12-31', freq='1d')
    >>> values = np.random.normal(1, 0.7, len(index))
    >>> values[values < 0] = 0.0
    >>> df = pd.DataFrame({'P': values}, index=index)
    >>> df
                       P
    1990-01-01  2.137042
    1990-01-02  0.571771
    ...              ...
    2019-12-30  1.285051
    2019-12-31  0.565803

    [10957 rows x 1 columns]


Calculate monthly SPI for the generate daily data:

.. code-block::

    >>> df_spi = spi_monthly(df).round(1)
    >>> with pd.option_context('display.max_rows', 4, 'display.max_columns', 8):
    ...     print(df_spi)
    ...
           P01   P02   P03   P04  ...  SPI09  SPI10  SPI11  SPI12
    year                          ...
    1990  30.3  29.5  35.5  29.4  ...    0.4   -0.3    1.1   -1.4
    1991  32.1  28.7  39.4  29.7  ...   -0.4   -0.3    0.1   -0.5
    ...    ...   ...   ...   ...  ...    ...    ...    ...    ...
    2018  32.1  25.5  33.2  33.9  ...    1.9    0.8   -0.9   -0.7
    2019  23.9  28.7  30.8  37.6  ...    0.8   -0.7    0.7    1.2

    [30 rows x 24 columns]


Given daily data, calculate monthly SPI for accumulated three months:

.. code-block::

    >>> spi_monthly(df, aggregation=3).round(1)
          P01-03  P02-04  P03-05  P04-06  ...  SPI09-11  SPI10-12  SPI11-01  SPI12-02
    year                                  ...
    1990    95.3    94.3   100.1    97.4  ...       0.7      -0.5      -0.2      -0.8
    1991   100.2    97.8    98.5    91.5  ...      -0.4      -0.5      -0.3      -0.7
    ...      ...     ...     ...     ...  ...       ...       ...       ...       ...
    2018    90.9    92.6    97.0    96.7  ...       1.1      -0.5      -2.3      -1.8
    2019    83.3    97.0    99.2    97.4  ...       0.4       0.8       NaN       NaN

Given daily data and list of months, calculate monthly SPI for accumulated three months:

.. code-block::

    >>> spi_monthly(df, aggregation=3, months=[1, 4, 7, 10]).round(1)
          P01-03  P02-04  P03-05  P04-06  ...  SPI09-11  SPI10-12  SPI11-01  SPI12-02
    year                                  ...
    1990    95.3    94.3   100.1    97.4  ...       0.7      -0.5      -0.2      -0.8
    1991   100.2    97.8    98.5    91.5  ...      -0.4      -0.5      -0.3      -0.7
    ...      ...     ...     ...     ...  ...       ...       ...       ...       ...
    2018    90.9    92.6    97.0    96.7  ...       1.1      -0.5      -2.3      -1.8
    2019    83.3    97.0    99.2    97.4  ...       0.4       0.8       NaN       NaN