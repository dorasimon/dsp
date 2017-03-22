# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are both a sequence of values, and the elements don't have to be the same type but are usually of the same type. Lists are mutable but tuples are immutable.  
Only tuples can work as keys, because keys must be immutable, because the hash table implementation of dictionaries uses a hash value calculated from the key value to find the key; if the key were a mutable object, its value could change, and thus its hash could also change.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists are ordered collection of elements; sets are unordered collection of unique elements.  
List: ["a", "b", "c", "b", "a"], Set: {"c", "a", "b"}  
Both list and set support membership test: print("element" in set/list), which returns True if the element is a member, False if the element is not a member; or print("element" not in set/list), which returns True if the element is not a member, True is the element is a member.  
Lists are ordered so elements can be indexed, like: print list.index("element"), which returns the index of the element in the list; or print(list[n]), which returns the element of index n. However, sets are unordered, meaning sets don't record element position or order of insertion, so elements can't be accessed with indices.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python supports the creation of anonymous functions (i.e. functions that are not bound to a name) at runtime, using a construct called "lambda". Lambda is often used in conjunction with typical functional concepts like filter(), map() and reduce().  

Examples:  
squares = [x ** 2 for x in range(1, 11)]  
print(list(filter(lambda x: x >= 30 and x <= 70, squares)))  

cubes = [x ** 3 for x in range(1, 11)]  
print(list(filter(lambda x: x % 3 == 0, cubes)))  

students = [("John", "A", 15), ("Jane", "B", 14), ("Dave", "C", 13)]  
print(sorted(students, lambda student: student[2]))

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.  

Examples:  
The filter() function takes in a function and a list as arguments. The function is called with all the items in the list and a new list is returned which contains items for which the function evaluates to True.  
my_list = [1, 5, 4, 6, 8, 11, 3, 12]  
print(list(filter(lambda x: x % 2 == 0, my_list)))  

The map() function takes in a function and a list. The function is called with all the items in the list and a new list is returned which contains items returned by that function for each item.  
my_list = [1, 5, 4, 6, 8, 11, 3, 12]  
print(list(map(lambda x: x * 2, my_list)))  

Set comprehension: {expression for element in sequence}  
{n ** 2 for n in range(10)} or set(n ** 2 for n in range(10))  

Dictionary comprehension: {key: value for (key, value) in iterable}  
{x: x ** 3 for x i range(10)}
{x: x ** 3 for x in range(10) if x ** 3 % 4 == 0}

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





