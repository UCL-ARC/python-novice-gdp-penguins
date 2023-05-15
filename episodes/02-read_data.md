---
title: Reading Tabular Data into DataFrames
teaching: 40
exercises: 20
---

::::::::::::::::::::::::::::::::::::::: objectives

- Import the Pandas library.
- Use Pandas to load a CSV data set.
- Retrieve some basic information about a Pandas dataframe.

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

[Pandas](https://pandas.pydata.org) is a widely-used Python library for statistics, particularly when processing tabular data.
We will use Pandas to read in our data files;
- First, we must tell Python that we want to use the Pandas library. We can do this using the [`import`](../learners/reference.md#library) command.
- Then, we can use the `read_csv` function from Pandas to read one of our data files into a dataframe. This function takes the name of a file as an argument, and returns a dataframe that we can assign to a variable.

```python
import pandas as pd # Tells Python we want to use the Pandas library

# Load the data using Pandas' read_csv method
data_oceania = pd.read_csv('data/gapminder_gdp_oceania.csv')

# Display the data
print(data_oceania)
```

```output
       country  gdpPercap_1952  gdpPercap_1957  gdpPercap_1962  \
0    Australia     10039.59564     10949.64959     12217.22686
1  New Zealand     10556.57566     12247.39532     13175.67800

   gdpPercap_1967  gdpPercap_1972  gdpPercap_1977  gdpPercap_1982  \
0     14526.12465     16788.62948     18334.19751     19477.00928
1     14463.91893     16046.03728     16233.71770     17632.41040

   gdpPercap_1987  gdpPercap_1992  gdpPercap_1997  gdpPercap_2002  \
0     21888.88903     23424.76683     26997.93657     30687.75473
1     19007.19129     18363.32494     21050.41377     23189.80135

   gdpPercap_2007
0     34435.36744
1     25185.00911
```
- The columns in a dataframe are the observed variables, and the rows are the observations.
- Pandas uses backslash `\` to show wrapped lines when output is too wide to fit the screen.
- Using descriptive dataframe names helps us distinguish between multiple DataFrames so we won't accidentally overwrite a dataframe or read from the wrong one.

:::::::::::::::::::::::::::::::::::::::::  callout

## File Not Found

Our lessons store their data files in a `data` sub-directory,
which is why the path to the file is `data/gapminder_gdp_oceania.csv`.
If you forget to include `data/`,
or if you include it but your copy of the file is somewhere else,
you will get a [runtime error](04-built-in.md)
that ends with a line like this:

```error
FileNotFoundError: [Errno 2] No such file or directory: 'data/gapminder_gdp_oceania.csv'
```

::::::::::::::::::::::::::::::::::::::::::::::::::

## Aliases and dot notation
There are a couple of extra things going on in the commands we just ran, so let's take a closer look at them.

```python
import pandas as pd # Tells Python we want to use the Pandas library
```

We `import`ed Pandas `as pd`:
- This means that we can refer to the Pandas library (and functions inside it) by typing `pd` as opposed to `pandas`.
- This will be the case so long as we stay working in the same JupyterLab notebook or script. If you make a new Python notebook or script, you'll need to import Pandas again.

```python
data_oceania = pd.read_csv('data/gapminder_gdp_oceania.csv')
```

We had to write `pd.read_csv` as opposed to just `read_csv` to load the data.
- This is because we want to tell Python to specifically look in the Pandas library for a function called `read_csv`.
- The `pd.` tells Python to look in the Pandas library (remember, we gave Pandas the name `pd` when we imported it).
- The `read_csv` is the name of the function to run.
- The `data/gapminder_gdp_oceania.csv` is the argument that we pass to the `read_csv` function. In this case, it's the name of the data file we want to read.
- `data_oceania` is the variable we want to save the output of `read_csv` to.
The dot notation in Python is used most of all as an object attribute/property specifier or for invoking its method. `object.property` will give you the `object.property` value, `object_name.method()` will invoke on `object_name` method or function.

## Specifying row headings

You might notice that our `data_oceania` dataframe is displaying the row headings as numbers - in this case `0` and `1`.
Additionally, the first column of each row contains the name of the country whose data is stored in that row.
We would like to be able to index our rows by the country rather than numbers.
- We can pass the name of the column which contains the row headers to `read_csv` as its `index_col` parameter to fix this.

```python
# Read the data file, specifying that the column "country" contains the names (indices) to be used for the rows
data_oceania = pd.read_csv('data/gapminder_gdp_oceania.csv', index_col='country')

print(data_oceania)
```

```output
             gdpPercap_1952  gdpPercap_1957  gdpPercap_1962  gdpPercap_1967  \
country
Australia       10039.59564     10949.64959     12217.22686     14526.12465
New Zealand     10556.57566     12247.39532     13175.67800     14463.91893

             gdpPercap_1972  gdpPercap_1977  gdpPercap_1982  gdpPercap_1987  \
country
Australia       16788.62948     18334.19751     19477.00928     21888.88903
New Zealand     16046.03728     16233.71770     17632.41040     19007.19129

             gdpPercap_1992  gdpPercap_1997  gdpPercap_2002  gdpPercap_2007
country
Australia       23424.76683     26997.93657     30687.75473     34435.36744
New Zealand     18363.32494     21050.41377     23189.80135     25185.00911
```

Now when we print out our dataframe we can see that the rows are identified by country, rather than by a number.

## Working with DataFrames

We know that the `data_oceania` variable contains a dataframe, but how do we actually know *what's in* this dataframe?
Or how many rows it has?
Or the *type of* data stored in the columns?

To obtain an overview of our dataframe, we can use the `info()` method.

```python
data_oceania.info()
```

```output
<class 'pandas.core.frame.DataFrame'>
Index: 2 entries, Australia to New Zealand
Data columns (total 12 columns):
 #   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   gdpPercap_1952  2 non-null      float64
 1   gdpPercap_1957  2 non-null      float64
 2   gdpPercap_1962  2 non-null      float64
 3   gdpPercap_1967  2 non-null      float64
 4   gdpPercap_1972  2 non-null      float64
 5   gdpPercap_1977  2 non-null      float64
 6   gdpPercap_1982  2 non-null      float64
 7   gdpPercap_1987  2 non-null      float64
 8   gdpPercap_1992  2 non-null      float64
 9   gdpPercap_1997  2 non-null      float64
 10  gdpPercap_2002  2 non-null      float64
 11  gdpPercap_2007  2 non-null      float64
dtypes: float64(12)
memory usage: 208.0+ bytes
```

This output is telling us that the `data_oceania` dataframe:
- Has two rows (entries), the first being `'Australia'` and the last being `'New Zealand'`.
- Has twelve columns per row.
  - Each row has 2 non-null values. Null values are used to represent missing data or observations.
  - All of the columns have data whose type is `float64` - that is, a floating point number like we saw in the previous lesson.
- The only variable (or datatype, `dtype`) used is `float64`, and it is used in 12 columns (that is, all of them).
- Is using 208 bytes of memory.

Whilst the `info()` method tells us how many columns our dataframe has, it doesn't tell us what the headers *are*.
Fortunately, DataFrames also have a `columns` variable, which stores the column headers:

```python
print(data_oceania.columns)
```

```output
Index(['gdpPercap_1952', 'gdpPercap_1957', 'gdpPercap_1962', 'gdpPercap_1967',
       'gdpPercap_1972', 'gdpPercap_1977', 'gdpPercap_1982', 'gdpPercap_1987',
       'gdpPercap_1992', 'gdpPercap_1997', 'gdpPercap_2002', 'gdpPercap_2007'],
      dtype='object')
```

- Notice that we *didn't* use parentheses when writing `data_oceania.columns`. This is because `columns` contains *data*, whereas `info()` is a *method* (which displays some information).
- `columns` is called a *member variable*, or just a *member* of the `data_oceania` variable.

Finally, we might want to treat our columns as rows and vice versa.
To do so, we can *transpose* our dataframe:
  - Transposing doesn't actually copy the data, but just changes how the program *views* it.

```python
print(data_oceania.T) # .T is short for Transpose
```

```output
country           Australia  New Zealand
gdpPercap_1952  10039.59564  10556.57566
gdpPercap_1957  10949.64959  12247.39532
gdpPercap_1962  12217.22686  13175.67800
gdpPercap_1967  14526.12465  14463.91893
gdpPercap_1972  16788.62948  16046.03728
gdpPercap_1977  18334.19751  16233.71770
gdpPercap_1982  19477.00928  17632.41040
gdpPercap_1987  21888.88903  19007.19129
gdpPercap_1992  23424.76683  18363.32494
gdpPercap_1997  26997.93657  21050.41377
gdpPercap_2002  30687.75473  23189.80135
gdpPercap_2007  34435.36744  25185.00911
```

## Accessing data in a dataframe

The next question on our minds should be; "now that we've loaded our data into Python, how do we select or access its values"?
DataFrames provide each row and column in our table of data with a *label*.
 - We saw that we can use the `index_col` parameter in `read_csv` to specify the row labels.
 - We also saw that, if we didn't provide `index_col` as a parameter, Pandas automatically assigned our rows labels that started at `0` and increased by `1`.

Specifying a row and column uniquely identifies an *entry* in the dataframe.
To retrieve value of the entry at a location, we can use the `DataFrame.loc` method:

```python
# Load the data for Europe so that we have a larger dataset to work with
data = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country')

print(data.loc['Albania', 'gdpPercap_1952'])
```

```output
1601.056136
```

However, underneath the labels for the rows and columns, each entry also has an *index* `[i, j]`.
- Indices are listed by `[row_number, column_number]`.
- Indices start at `0` and increase by `1` as we move along the rows and columns.
- Indices start at `0` because it represents an offset from the "first" entry in the dataframe, which is the entry at the intersection of the first row and first column.
- We saw that if we don't provide `index_col` to `read_csv`, Pandas sets the row labels to match the row indices.

Our `data` dataframe is effectively storing our entries as a grid, and keeps track of which labels correspond to which index.
This lets us interact with our data in a friendly and human-readable way, as it is much easier to work with labels than indices when handling tabular data!
![](fig/python-zero-index.svg){alt="."}

We can also access entries by providing their index to the `DataFrame.iloc[]` method, rather than their row and column labels.
- Since `'Albania'` is our first row, and `'gdpPercap_1952'` our first column, we can also get the `['Albania', 'gdpPercap_1952']` entry by using `iloc[0,0]`.
- Since `'Italy'` is the 16th row, and `'gdpPercap_1977'` is the 6th column, we can get the `['Italy', 'gdpPercap_1977']` entry by using `iloc[15,5]`.

```python
# Albania is 0 rows away from the first row (Albania)
# gdpPercap_1952 is 0 columns away from the first column (gdpPercap_1952)
print(data.iloc[0,0])
# Italy is 15 rows away from the first row (Albania)
# gdpPercap_1977 is 5 columns away from the first column (gdpPercap_1952)
print(data.iloc[15,5])
```

```output
1601.056136
14255.98475
```

## Selection using slices

We have seen that `loc` and `iloc` allow us to select individual entries in our dataframe.
However, they can also be used to select a range of rows and columns whose entries we want to retrieve.
- A range of indices (or labels) that we want to select is called a *slice*.
- Slices are writing using a semicolon `:`.

For example, let's say we wanted all the entries from `1957` through to `1987` for all the countries beginning with "B" (`'Belgium'` through to `'Bulgaria'`).
We could access these entries via a slice:

```python
# Slice using labels. Notice that, because a slice doesn't include the end value, we have to provide the label of the first column we don't want to include as the end value of our slice.
print(data.loc['Belgium':'Bulgaria', 'gdpPercap_1957':'gdpPercap_1987'])
```

```output
                        gdpPercap_1957  gdpPercap_1962  gdpPercap_1967  \
country                                                                  
Belgium                    9714.960623    10991.206760    13149.041190   
Bosnia and Herzegovina     1353.989176     1709.683679     2172.352423   
Bulgaria                   3008.670727     4254.337839     5577.002800   
Croatia                    4338.231617     5477.890018     6960.297861   

                        gdpPercap_1972  gdpPercap_1977  gdpPercap_1982  \
country                                                                  
Belgium                   16672.143560    19117.974480    20979.845890   
Bosnia and Herzegovina     2860.169750     3528.481305     4126.613157   
Bulgaria                   6597.494398     7612.240438     8224.191647   
Croatia                    9164.090127    11305.385170    13221.821840   

                        gdpPercap_1987  gdpPercap_1992  
country                                                 
Belgium                   22525.563080    25575.570690  
Bosnia and Herzegovina     4314.114757     2546.781445  
Bulgaria                   8239.854824     6302.623438  
Croatia                   13822.583940     8447.794873  
```

- Leaving out the `start` label will be taken to mean "start from the beginning".
- Leaving out the `end` label will be taken to mean "go until the end of the dataframe".
- Putting only a semicolon can be used to mean "all the entries".

```python
# Fetch the entries in rows up to and including Belgium
print(data.loc[:'Belgium', :])
# Fetch the entries in columns from 1987 onwards
print(data.loc[:, 'gdpPercap_1987':])
# Fetch all the entries for 'Albania'
data.loc['Albania', :]
# Fetch the data from 1987 for all countries
data.loc[:, 'gdpPercap_1987']
```

:::::::::::::::::::::::::::::::::::::::::: callout

If you want to fetch all of the columns, you don't have to include the second slice when using `loc`.
For example, the following two calls will give back the same entries:
```python
data.loc['Albania']
data.loc['Albania', :]
```

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Extent of Slicing

1. Do the two statements below produce the same output?
2. Based on this, what rule governs what is included (or not) in numerical slices (using `iloc`) and named slices (using `loc`) in Pandas?

```python
print(data.iloc[0:2, 0:2])
print(data.loc['Albania':'Belgium', 'gdpPercap_1952':'gdpPercap_1962'])
```

:::::::::::::::  solution

## Solution

No, they do not produce the same output! The output of the first statement is:

```output
        gdpPercap_1952  gdpPercap_1957
country                                
Albania     1601.056136     1942.284244
Austria     6137.076492     8842.598030
```

The second statement gives:

```output
        gdpPercap_1952  gdpPercap_1957  gdpPercap_1962
country                                                
Albania     1601.056136     1942.284244     2312.888958
Austria     6137.076492     8842.598030    10750.721110
Belgium     8343.105127     9714.960623    10991.206760
```

Clearly, the second statement produces an additional column and an additional row compared to the first statement.  
What conclusion can we draw? 
We see that a numerical slice (slicing indices), `0:2`, *omits* the final index (i.e. index 2) in the range provided, while a named slice, `'gdpPercap_1952':'gdpPercap_1962'`, *includes* the final element.

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Reading Other Data

Read the data in `gapminder_gdp_americas.csv` (which should be in the same directory as `gapminder_gdp_oceania.csv`) into a variable called `data_americas`.

Determine how many rows and columns this data has.
Hint: try printing out the value of the `.shape` member variable once you load your dataframe!

:::::::::::::::  solution

## Solution

To read in a CSV, we use `pd.read_csv` and pass the filename `'data/gapminder_gdp_americas.csv'` to it.
We also once again pass the column name `'country'` to the parameter `index_col` in order to index by country.

To determine how many rows and columns this dataframe has, we could use `info` like we did before:
```python
data_americas = pd.read_csv('data/gapminder_gdp_americas.csv', index_col='country')
data_americas.info()
```

```output
<class 'pandas.core.frame.DataFrame'>
Index: 25 entries, Argentina to Venezuela
Data columns (total 13 columns):
 #   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   continent       25 non-null     object 
 1   gdpPercap_1952  25 non-null     float64
 2   gdpPercap_1957  25 non-null     float64
 3   gdpPercap_1962  25 non-null     float64
 4   gdpPercap_1967  25 non-null     float64
 5   gdpPercap_1972  25 non-null     float64
 6   gdpPercap_1977  25 non-null     float64
 7   gdpPercap_1982  25 non-null     float64
 8   gdpPercap_1987  25 non-null     float64
 9   gdpPercap_1992  25 non-null     float64
 10  gdpPercap_1997  25 non-null     float64
 11  gdpPercap_2002  25 non-null     float64
 12  gdpPercap_2007  25 non-null     float64
dtypes: float64(12), object(1)
memory usage: 2.7+ KB
```

We can see that we have 25 entries (rows), and 13 columns.
We could also get the same information about the number of rows and columns using `shape`:

```python
print(data_americas.shape)
```

```output
(25, 13)
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Inspecting Data

After reading the data for the Americas,
use `help(data_americas.head)` and `help(data_americas.tail)`
to find out what `DataFrame.head` and `DataFrame.tail` do.

1. What method call will display the first three rows of this data?
2. What method call will display the last three columns of this data?
  (Hint: you may need to change your view of the data.)

:::::::::::::::  solution

## Solution

1. We can check out the first five rows of `data_americas` by executing `data_americas.head()`
  which lets us view the beginning of the dataframe. We can specify the number of rows we wish
  to see by specifying the parameter `n` in our call to `data_americas.head()`.
  To view the first three rows, execute:
  
  ```python
  data_americas.head(n=3)
  ```
  
  ```output
            continent  gdpPercap_1952  gdpPercap_1957  gdpPercap_1962  \
  country
  Argentina  Americas     5911.315053     6856.856212     7133.166023
  Bolivia    Americas     2677.326347     2127.686326     2180.972546
  Brazil     Americas     2108.944355     2487.365989     3336.585802
  
            gdpPercap_1967  gdpPercap_1972  gdpPercap_1977  gdpPercap_1982  \
  country
  Argentina     8052.953021     9443.038526    10079.026740     8997.897412
  Bolivia       2586.886053     2980.331339     3548.097832     3156.510452
  Brazil        3429.864357     4985.711467     6660.118654     7030.835878
  
             gdpPercap_1987  gdpPercap_1992  gdpPercap_1997  gdpPercap_2002  \
  country
  Argentina     9139.671389     9308.418710    10967.281950     8797.640716
  Bolivia       2753.691490     2961.699694     3326.143191     3413.262690
  Brazil        7807.095818     6950.283021     7957.980824     8131.212843
  
             gdpPercap_2007
  country
  Argentina    12779.379640
  Bolivia       3822.137084
  Brazil        9065.800825
  ```

2. To check out the last three rows of `data_americas`, we would use the command,
  `americas.tail(n=3)`, analogous to `head()` used above. However, here we want to look at
  the last three columns so we need to change our view and then use `tail()`. To do so, we
  create a new dataframe in which rows and columns are switched:
  
  ```python
  americas_flipped = data_americas.T
  ```
  
  We can then view the last three columns of `americas` by viewing the last three rows
  of `americas_flipped`:
  
  ```python
  americas_flipped.tail(n=3)
  ```
  
  ```output
  country        Argentina  Bolivia   Brazil   Canada    Chile Colombia  \
  gdpPercap_1997   10967.3  3326.14  7957.98  28954.9  10118.1  6117.36
  gdpPercap_2002   8797.64  3413.26  8131.21    33329  10778.8  5755.26
  gdpPercap_2007   12779.4  3822.14   9065.8  36319.2  13171.6  7006.58
  
  country        Costa Rica     Cuba Dominican Republic  Ecuador    ...     \
  gdpPercap_1997    6677.05  5431.99             3614.1  7429.46    ...
  gdpPercap_2002    7723.45  6340.65            4563.81  5773.04    ...
  gdpPercap_2007    9645.06   8948.1            6025.37  6873.26    ...
  
  country          Mexico Nicaragua   Panama Paraguay     Peru Puerto Rico  \
  gdpPercap_1997   9767.3   2253.02  7113.69   4247.4  5838.35     16999.4
  gdpPercap_2002  10742.4   2474.55  7356.03  3783.67  5909.02     18855.6
  gdpPercap_2007  11977.6   2749.32  9809.19  4172.84  7408.91     19328.7
  
  country        Trinidad and Tobago United States  Uruguay Venezuela
  gdpPercap_1997             8792.57       35767.4  9230.24   10165.5
  gdpPercap_2002             11460.6       39097.1     7727   8605.05
  gdpPercap_2007             18008.5       42951.7  10611.5   11415.8
  ```
  
  This shows the data that we want, but we may prefer to display three columns instead of three rows,
  so we can flip it back:
  
  ```python
  americas_flipped.tail(n=3).T    
  ```
  
  **Note:** we could have done the above in a single line of code by 'chaining' the commands:
  
  ```python
  data_americas.T.tail(n=3).T
  ```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- Use the `pandas` library to work with tabular data in Python.
- Use the `read_csv` function to load data into a dataframe variable.
- Use `index_col` to specify that a column's values should be used as row headings.
- Use `info` to find out basic information about a dataframe.
- Use slices and `loc` to extract entries from a dataframe.

::::::::::::::::::::::::::::::::::::::::::::::::::
