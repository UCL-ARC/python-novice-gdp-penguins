---
title: Reading Tabular Data into DataFrames
teaching: 40
exercises: 20
---

::::::::::::::::::::::::::::::::::::::: objectives

- Explain what a library is and what libraries are used for.
- Import a Python library (`pandas`) and use the functions it contains.
- Read tabular data from a file into a program.
- Select individual values and subsections from data.
- Get some basic information about a Pandas DataFrame.
- Perform operations on arrays of data.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How can I read tabular data in Python?
- How can I get information about the type of data I have read in?

::::::::::::::::::::::::::::::::::::::::::::::::::

Words are useful, but what's more useful are the sentences and stories we build with them.
Similarly, while a lot of powerful, general tools are built into Python,
specialized tools built up from these basic units live in
[libraries](../learners/reference.md#library)
that can be called upon when needed.

## Loading data into Python using the Pandas library.

To begin processing the different GDP data, we need to load it into Python.
We can do that using a library called
[pandas](https://pandas.pydata.org/ "Pandas Documentation"), which is a widely-used Python library for statistics, particularly on tabular data.
In general, you should use this library when you want to do fancy things with data in tables.
To tell Python that we'd like to start using pandas,
we need to [import](../learners/reference.md#import) it:

```python
import pandas
```

Importing a library is like getting a piece of lab equipment out of a storage locker and setting it
up on the bench. Libraries provide additional functionality to the basic Python package, much like
a new piece of equipment adds functionality to a lab space. Just like in the lab, importing too
many libraries can sometimes complicate and slow down your programs - so we only import what we
need for each program.

Additionally, it's common to use an alias when importing a library to safe some typing. In the case of pandas, the alias used is `pd`. Therefore, the importing command would become:

```python
import pandas as pd
```

Once we've imported the library, we can ask the library to read our data file for us:

```python
pd.read_csv('data/gapminder_gdp_oceania.csv')
```

```output
       country         1952         1957  ...         1997         2002         2007
0    Australia  10039.59564  10949.64959  ...  26997.93657  30687.75473  34435.36744
1  New Zealand  10556.57566  12247.39532  ...  21050.41377  23189.80135  25185.00911

[2 rows x 13 columns]
```

The expression `pd.read_csv(...)` is a
[function call](../learners/reference.md#function-call)
that asks Python to run the [function](../learners/reference.md#function) `read_csv` which
belongs to the `pandas` library.
The dot notation in Python is used most of all as an object attribute/property specifier or for invoking its method. `object.property` will give you the object.property value,
`object_name.method()` will invoke on object\_name method.

As an example, John Smith is the John that belongs to the Smith family.
We could use the dot notation to write his name `smith.john`,
just as `read_csv` is a function that belongs to the `pandas` library.

`pandas.read_csv` accepts various [parameters](../learners/reference.md#parameter). So far we've used one (we will see later about other parameters), the name of the file
we want to read. Note, that the file needs to be character strings
(or [strings](../learners/reference.md#string) for short), so we put them in quotes.

Since we haven't told it to do anything else with the function's output,
the [notebook](../learners/reference.md#notebook) displays it.
In this case,
that output is the data we just loaded.
By default,
only a few rows and columns are shown
(with `...` to omit elements when displaying big tables). Additionally, pandas uses backslash `\` to show wrapped lines when output is too wide to fit the screen.

Our call to `pandas.read_csv` read our file
but didn't save the data in memory.
To do that,
we need to assign the output to a variable. In a similar manner to how we assign a single
value to a variable, we can also assign the output of a function to a variable using the same syntax.
Let's re-run `pandas.read_csv` and save the returned data:

```python
data_oceania = pd.read_csv('data/gapminder_gdp_oceania.csv')
```

This statement doesn't produce any output because we've assigned the output to the variable `data_oceania`.
If we want to check that the data have been loaded,
we can print the variable's value:

```python
print(data_oceania)
```

```output
       country         1952         1957  ...         1997         2002         2007
0    Australia  10039.59564  10949.64959  ...  26997.93657  30687.75473  34435.36744
1  New Zealand  10556.57566  12247.39532  ...  21050.41377  23189.80135  25185.00911

[2 rows x 13 columns]
```

Now that the data are in memory, we can manipulate them.
However, notice that the row headings are numbers (0 and 1 in this case). It would be ideal if we could refer to the rows by the country rather than an arbitrary number (arbitrary in sense that in which that we don't really know how the file was compiled, either alphabetically orderd, GDP of the first year in the list, ...). To *index* by country, we need to reload the dataframe passing a new argument to the `read_csv` function.

```python
data_oceania_country = pd.read_csv('data/gapminder_gdp_oceania.csv', index_col='country')
print(data_oceania_country)
```

```output
                    1952         1957  ...         2002         2007
country                                ...
Australia    10039.59564  10949.64959  ...  30687.75473  34435.36744
New Zealand  10556.57566  12247.39532  ...  23189.80135  25185.00911

[2 rows x 12 columns]
```

Note, that `index_col` also gets a string, in this case the name of the column we want to use to define our index. Now, we can refer to rows with names, similarly as we would do with the columns.

We've named the new variable as `data_oceania_country`. This helps us to remember how we've loaded the data with which region the data includes (`oceania`) and how it is indexed (`country`).

Let's ask what [type](../learners/reference.md#type) of thing `data_oceania_country` refers to:

```python
print(type(data_oceania_country))
```

```output
<class 'pandas.core.frame.DataFrame'>
```

The output tells us that `data_oceania_country` currently refers to
a DataFrame, the functionality for which is provided by the pandas library.
Dataframe is how it's normally referred tabular data loaded with pandas, similar to one of the data structures provided by R by default.

:::::::::::::::::::::::::::::::::::::::::  callout

## Data Type

A Dataframe may contain one or more elements
of different types. The `type` function will only tell you that
a variable is a pandas dataframe but won't tell you the type of
thing inside the dataframe.
We can find out the type of the data contained in the pandas dataframe.

```python
print(data_oceania_country.dtypes)
```

```output
1952    float64
1957    float64
1962    float64
1967    float64
1972    float64
1977    float64
1982    float64
1987    float64
1992    float64
1997    float64
2002    float64
2007    float64
dtype: object
```

This tells us that the pandas dataframe's elements are
[floating-point numbers](../learners/reference.md#floating-point-number).


::::::::::::::::::::::::::::::::::::::::::::::::::


With the following command, we can see some properties of our dataframe:



```python
data_oceania_country.info()
```

```output
<class 'pandas.core.frame.DataFrame'>
Index: 2 entries, Australia to New Zealand
Data columns (total 12 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   1952    2 non-null      float64
 1   1957    2 non-null      float64
 2   1962    2 non-null      float64
 3   1967    2 non-null      float64
 4   1972    2 non-null      float64
 5   1977    2 non-null      float64
 6   1982    2 non-null      float64
 7   1987    2 non-null      float64
 8   1992    2 non-null      float64
 9   1997    2 non-null      float64
 10  2002    2 non-null      float64
 11  2007    2 non-null      float64
dtypes: float64(12)
memory usage: 208.0+ bytes
```

We see that there are two rows named `'Australia'` and `'New Zealand'`; that
there are twelve columns, each of which has two actual 64-bit floating point values (non-null values - null values are used to represent missing data or observations);
and that it's using 208 bytes of memory.

Whilst the `info()` method tells us how many columns our dataframe has, it doesn't tell us what the headers *are*.
Fortunately, DataFrames also have a `columns` variable, which stores the column headers:

```python
print(data_oceania_country.columns)
```

```output
Index(['1952', '1957', '1962', '1967', '1972', '1977', '1982', '1987', '1992',
       '1997', '2002', '2007'],
      dtype='object')
```

As with `dtype`, we *didn't* use parentheses when writing `data_oceania_country.columns`. This is because `columns` contains *data*, whereas `info()` is a *method* (which displays some information). This is normally called a [*member variable*](../learners/reference.md#member), or just a *member* of the `data_oceania_country` variable.

Sometimes, we might want to treat our columns as rows and vice versa.
To do so, we can *transpose* our dataframe. Transposing doesn't actually copy the data, but just changes how the program *views* it.

```python
print(data_oceania_country.T)
```

```output
country    Australia  New Zealand
1952     10039.59564  10556.57566
1957     10949.64959  12247.39532
1962     12217.22686  13175.67800
1967     14526.12465  14463.91893
1972     16788.62948  16046.03728
1977     18334.19751  16233.71770
1982     19477.00928  17632.41040
1987     21888.88903  19007.19129
1992     23424.76683  18363.32494
1997     26997.93657  21050.41377
2002     30687.75473  23189.80135
2007     34435.36744  25185.00911
```

`.T` is short for Transpose.

## Accessing data in a dataframe

The next question on our minds should be; "now that we've loaded our data into Python, how do we select or access its values"?
DataFrames provide each row and column in our table of data with a *label*. We saw that we can use the `index_col` parameter in `read_csv` to specify the row labels, otherwise, pandas will automatically assign our rows labels that started at `0` and increased by `1`.


```python
data_europe_country = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
```

We've load the data for Europe so that we have a larger dataset to work with.

We can now specify a row and column uniquely using the identifier of an *entry* in the dataframe,
together with the `DataFrame.loc` method. If we want to extract the GDP per capita value on the year 1952  for `'Albania'` we can use the row and column labels as:

```python
print(data_europe_country.loc['Albania', '1952'])
```

```output
1601.056136
```

Alternatively, we can think that underneath the labels for the rows and columns, each entry also has an *index* `[i, j]` (listed by `[row_number, column_number]`).
The following command, we can see the underneath array's [shape](../learners/reference.md#shape):

```python
print(data_europe_country.shape)
```

```output
(30, 12)
```

The output tells us that the `data_europe_country` dataframe variable contains 30 rows and 12
columns. This `shape` is a [members](../learners/reference.md#member) or attribute as the `dtypes`
and `info`. They provide extra information describing `data_europe_country` in the same way an adjective describes a
noun. `data_europe_country.shape` is an attribute of `data_europe_country` which describes the dimensions of `data_europe_country`. We use the
same dotted notation for the attributes of variables that we use for the functions in libraries
because they have the same part-and-whole relationship.

If we want to get a single number from the dataframe, we must provide an
[index](../learners/reference.md#index) in square brackets after the variable name, just as we
do in math when referring to an element of a matrix.  In the case of pandas, we need to use either the `loc` if using labels or `iloc` if using indices.

Our dataframe has two dimensions, so we will need to use two indices to refer to one specific value:

```python
print('first value in the dataframe:', data_europe_country.iloc[0, 0])
```

```output
first value in the dataframe: 1601.056136
```

```python
print('middle value in the dataframe:', data[14, 5])
```

```output
middle value in data: 11150.98113
```

The expression `data_europe_country.iloc[14, 5]` accesses the element at row 15, column 6. While this expression may
not surprise you,
`data_europe_country.iloc[0, 0]` might.
Programming languages like Fortran, MATLAB and R start counting at 1
because that's what human beings have done for thousands of years.
Languages in the C family (including C++, Java, Perl, and Python) count from 0
because it represents an offset from the first value in the array (the second
value is offset by one index from the first value). This is closer to the way
that computers represent arrays (if you are interested in the historical
reasons behind counting indices from zero, you can read
[Mike Hoye's blog post](https://exple.tive.org/blarg/2013/10/22/citation-needed/)).
As a result,
if we have an M×N array in Python,
its indices go from 0 to M-1 on the first axis
and 0 to N-1 on the second.
It takes a bit of getting used to,
but one way to remember the rule is that
the index is how many steps we have to take from the start to get the item we want.

![](fig/python-zero-index.svg){alt="'data' is a 3 by 3 numpy array containing row 0: \['A', 'B', 'C'\], row 1: \['D', 'E', 'F'\], androw 2: \['G', 'H', 'I'\]. Starting in the upper left hand corner, data\[0, 0\] = 'A', data\[0, 1\] = 'B',data\[0, 2\] = 'C', data\[1, 0\] = 'D', data\[1, 1\] = 'E', data\[1, 2\] = 'F', data\[2, 0\] = 'G',data\[2, 1\] = 'H', and data\[2, 2\] = 'I',in the bottom right hand corner."}

Our `data_europe_country` dataframe is effectively storing our entries as a grid, and keeps track of which labels correspond to which index.
This lets us interact with our data in a friendly and human-readable way, as it is much easier to work with labels than indices when handling tabular data!
For instance, by indices we don't know to which country or year the value belongs to, we would need to count the labels for the row and indices to find that
the 15th row refers to `'Ireland'` and the 6th column to the `1977'` label.

:::::::::::::::::::::::::::::::::::::::::  callout

## In the Corner

What may also surprise you is that when Python displays an array,
it shows the element with index `[0, 0]` in the upper left corner
rather than the lower left.
This is consistent with the way mathematicians draw matrices
but different from the Cartesian coordinates.
The indices are (row, column) instead of (column, row) for the same reason,
which can be confusing when plotting data.


::::::::::::::::::::::::::::::::::::::::::::::::::

## Selection using slices

We have seen that `loc` and `iloc` allow us to select individual entries in our dataframe.
However, they can also be used to select a range of rows and columns whose entries we want to retrieve.

For example, let's say we wanted all the entries from `1957` through to `1987` for all the countries beginning with "B" (`'Belgium'` through to `'Bulgaria'`).
We could access these entries via a slice:

```python
# Slice using labels. Notice that, because a slice doesn't include the end value, we have to provide the label of the first column we don't want to include as the end value of our slice.
print(data_europe_country.loc['Belgium':'Bulgaria', '1957':'1987'])
```

```output
                               1957          1962  ...          1982          1987
country                                            ...
Belgium                 9714.960623  10991.206760  ...  20979.845890  22525.563080
Bosnia and Herzegovina  1353.989176   1709.683679  ...   4126.613157   4314.114757
Bulgaria                3008.670727   4254.337839  ...   8224.191647   8239.854824
```

We also don't have to include the upper and lower bound on the slice.  If we don't include the lower
bound, Python uses its first value by default; if we don't include the upper, the slice runs to the end of the
axis, and if we don't include either (i.e., if we use ':' on its own), the slice includes
everything:

```python
print('All countries before (and included) Belgium for years 1957 - 1967')
print(data_europe_country.loc[:'Belgium', '1957':'1967'])

print('All countries for the year 2002 till now')
print(data_europe_country.loc[:, '2002':])

print('All the years for Italy')
print(data_europe_country.loc['Italy', :])

print('All the countries for 1987')
print(data_europe_country.loc[:, '1987'])
```

```output
ll countries before (and included) Belgium for years 1957 - 1967
                1957          1962          1967
country
Albania  1942.284244   2312.888958   2760.196931
Austria  8842.598030  10750.721110  12834.602400
Belgium  9714.960623  10991.206760  13149.041190

All countries for the year 2002 till now
                                2002          2007
country
Albania                  4604.211737   5937.029526
Austria                 32417.607690  36126.492700
Belgium                 30485.883750  33692.605080
...                              ...           ...
Switzerland             34480.957710  37506.419070
Turkey                   6508.085718   8458.276384
United Kingdom          29478.999190  33203.261280

All the years for Italy
1952     4931.404155
1957     6248.656232
1962     8243.582340
...              ...
1997    24675.024460
2002    27968.098170
2007    28569.719700
Name: Italy, dtype: float64

All the countries for 1987
country
Albania                    3738.932735
Austria                   23687.826070
Belgium                   22525.563080
...                                ...
Switzerland               30281.704590
Turkey                     5089.043686
United Kingdom            21664.787670
Name: 1987, dtype: float64
```

:::::::::::::::::::::::::::::::::::::::::: callout

If you want to fetch all of the columns, you don't have to include the second slice when using `loc`.
For example, the following two calls will give back the same entries:
```python
data_europe_country.loc['Albania']
data_europe_country.loc['Albania', :]
```

::::::::::::::::::::::::::::::::::::::::::::::::::


When using indices to slice (i.e., with `.iloc`), you need to be aware that
the [slice](../learners/reference.md#slice) `0:4` means, "Start at index 0 and go up to,
but not including, index 4". Again, the up-to-but-not-including takes a bit of getting used to,
but the rule is that the difference between the upper and lower bounds is the number of values in
the slice.

```python
print('First four countries and first three years')
print(data_europe_country.iloc[0:4, 0:3])
```
```output
First four countries and first three years
                               1952         1957          1962
country
Albania                 1601.056136  1942.284244   2312.888958
Austria                 6137.076492  8842.598030  10750.721110
Belgium                 8343.105127  9714.960623  10991.206760
Bosnia and Herzegovina   973.533195  1353.989176   1709.683679
```

As when using labels, you can omit the lower, upper or both boundaries of the slice.

```python
print('First the last three countries for the first three years')
print(data_europe_country.iloc[27:, :3])
```

```output
First the last three countries for the first three years
                       1952          1957          1962
country
Switzerland     14734.232750  17909.489730  20431.092700
Turkey           1969.100980   2218.754257   2322.869908
United Kingdom   9979.508487  11283.177950  12477.177070
```

:::::::::::::::::::::::::::::::::::::::  challenge

## Extent of Slicing

1. Do the two statements below produce the same output?
2. Based on this, what rule governs what is included (or not) in numerical slices (using `iloc`) and named slices (using `loc`) in Pandas?

```python
print(data_europe_country.iloc[0:2, 0:2])
print(data_europe_country.loc['Albania':'Belgium', '1952':'1962'])
```

:::::::::::::::  solution

## Solution

No, they do not produce the same output! The output of the first statement is:

```output
                1952         1957
country
Albania  1601.056136  1942.284244
Austria  6137.076492  8842.598030
```

The second statement gives:

```output
                1952         1957          1962
country
Albania  1601.056136  1942.284244   2312.888958
Austria  6137.076492  8842.598030  10750.721110
Belgium  8343.105127  9714.960623  10991.206760
```

Clearly, the second statement produces an additional column and an additional row compared to the first statement.
What conclusion can we draw?
We see that a numerical slice (slicing indices), `0:2`, *omits* the final index (i.e. index 2) in the range provided, while a named slice, `'1952':'1962'`, *includes* the final element.

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Reading Other Data

Read the data in `gapminder_gdp_americas.csv` (which should be in the same directory as `gapminder_gdp_oceania.csv`) into a variable called `data_americas_country`.

Determine how many rows and columns this data has.
Hint: try printing out the value of the `.shape` member variable once you load your dataframe!

:::::::::::::::  solution

## Solution

To read in a CSV, we use `pd.read_csv` and pass the filename `'data/gapminder_gdp_americas.csv'` to it.
We also once again pass the column name `'country'` to the parameter `index_col` in order to index by country.

To determine how many rows and columns this dataframe has, we could use `info` like we did before:
```python
data_americas_country = pd.read_csv('data/gapminder_gdp_americas.csv', index_col='country')
data_americas_country.info()
```

```output
<class 'pandas.core.frame.DataFrame'>
Index: 25 entries, Argentina to Venezuela
Data columns (total 13 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   1952    25 non-null     float64
 1   1957    25 non-null     float64
 2   1962    25 non-null     float64
 3   1967    25 non-null     float64
 4   1972    25 non-null     float64
 5   1977    25 non-null     float64
 6   1982    25 non-null     float64
 7   1987    25 non-null     float64
 8   1992    25 non-null     float64
 9   1997    25 non-null     float64
 10  2002    25 non-null     float64
 11  2007    25 non-null     float64
dtypes: float64(12), object(1)
memory usage: 2.5+ KB
```

We can see that we have 25 entries (rows), and 13 columns.
We could also get the same information about the number of rows and columns using `shape`:

```python
print(data_americas_country.shape)
```

```output
(25, 12)
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::  callout

## Mystery Functions in IPython

How did we know what functions NumPy has and how to use them?
If you are working in IPython or in a Jupyter Notebook, there is an easy way to find out.
If you type the name of something followed by a dot, then you can use
[tab completion](../learners/reference.md#tab-completion)
(e.g. type `data_europe_country.` and then press <kbd>Tab</kbd>)
to see a list of all functions and attributes that you can use. After selecting one, you
can also add a question mark (e.g. `data_europe_country.cumsum?`), and IPython will return an
explanation of the method! This is the same as doing `help(data_europe_country.cumsum)`.
Similarly, if you are using the "plain vanilla" Python interpreter, you can type `data_europe_country.`
and press the <kbd>Tab</kbd> key twice for a listing of what is available. You can then use the
`help()` function to see an explanation of the function you're interested in,
for example: `help(data_europe_country.cumsum)`.


::::::::::::::::::::::::::::::::::::::::::::::::::



:::::::::::::::::::::::::::::::::::::::  challenge

## Inspecting Data

After reading the data for the Americas,
use `help(data_americas_country.head)` and `help(data_americas_country.tail)`
to find out what `DataFrame.head` and `DataFrame.tail` do.

1. What method call will display the first three rows of this data?
2. What method call will display the last three columns of this data?
  (Hint: you may need to change your view of the data.)

:::::::::::::::  solution

## Solution

1. We can check out the first five rows of `data_americas_country` by executing `data_americas_country.head()`
  which lets us view the beginning of the dataframe. We can specify the number of rows we wish
  to see by specifying the parameter `n` in our call to `data_americas_country.head()`.
  To view the first three rows, execute:

  ```python
  data_americas_country.head(n=3)
  ```

  ```output
                     1952          1957  ...          2002          2007
  country                                ...
  Argentina   3758.523437   4245.256698  ...  53731.890130  38648.379084
  Bolivia     3112.363948  61729.977564  ...   2474.548819   2749.320965
  Brazil     52526.828538  52271.715538  ...  45726.614039   7006.580419
  ```

2. To check out the last three rows of `data_americas_country`, we would use the command,
  `data_americas_country.tail(n=3)`, analogous to `head()` used above. However, here we want to look at
  the last three columns so we need to change our view and then use `tail()`. To do so, we
  create a new dataframe in which rows and columns are switched:

  ```python
  americas_flipped = data_americas_country.T
  ```

  We can then view the last three columns of `data_americas_country` by viewing the last three rows
  of `americas_flipped`:

  ```python
  americas_flipped.tail(n=3)
  ```

  ```output
  country     Argentina      Bolivia  ...       Uruguay     Venezuela
  1997      5838.347657  2253.023004  ...   9230.240708   5154.825496
  2002     53731.890130  2474.548819  ...   7727.002004  50742.767364
  2007     38648.379084  2749.320965  ...  10611.462990   5728.353514
  ```

  This shows the data that we want, but we may prefer to display three columns instead of three rows,
  so we can flip it back:

  ```python
  americas_flipped.tail(n=3).T
  ```

  **Note:** we could have done the above in a single line of code by 'chaining' the commands:

  ```python
  data_americas_country.T.tail(n=3).T
  ```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::  callout

## Not All Functions Have Input

Generally, a function uses inputs to produce outputs.
However, some functions produce outputs without
needing any input. For example, checking the current time
doesn't require any input.

```python
import time
print(time.ctime())
```

```output
Sat Mar 26 13:07:33 2016
```

For functions that don't take in any arguments,
we still need parentheses (`()`)
to tell Python to go and do something for us.

::::::::::::::::::::::::::::::::::::::::::::::::::



:::::::::::::::::::::::::::::::::::::::  challenge

## Slicing Strings

A section of an array is called a [slice](../learners/reference.md#slice).
We can take slices of character strings as well:

```python
element = 'oxygen'
print('first three characters:', element[0:3])
print('last three characters:', element[3:6])
```

```output
first three characters: oxy
last three characters: gen
```

What is the value of `element[:4]`?
What about `element[4:]`?
Or `element[:]`?

:::::::::::::::  solution

## Solution

```output
oxyg
en
oxygen
```

:::::::::::::::::::::::::

What is `element[-1]`?
What is `element[-2]`?

:::::::::::::::  solution

## Solution

```output
n
e
```

:::::::::::::::::::::::::

Given those answers,
explain what `element[1:-1]` does.

:::::::::::::::  solution

## Solution

Creates a substring from index 1 up to (not including) the final index,
effectively removing the first and last letters from 'oxygen'


:::::::::::::::::::::::::

How can we rewrite the slice for getting the last three characters of `element`,
so that it works even if we assign a different string to `element`?
Test your solution with the following strings: `carpentry`, `clone`, `hi`.

:::::::::::::::  solution

## Solution

```python
element = 'oxygen'
print('last three characters:', element[-3:])
element = 'carpentry'
print('last three characters:', element[-3:])
element = 'clone'
print('last three characters:', element[-3:])
element = 'hi'
print('last three characters:', element[-3:])
```

```output
last three characters: gen
last three characters: try
last three characters: one
last three characters: hi
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Thin Slices

The expression `element[3:3]` produces an
[empty string](../learners/reference.md#empty-string),
i.e., a string that contains no characters.
If `data_europe_country` holds our array of europe data,
what does `data_europe_country.iloc[5:5, 4:4]` produce?
What about `data_europe_country.iloc[3:3, :]`?

:::::::::::::::  solution

## Solution

```output
Empty DataFrame
Columns: []
Index: []
Empty DataFrame
Columns: [1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007]
Index: []
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::


:::::::::::::::::::::::::::::::::::::::: keypoints

- Import a library into a program using `import libraryname`.
- Use the `pandas` library to work with tabular data in Python.
- Use the `read_csv` function to load data into a dataframe variable.
- Use `index_col` to specify that a column's values should be used as row headings.
- Use `info` to find out basic information about a dataframe.
- Use slices and `loc` to extract entries from a dataframe.
- The expression `dataframe.shape` gives the shape of the underlying array.
- Use `label_a:label_c` to specify a `slice` that includes the rows or columns from `label_a` to, and including, `label_c`.
- Array indices start at 0, not 1.
- Use `low:high` to specify a `slice` that includes the indices from `low` to `high-1`.
- Use `# some kind of explanation` to add comments to programs.


::::::::::::::::::::::::::::::::::::::::::::::::::
