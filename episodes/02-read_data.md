---
title: Reading Tabular Data into DataFrames
teaching: 40
exercises: 20
---

::::::::::::::::::::::::::::::::::::::: objectives

- Import the Pandas library.
- Use Pandas to load a CSV data set.
- Retrieve some basic information about a Pandas DataFrame.

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
- Then, we can use the `read_csv` function from Pandas to read one of our data files into a DataFrame. This function takes the name of a file as an argument, and returns a DataFrame that we can assign to a variable.

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
- The columns in a DataFrame are the observed variables, and the rows are the observations.
- Pandas uses backslash `\` to show wrapped lines when output is too wide to fit the screen.
- Using descriptive DataFrame names helps us distinguish between multiple DataFrames so we won't accidentally overwrite a DataFrame or read from the wrong one.

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

You might notice that our `data_oceania` DataFrame is displaying the row headings as numbers - in this case `0` and `1`.
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

Now when we print out our DataFrame we can see that the rows are identified by country, rather than by a number.

## Working with DataFrames

We know that the `data_oceania` variable contains a DataFrame, but how do we actually know *what's in* this DataFrame?
Or how many rows it has?
Or the *type of* data stored in the columns?

To obtain an overview of our DataFrame, we can use the `info()` method.

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

This output is telling us that the `data_oceania` DataFrame:
- Has two rows (entries), the first being `'Australia'` and the last being `'New Zealand'`.
- Has twelve columns per row.
  - Each row has 2 non-null values. Null values are used to represent missing data or observations.
  - All of the columns have data whose type is `float64` - that is, a floating point number like we saw in the previous lesson.
- The only variable (or datatype, `dtype`) used is `float64`, and it is used in 12 columns (that is, all of them).
- Is using 208 bytes of memory.

Whilst the `info()` method tells us how many columns our DataFrame has, it doesn't tell us what the headers *are*.
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
To do so, we can *transpose* our DataFrame:
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

:::::::::::::::::::::::::::::::::::::::  challenge

## Reading Other Data

Read the data in `gapminder_gdp_americas.csv`
(which should be in the same directory as `gapminder_gdp_oceania.csv`)
into a variable called `data_americas`
and display its summary statistics.

:::::::::::::::  solution

## Solution

To read in a CSV, we use `pd.read_csv` and pass the filename `'data/gapminder_gdp_americas.csv'` to it.
We also once again pass the column name `'country'` to the parameter `index_col` in order to index by country.
The summary statistics can be displayed with the `DataFrame.describe()` method.

```python
data_americas = pd.read_csv('data/gapminder_gdp_americas.csv', index_col='country')
data_americas.describe()
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
  which lets us view the beginning of the DataFrame. We can specify the number of rows we wish
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
  create a new DataFrame in which rows and columns are switched:
  
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

## Writing Data

As well as the `read_csv` function for reading data from a file, Pandas provides a `to_csv` function to write dataframes to files.
- `to_csv` takes the name of the file you want to save your DataFrame to as it's argument.
- You can use `help` to get more information on how to use `to_csv`:
```python
help(data_oceania.to_csv)
```

Applying what you've learned about reading from files, write the `data_oceania` DataFrame to a file called `processed.csv`.

:::::::::::::::  solution

## Solution

In order to write the DataFrame `data_oceania` to a file called `processed.csv`, execute the following command:

```python
data_americas.to_csv('processed.csv')
```

Note that `help(to_csv)` or `help(pd.to_csv)` throws an error! 
This is due to the fact that `to_csv` is not a global Pandas function, but a *member function* of DataFrames. 
This means you can only call it using the dot notation on a DataFrame variable.

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- Use the Pandas library to get basic statistics out of tabular data.
- Use `index_col` to specify that a column's values should be used as row headings.
- Use `DataFrame.info` to find out more about a dataframe.
- The `DataFrame.columns` variable stores information about the dataframe's columns.
- Use `DataFrame.T` to transpose a dataframe.

::::::::::::::::::::::::::::::::::::::::::::::::::