---
title: Visualizing Tabular Data
teaching: 40
exercises: 20
---

::::::::::::::::::::::::::::::::::::::: objectives

- Plot simple graphs from data.
- Plot multiple graphs in a single figure.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How can I visualize tabular data in Python?
- How can I group several plots together?

::::::::::::::::::::::::::::::::::::::::::::::::::

## Visualizing data

The mathematician Richard Hamming once said, "The purpose of computing is insight, not numbers," and the best way to develop insight is often to visualize data.  Visualization deserves an entire lecture of its own, but we can explore a few features of Python's `matplotlib` library here. 
While there is no official plotting library, `matplotlib` is the *de facto* standard.

::::::::::::::::::::::::::::::::::::::::::  prereq

## Episode Prerequisites

Before we can start plotting, we need to load the data from one of our files to use as an example.
Start a new notebook and import the GDP data for Europe into a dataframe called `data_eu`.

```python
import pandas as pd

data_eu = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
```

::::::::::::::::::::::::::::::::::::::::::::::::::

Countries are grouped into files by continent.
Each country has its Gross Domestic Product (GDP) per capita (population) recorded in 5 year intervals from 1952 to 2007.

Dataframes have a `plot()` method which we can use to produce a line-plot of the data contained within the frame.

```python
data_eu.plot()
```

![](fig/03-data_eu_plot.svg){alt='A line graph showing the GDP of each country in Europe between 1952 and 2007. Unhelpfully, the dependant variable has been assumed to be the column headers, rather than the rows.'}

This has placed all of our data into a single plot that Python has then displayed to us - clearly, there is far too much here for us to take in!
You might notice that Pandas has assumed we want to use the row labels as the dependant variable for our plot, and the column headers as the line-labels.
In our case however, we want to display the GDP per capital over time, using one line for each country.
We can fix these problems by combining two of the methods we saw in the previous episode;
- We can transpose our dataframe to reverse the roles of our rows and columns, so `plot` uses the columns as the dependant variable and the rows as the line labels.
- We can use an (index) slice to take only the first 5 countries, for example.

```python
# Take only the first 5 countries (rows)
first_five_countries = data_eu.iloc[0:5, :]
# Transpose the data, then plot if afterwards
first_five_countries.T.plot()
```

![](fig/03-data_eu_T_plot.svg){alt='A line graph showing the GDP per capita of 5 European countries, from 1952 through to 2007.'}

## Computing statistics across dataframe axes

Let's begin our analysis of the data by plotting the average GDP across Europe, as a function of time.
Pandas dataframes have a built-in function, `mean()` that we can use to help us here:

```python
print(data_eu.mean())
```

```output
1952     5661.057435
1957     6963.012816
1962     8365.486814
1967    10143.823757
1972    12479.575246
1977    14283.979110
1982    15617.896551
1987    17214.310727
1992    17061.568084
1997    19076.781802
2002    21711.732422
2007    25054.481636
dtype: float64
```

You'll notice that Pandas has assumed (again) that we want to get the mean for each year, or to "take the mean GDP down the columns".
However it may also be useful to know the average GDP for each country - in which case we want to take the average "along the rows" instead.
- We could use the transpose method to reverse the roles of our rows and columns like we did before, and *then* take the average:
- Alternatively, `mean()` (and many other dataframe functions) take an optional parameter called `axis` which lets us specify which axis of the dataframe (rows or columns) to take the average along.

Using the `axis` keyword, we can retrieve the average GDP for each country by taking the average value *across the columns*:

```python
# axis=columns means "take the average across the column values"
# That is, compute the average of each row (country)
data_eu.mean(axis='columns')
```

```output
country
Albania                    3255.366633
Austria                   20411.916279
Belgium                   19900.758072
Bosnia and Herzegovina     3484.779069
Bulgaria                   6384.055172
Croatia                    9331.712346
Czech Republic            13920.011379
Denmark                   21671.824888
Finland                   17473.722667
France                    18833.570327
Germany                   20556.684433
Greece                    13969.036833
Hungary                   10888.175654
Iceland                   20531.422273
Ireland                   15758.606238
Italy                     16245.209006
Montenegro                 7208.064560
Netherlands               21748.852208
Norway                    26747.306554
Poland                     8416.553912
Portugal                  11354.091927
Romania                    7300.169974
Serbia                     9305.049444
Slovak Republic           10415.530689
Slovenia                  14074.582109
Spain                     14029.826479
Sweden                    19943.126104
Switzerland               27074.334405
Turkey                     4469.453380
United Kingdom            19380.472986
dtype: float64
```
![](fif/../fig/03-axis-operations.svg){alt='Diagram illustrating how the axis keyword changes the axis along which the mean() function operates.'}

