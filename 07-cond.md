---
title: Making Choices
teaching: 30
exercises: 0
---

::::::::::::::::::::::::::::::::::::::: objectives

- Write conditional statements including `if`, `elif`, and `else` branches.
- Correctly evaluate expressions containing `and` and `or`.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How can my programs do different things based on data values?

::::::::::::::::::::::::::::::::::::::::::::::::::

In our last lesson, we discovered something suspicious was going on
in our GDP data by drawing some plots.
How can we use Python to automatically recognize the different features we saw,
and take a different action for each? In this lesson, we'll learn how to write code that
runs only when certain conditions are true.

## Conditionals

We can ask Python to take different actions, depending on a condition, with an `if` statement:

```python
num = 37
if num > 100:
    print('greater')
else:
    print('not greater')
print('done')
```

```output
not greater
done
```

The second line of this code uses the keyword `if` to tell Python that we want to make a choice.
If the test that follows the `if` statement is true,
the body of the `if`
(i.e., the set of lines indented underneath it) is executed, and "greater" is printed.
If the test is false,
the body of the `else` is executed instead, and "not greater" is printed.
Only one or the other is ever executed before continuing on with program execution to print "done":

![](fig/python-flowchart-conditional.png){alt='A flowchart diagram of the if-else construct that tests if variable num is greater than 100'}

Conditional statements don't have to include an `else`.
If there isn't one,
Python simply does nothing if the test is false:

```python
num = 53
print('before conditional...')
if num > 100:
    print(num, 'is greater than 100')
print('...after conditional')
```

```output
before conditional...
...after conditional
```

We can also chain several tests together using `elif`,
which is short for "else if".
The following Python code uses `elif` to print the sign of a number.

```python
num = -3

if num > 0:
    print(num, 'is positive')
elif num == 0:
    print(num, 'is zero')
else:
    print(num, 'is negative')
```

```output
-3 is negative
```

Note that to test for equality we use a double equals sign `==`
rather than a single equals sign `=` which is used to assign values.

:::::::::::::::::::::::::::::::::::::::::  callout

## Comparing in Python

Along with the `>` and `==` operators we have already used for comparing values in our
conditionals, there are a few more options to know about:

- `>`: greater than
- `<`: less than
- `==`: equal to
- `!=`: does not equal
- `>=`: greater than or equal to
- `<=`: less than or equal to
  

::::::::::::::::::::::::::::::::::::::::::::::::::

We can also combine tests using `and` and `or`.
`and` is only true if both parts are true:

```python
if (1 > 0) and (-1 >= 0):
    print('both parts are true')
else:
    print('at least one part is false')
```

```output
at least one part is false
```

while `or` is true if at least one part is true:

```python
if (1 < 0) or (1 >= 0):
    print('at least one test is true')
```

```output
at least one test is true
```

:::::::::::::::::::::::::::::::::::::::::  callout

## `True` and `False`

`True` and `False` are special words in Python called `booleans`,
which represent truth values. A statement such as `1 < 0` returns
the value `False`, while `-1 < 0` returns the value `True`.


::::::::::::::::::::::::::::::::::::::::::::::::::

## Checking our Data

Now that we've seen how conditionals work,
we can use them to check for the suspicious features we saw in our inflammation data.
We are about to use functions provided by the `pandas` module again.
Therefore, if you're working in a new Python session, make sure to load the
module with:

```python
import pandas as pd
```

From the first set of plots, we saw that the minimum and average exhibit
a strange behavior for some of our dataset.
Wouldn't it be a good idea to detect such behavior and report it as suspicious?
Let's do that!
However, instead of checking every entry manually, let's check if the minimum and the maximum for the minimum across years is the same.

```python
min_data = data.min(axis='rows')
min_min_data = min_data.min()
max_min_data = min_data.max()

if min_min_data == 0 and max_min_data == 0:
    print('Suspicious looking minima!')
```

We also saw a different problem with America dataset;
the average across the years was constant (looks like someone had manipulated the data).
We can also check for this with an `elif` condition:

```python
elif round(data.mean(axis='rows').min()) == round(data.mean(axis='rows').max()):
    print('Average is flat!')
```

And if neither of these conditions are true, we can use `else` to give the all-clear:

```python
else:
    print('Seems OK!')
```

Let's test that out:

