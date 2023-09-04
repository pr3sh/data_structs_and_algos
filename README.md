
# **`Abstract`**

This repostitory aims at covering the fundamental components of Data Structure & Algorithms.

-  **Table of contents**:
  - [Introduction](#introduction)
  - [Data Structures](#data-structures)
    - [Hash Maps](#hash-maps)
    - [ Arrays](#arrays)
    - [Linked List](#linked-list)
    - [ Stacks](#stacks)
    - [ Queue](#queue)
  - [Algorithms](#algorithms)
  



### **`Introduction`**: 

Data structures and Algorithms are fundamental concepts in Computer Science, which are used for the efficient storage and manipulation of data.
Data Structures specifically, refer to the organization, storage and retrival of data, while algorithms refer to the instructions that are utilized to solve a particular problem.





### **`Data Structures`**:


#### **`Hash Maps`**:


A Hashmap is a data structure used to store information and primarily consists of two main components; a *key* and *value*. For example, an employer might have a unique **`employeeID`**, which maps to each individual in the organization as shown below.

```python
employee_mapping = {
             "1000356" : {
                        "full_name": "John Doe",
                        "postion"  : "Software Developer"
                         }      ,
             "1017890" : {
                        "full_name": "Sofia Cummings",
                        "position" : "Program Director"
                        }   
         }
```
- Generally speaking, hashmaps use two main methods to store & retrieve data; **`get()`** and **`put()`**.
- **`Time Complexity`**:
    - Insertion: *`O(1)`*
    - Deletion: *`O(1)`*
    - Lookup: *`O(1)`*

> However, in the worst-case scenario, these operations can degrade to *`O(n)`*, where n is the number of entries in the hash table. 
- **`Space Complexity`**
The space complexity for a hash table is *`O(n)`*, where *n* is the number of entries. This accounts for the storage of keys and their associated values.

> Useful ways to manipulate dictionaries in *Python*.
```python
#initialization
d = {}
d = dict()
```
```python
#insertion
d[key] = value
```
```python
#lookup
value = d[key]

#deletion
del d[key]
```
```python
#check for the existance of key
if key in d:
    # Do something
```
```python
#retrive all keys in dictionary
keys = d.keys()

#retrieve all values in dictionary
values = d.values()

#get all key-value pairs.
items = d.items()
```
```python
#if key doesn't exist in dictionary, set default value
d.setdefault(key, default_value)

#retrieve value with a default if key is not present.
value = d.get(key, default_value)
```
```python
#merge two dictionaries
d.update(another_dict)
```
```python
#remove & return value for given key
value = d.pop(key, default_value)

#remove and return some (key, value) pair as a 2-tuple.
key, value = d.popitem()
```
```python
#remove all items from dictionary
d.clear()
```



#### **`Arrays`**:
#### **`Linked List`**:
#### **`Stacks`**:

A *stack* is a linear data structure that follows *LIFO* principle. *LIFO* is an acronym for *Last In First Out* and describes the behavior which are exihited by these data structures. For example, if you have a stack of books, stacked ontop of each other: the last book you place on the stack is the first book you'd remove from the stack.

Irrespective of your choice of scripting language, all *Stack* data structures should implement the following functionalities:
- **Push:** Add an item to the top of the stack.
- **Pop:** Remove item from top of the stack.
- **Peek/Top:** Returns the top element of stack without removing it.
- **isEmpty:** Checks if the stack is empty.


> The primary feature of a stack is that it onlys allows access to the top element, therefore you can't access items below the top item without removing the top items one by one.

#### **`Time Complexities of Stacks :`**

|         **`Operation`**               |       **`Time Complexity`**                                                 | 
|---------------------------------------|:---------------------------------------------------------------------------:|  
| **`Push`**                            | *O(1)* - Constant time to add an element to the top.                          | 
|  **`Pop`**                            | *O(1)* - Constant time to remove the top element.                             |   
| **`Peek/Top`**                        | *O(1)* - Constant time to look at the top element.                            |
| **`isEmpty`**                         | *O(1)* - Constant time to check if the stack is empty.                        |

> Space complexity for a stack containing *n* elements is  *O(n)*.

You can use the **`deque`** method from the collections library to implement stack operations but the methodologies can be applied using built-in python **`Lists`** as show below.

```python
#Push item to the top of stack.
stack.append(item)
```
```python
#Pop item from the top of stack.
item = stack.pop()
```
```python
#Retrieve the top item from stack
top = stack[-1]
```
```python
#Check is stack is empty
is_empty = not stack
```


#### **`Queue`**:

Queues are linear data structures that follow *First In First Out* (*FIFO*) principle. For example, a line of people waiting at a bank. The first person in line will be the first person to be served.