## Plotting statistics

The `plot` method called directly from our dataframe is implicitly using `matplotlib`'s `pyplot.plot` function.
Whilst calling `plot` directly from a dataset can be helpful to get a quick visual glimpse of the data, most of the time we will want to manipulate our data in some way and plot some significant statistics or derived values, rather than the raw data itself.
We will use the `matplotlib` library to manage and create plots ourselves from here on.
As with any library, we must first tell Python to import it:

```python
import matplotlib.pyplot as plt
```

We can now create a plot of the average GDP of European countries in the following way:

```python
# Create a figure or window for plotting
fig = plt.figure()
# Extract the mean GDP each year
mean_gdp_each_year = data_eu.mean(axis='rows')
# Plot the data in the figure window
plt.plot(mean_gdp_each_year)
# Show the figure to the screen
plt.show()
```

![](fig/03-eu_mean_gdp_no_labels.svg){alt='A line graph showing the change in the average GDP of European countries.'})

Let's break down what each line is doing.
```python
fig = plt.figure()
```
- Uses the `figure` function from the `matplotlib.pyplot` library. 
- This tells Python to create a new, blank figure window.
- The variable `fig` cna be used to access this figure window.

```python
mean_gdp_each_year = data_eu.mean(axis='rows')
```
- Takes the average value of our `data_eu` dataframe across the rows (down the columns).
- Places the result into the variable `mean_gdp_each_year`.

```python
plt.plot(mean_gdp_each_year)
```
- Uses the `plot` function from the `matplotlib.pyplot` library.
- This places the data stored in `mean_gdp_each_year` and plots it to the figure window.
- If we had multiple figures open, we could specify which one to plot this data on. But since we only have one (`fig`), `plt.plot` knows to plot the data onto this one.

## Grouping Plots

So far, `matplotlib`'s plot hasn't done much more than dataframe's `plot` function did - but that changes now.
It is often the case where we will want to display multiple statistics side-by-side, or the same statistic from multiple datasets simultaneously for comparison purposes.
This can be achieved by adding *subplots* to a figure, using the `add_subplots` function.
Let's demonstrate how to do this by plotting the maximum and minimum GDP of countries in Europe for each year alongside the average GDP for that year.

```python
# Compute the min, max, and average GDP each year for European countries
eu_min_data = data_eu.min(axis='rows')
eu_max_data = data_eu.max(axis='rows')
eu_avg_data = data_eu.mean(axis='rows')

# Create a new figure to draw the plots onto
fig = plt.figure(figsize=(25., 6.))

# Create a new axis, or plotting window
# (1, 3, 1) indicates that we want to place this plot in a 1-by-3 grid;
# and place this subplot in the first position
axes_1 = fig.add_subplot(1, 3, 1)
# Plot the minimum GDP on this axis
axes_1.plot(eu_min_data)

# Create another new axis
# (1, 3, 2) indicating that we want to use the same 1-by-3 grid;
# and place this subplot in the second position
axes_2 = fig.add_subplot(1, 3, 2)
# Plot the maximum GDP on this axis
axes_2.plot(eu_max_data)

# Create another new axis
# This axis will be in the third position of our 1-by-3 grid
axes_3 = fig.add_subplot(1, 3, 3)
# Plot the average GDP on this axis
axes_3.plot(eu_avg_data)

# Display the figure.
plt.show()
```

![](fig/03-min_max_avg_no_labels.svg){alt='A figure which contains three subplots, side-by-side'}

::::::::::::::::::::::::::::::::::::::::::::::: callout

## `min` and `max` methods

The `min` and `max` functions can be used on a dataframe in the same way as the `mean` function, and take the same `axis` parameter.
For us to retrieve the minimum GDP of countries in Europe for each year, we can use