```python
data = pd.read_csv('data/gapminder_gdp_asia.csv', index_col='country')

min_data = data.min(axis='rows')
min_min_data = min_data.min()
max_min_data = min_data.max()

if min_min_data == 0 and max_min_data == 0:
    print('Suspicious looking minima!')
elif round(data.mean(axis='rows').min()) == round(data.mean(axis='rows').max()):
    print('Average is flat!')
else:
    print('Seems OK!')
```

```output
Suspicious looking minima!
```

```python
data = pd.read_csv('data/gapminder_gdp_americas.csv', index_col='country')

min_data = data.min(axis='rows')
min_min_data = min_data.min()
max_min_data = min_data.max()

if min_min_data == 0 and max_min_data == 0:
    print('Suspicious looking minima!')
elif round(data.mean(axis='rows').min()) == round(data.mean(axis='rows').max()):
    print('Average is flat!')
else:
    print('Seems OK!')
```

```output
Average is flat!
```

In this way, we have asked Python to do something different depending on the condition of our data.
Here we printed messages in all cases, but we could also imagine not using the `else` catch-all
so that messages are only printed when something is wrong,
freeing us from having to manually examine every plot for features we've seen before.

:::::::::::::::::::::::::::::::::::::::  challenge

## How Many Paths?

Consider this code:

```python
if 4 > 5:
    print('A')
elif 4 == 5:
    print('B')
elif 4 < 5:
    print('C')
```

Which of the following would be printed if you were to run this code?
Why did you pick this answer?

1. A
2. B
3. C
4. B and C

:::::::::::::::  solution

## Solution

C gets printed because the first two conditions, `4 > 5` and `4 == 5`, are not true,
but `4 < 5` is true.
In this case only one of these conditions can be true for at a time, but in other
scenarios multiple `elif` conditions could be met. In these scenarios only the action
associated with the first true `elif` condition will occur, starting from the top of the
conditional section.
![](fig/python-else-if.png){alt='A flowchart diagram of a conditional section with multiple elif conditions and some possible outcomes.'}
This contrasts with the case of multiple `if` statements, where every action can occur
as long as their condition is met.
![](fig/python-multi-if.png){alt='A flowchart diagram of a conditional section with multiple if statements and some possible outcomes.'}



:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## What Is Truth?

`True` and `False` booleans are not the only values in Python that are true and false.
In fact, *any* value can be used in an `if` or `elif`.
After reading and running the code below,
explain what the rule is for which values are considered true and which are considered false.

```python
if '':
    print('empty string is true')
if 'word':
    print('word is true')
if []:
    print('empty list is true')
if [1, 2, 3]:
    print('non-empty list is true')
if 0:
    print('zero is true')
if 1:
    print('one is true')
```

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## That's Not Not What I Meant

Sometimes it is useful to check whether some condition is not true.
The Boolean operator `not` can do this explicitly.
After reading and running the code below,
write some `if` statements that use `not` to test the rule
that you formulated in the previous challenge.

```python
if not '':
    print('empty string is not true')
if not 'word':
    print('word is not true')
if not not True:
    print('not not True is true')
```

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Close Enough

Write some conditions that print `True` if the variable `a` is within 10% of the variable `b`
and `False` otherwise.
Compare your implementation with your partner's:
do you get the same answer for all possible pairs of numbers?

:::::::::::::::  solution

## Hint

There is a [built-in function `abs`][abs-function] that returns the absolute value of
a number:

```python
print(abs(-12))
```

```output
12
```

:::::::::::::::::::::::::

:::::::::::::::  solution

## Solution 1

```python
a = 5
b = 5.1

if abs(a - b) <= 0.1 * abs(b):
    print('True')
else:
    print('False')
```

:::::::::::::::::::::::::

:::::::::::::::  solution

## Solution 2

```python
print(abs(a - b) <= 0.1 * abs(b))
```

This works because the Booleans `True` and `False`
have string representations which can be printed.



:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## In-Place Operators