```python
data_eu.min(axis='rows')
```

```output
1952     973.533195
1957    1353.989176
1962    1709.683679
1967    2172.352423
1972    2860.169750
1977    3528.481305
1982    3630.880722
1987    3738.932735
1992    2497.437901
1997    3193.054604
2002    4604.211737
2007    5937.029526
dtype: float64
```

for example.

:::::::::::::::::::::::::::::::::::::::::::::::::::::::

There are a lot of new functions coming in here, so let's again break down what each one is doing.

```python
fig = plt.figure(figsize=(25., 6.))
```

- Creates a new figure, like we saw before.
- The `figsize` parameter lets us specify the size of the figure, rather than letting `matplotlib` decide this automatically for us.

```python
axes_1 = fig.add_subplot(1, 3, 1)
```

- This calls the `add_subplot` method on the figure that is stored in the `fig` variable.
- `add_subplot` takes 3 arguments; the first denotes how many total rows fo subplots there are (to be) in our figure, the second how many total columns, and the final parameter denotes which of these subplots that we want to reference (left-to-right, top-to-bottom). In this case, `1` refers to the leftmost subplot.
- The subplot is saved to the `axes_1` variable so we can refer to it later.

```python
axes_1.plot(eu_min_data)
```

- `plot` tells `matplotlib` to draw data onto a subplot window.
- In this case, we draw the data stored in `eu_min_data`, the minimum GDP for each year.
- The `axes_1` dot notation is needed so that Python knows we want to place this data on the `axes_1` subplot.

## Adding labels

Just because we have plotted some statistics doesn't mean our plot is complete!
- There are no axis labels telling us what each subplot is showing us.
- There's no title for the plot.
- There's a lot of whitespace (empty space) surrounding our plot, and between our subplots.

We can fix these using some more ``matplotlib` functions.
- The `set_ylabel` method lets us add a label for the y-axis of any plot or subplot, using dot notation.
- The `set_title` method lets us add a title to a subplot.
- The `suptitle` method lets us add a title to the figure window ("super"-title).
- The `tight_layout` method tells `matplotlib` to remove as much whitespace as possible from our figure.

```python
# Compute the min, max, and average GDP each year for European countries
eu_min_data = data_eu.min(axis='rows')
eu_max_data = data_eu.max(axis='rows')
eu_avg_data = data_eu.mean(axis='rows')

# Create a new figure to draw the plots onto
fig = plt.figure(figsize=(25., 6.))

# Create a new axis, or plotting window
# (1, 3, 1) indicates that we want to place this plot in a 1-by-3 grid;
# and place this subplot in the first position
axes_1 = fig.add_subplot(1, 3, 1)
# Plot the minimum GDP on this axis
axes_1.plot(eu_min_data)
# Add a label to the y-axis of the subplot that axes_1 refers to
axes_1.set_ylabel('GDP/capita')
# Add a title to the subplot that axes_1 refers to
axes_1.set_title('Min')

# Create another new axis
# (1, 3, 1) indicating that we want to use the same 1-by-3 grid;
# and place this subplot in the second position
axes_2 = fig.add_subplot(1, 3, 2)
# Plot the maximum GDP on this axis
axes_2.plot(eu_max_data)
# Add a label to the y-axis of the subplot
axes_2.set_ylabel('GDP/capita')
# Add a title to the subplot
axes_1.set_title('Max')

# Create another new axis
# This axis will be in the third position of our 1-by-3 grid
axes_3 = fig.add_subplot(1, 3, 3)
# Plot the average GDP on this axis
axes_3.plot(eu_avg_data)
# Add a label to the y-axis of the subplot
axes_3.set_ylabel('GDP/capita')
# Add a title to the subplot
axes_1.set_title('Average')

# Add a main title to the figure that fig refers to
fig.suptitle('GDP/capita statistics for European countries')
# Trim away as much empty space from the figure as possible
fig.tight_layout()