Python (and most other languages in the C family) provides
[in-place operators](../learners/reference.md#in-place-operators)
that work like this:

```python
x = 1  # original value
x += 1 # add one to x, assigning result back to x
x *= 3 # multiply x by 3
print(x)
```

```output
6
```

Write some code that sums the positive and negative numbers in a list separately,
using in-place operators.
Do you think the result is more or less readable
than writing the same without in-place operators?

:::::::::::::::  solution

## Solution

```python
positive_sum = 0
negative_sum = 0
test_list = [3, 4, 6, 1, -1, -5, 0, 7, -8]
for num in test_list:
    if num > 0:
        positive_sum += num
    elif num == 0:
        pass
    else:
        negative_sum += num
print(positive_sum, negative_sum)
```

Here `pass` means "don't do anything".
In this particular case, it's not actually needed, since if `num == 0` neither
sum needs to change, but it illustrates the use of `elif` and `pass`.



:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Counting Vowels

1. Write a loop that counts the number of vowels in a character string.
2. Test it on a few individual words and full sentences.
3. Once you are done, compare your solution to your neighbor's.
  Did you make the same decisions about how to handle the letter 'y'
  (which some people think is a vowel, and some do not)?

:::::::::::::::  solution

## Solution

```python
vowels = 'aeiouAEIOU'
sentence = 'Mary had a little lamb.'
count = 0
for char in sentence:
    if char in vowels:
        count += 1

print('The number of vowels in this string is ' + str(count))
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::


:::::::::::::::::::::::::::::::::::::::  challenge

## Trimming Values

Fill in the blanks so that this program creates a new list
containing zeroes where the original list's values were negative
and ones where the original list's values were positive.

```python
original = [-1.5, 0.2, 0.4, 0.0, -1.3, 0.4]
result = ____
for value in original:
    if ____:
        result.append(0)
    else:
        ____
print(result)
```

```output
[0, 1, 1, 1, 0, 1]
```

:::::::::::::::  solution

## Solution

```python
original = [-1.5, 0.2, 0.4, 0.0, -1.3, 0.4]
result = []
for value in original:
    if value < 0.0:
        result.append(0)
    else:
        result.append(1)
print(result)
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Processing Small Files

Modify this program so that it only processes files with fewer than 50 records.

```python
import glob
import pandas as pd
for filename in glob.glob('data/*.csv'):
    contents = pd.read_csv(filename)
    ____:
        print(filename, len(contents))
```

:::::::::::::::  solution

## Solution

```python
import glob
import pandas as pd
for filename in glob.glob('data/*.csv'):
    contents = pd.read_csv(filename)
    if len(contents) < 50:
        print(filename, len(contents))
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Initializing

Modify this program so that it finds the largest and smallest values in the list
no matter what the range of values originally is.

```python
values = [...some test data...]
smallest, largest = None, None
for v in values:
    if ____:
        smallest, largest = v, v
    ____:
        smallest = min(____, v)
        largest = max(____, v)
print(smallest, largest)
```

What are the advantages and disadvantages of using this method
to find the range of the data?

:::::::::::::::  solution

## Solution

```python
values = [-2,1,65,78,-54,-24,100]
smallest, largest = None, None
for v in values:
    if smallest is None and largest is None:
        smallest, largest = v, v
    else:
        smallest = min(smallest, v)
        largest = max(largest, v)
print(smallest, largest)
```

If you wrote `== None` instead of `is None`, that works too, but Python programmers always
write `is None` because of the special way `None` works in the language.

It can be argued that an advantage of using this method would be to make the code more readable.
However, a disadvantage is that this code is not efficient because within each iteration of the
`for` loop statement, there are two more loops that run over two numbers each (the `min` and
`max` functions). It would be more efficient to iterate over each number just once:

```python
values = [-2,1,65,78,-54,-24,100]
smallest, largest = None, None
for v in values:
    if smallest is None or v < smallest:
        smallest = v
    if largest is None or v > largest:
        largest = v
print(smallest, largest)
```

Now we have one loop, but four comparison tests. There are two ways we could improve it further:
either use fewer comparisons in each iteration, or use two loops that each contain only one
comparison test. The simplest solution is often the best:

```python
values = [-2,1,65,78,-54,-24,100]
smallest = min(values)
largest = max(values)
print(smallest, largest)
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::


:::::::::::::::::::::::::::::::::::::::: keypoints

- Use `if condition` to start a conditional statement, `elif condition` to provide additional tests, and `else` to provide a default.
- The bodies of the branches of conditional statements must be indented.
- Use `==` to test for equality.
- `X and Y` is only true if both `X` and `Y` are true.
- `X or Y` is true if either `X` or `Y`, or both, are true.
- Zero, the empty string, and the empty list are considered false; all other numbers, strings, and lists are considered true.
- `True` and `False` represent truth values.

::::::::::::::::::::::::::::::::::::::::::::::::::


[abs-function]: https://docs.python.org/3/library/functions.html#abs