# Display the figure.
plt.show()
```

![](fig/03-min_max_avg_with_labels.svg){alt='A figure with 3 subplots, each labelled with the statistic that they display.'}

::::::::::::::::::::::::::::::::::::::::::::: challenge

## Setting limits for the axes

You might have noticed that our subplots leave a little bit of space between our line and the edges of the subplot itself, which is a result of the range of the y-axis being slightly bigger than the maximum and minimum range of the data we are plotting.

Can you figure out a way to manually set the range of the y-axis, to remove this white space?

Hint:
- Try using the `set_ylim(min_value, max_value)` method on the subplots.
- Try using the `max()` and `min()` methods on the `eu_min_data` variables.

:::::::::::::::: solution

To fix this for the first subplot, for example, we can use

```python
# Create a new axis, or plotting window
# (1, 3, 1) indicates that we want to place this plot in a 1-by-3 grid;
# and place this subplot in the first position
axes_1 = fig.add_subplot(1, 3, 1)
# Plot the minimum GDP on this axis
axes_1.plot(eu_min_data)
# Add a label to the y-axis of the subplot that axes_1 refers to
axes_1.set_ylabel('GDP/capita')
# Add a title to the subplot that axes_1 refers to
axes_1.set_title('Min')
# Set the y-limits to be the max and min values of the data that we are plotting
y_axes_min_value = eu_min_data.min()
y_axes_max_value = eu_max_data.max()
axes_1.set_ylim(y_axes_min_value, y_axes_max_value)
```

If you want to be really fancy, you can even use

```python
axes_1.set_ylim(eu_min_data.min(), eu_min_data.max())
```

instead of the last three lines!

:::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::  challenge

## Drawstyles

The `plot` method doesn't just draw straight, blue lines - it can be customised with some optional parameters.

Modify your calls to `plot` with different parameters to create different line styles in each of the three subplots.
Some useful parameters to add to `plot` are:
- `linestyle = ':'`. Can also be tried with `'--'`, `'-.'`, and a few other options.
- `color = 'red'`. Several other colours are also available!
- `marker = 'x'`. There are [lots of these](https://matplotlib.org/stable/api/markers_api.html) to try out.

:::::::::::::::  solution

## Solution

There are a ton of options to pick from here, but an example that draws a dashed, red line with crosses marking the datapoints is below:

```python
axes_1.plot(numpy.mean(data, axis=0), linestyle=':', color='red', marker='x')
```

:::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::  challenge

## Make Your Own Plot

Create a plot showing the standard deviation of the GDP/captia for each year.

Hint:
- Try using the `std` method on `data_eu`.

:::::::::::::::  solution

## Solution

```python
# Create a new figure window for the plot
std_plot = plt.figure()

# Compute the standard deviation down the columns
std_data = data_eu.std(axis='rows')

plt.plot(std_data)
plt.show()
```

:::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::: challenge

## Moving Plots Around

Modify the program to display the three plots on top of one another instead of side by side.

:::::::::::::::  solution

## Solution

```python
eu_min_data = data_eu.min(axis='rows')
eu_max_data = data_eu.max(axis='rows')
eu_avg_data = data_eu.mean(axis='rows')

fig = plt.figure(figsize=(25., 6.))

# Create a new axis, or plotting window
# (3, 1, 1) indicates that we want to place this plot in a 3-by-1 grid;
# and place this subplot in the first position
axes_1 = fig.add_subplot(3, 1, 1)
axes_1.plot(eu_min_data)
axes_1.set_ylabel('GDP/capita')
axes_1.set_title('Min')

# Create another new axis
# (3, 1, 2) indicating that we want to use the same 3-by-1 grid;
# and place this subplot in the second position
axes_2 = fig.add_subplot(3, 1, 2)
axes_2.plot(eu_max_data)
axes_2.set_ylabel('GDP/capita')
axes_1.set_title('Max')

axes_3 = fig.add_subplot(3, 1, 3)
axes_3.plot(eu_avg_data)
axes_3.set_ylabel('GDP/capita')
axes_1.set_title('Average')

fig.suptitle('GDP/capita statistics for European countries')
fig.tight_layout()

plt.show()
```

:::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::: keypoints

- Use the `pyplot` module from the `matplotlib` library to create visualizations of data.
- Dataframes have methods like `min`, `max`, and `mean` to compute statistics along either the rows or the columns.
- We can use `add_subplot` to create multiple plots in a single figure.
- We can customise the labels, axis ranges, line styles, and more of our plots using `matplotlib`.

:::::::::::::::::::::::::::::::::::::::::::::::::::::::
