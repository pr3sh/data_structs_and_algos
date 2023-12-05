
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
    - [Heaps](#heaps)
  - [Algorithms](#algorithms)
    - [Depth First Search](#depth-first-search)
    - [Breadth First Search](#breadth-first-search)
  



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

- A linked list is a linear data structure where each element (commonly called a 'node') contains a data part and a reference (or link) to the next node in the sequence. 
- Unlike arrays, data in a linked list are not stored in contiguous memory locations; they are linked using pointers, making the structure dynamic and flexible.

**`Types of Linked Lists`**:

- **`Singly Linked List`**: Each node contains data and a pointer to the next node.
- Doubly Linked List: Each node contains data, a pointer to the next node, and a pointer to the previous node.
- Circular Linked List: The last node points back to the first node, forming a circle.

**`Basic Operations`**:
- **`Insertion`**: Add a new node to the list.
- **`Deletion`**: Remove a node from the list.
- **`Traversal`**: Access each node of the list, typically starting from the first node.
- **`Search`**: Find a node in the list with a given value.
- **`Update`**: Modify the data of a node.

**`Advantages Over Arrays`**:
- **`Dynamic Size`**: The size of a linked list can grow or shrink during execution.
- **`Efficient Insertions/Deletions`**: Inserting or deleting elements doesn't require shifting other elements, as in an array.

**`Disadvantages`**:
- **`Memory Usage`**: Each node requires extra memory for a pointer.
- **`Sequential Access`**: Direct access to an element is not possible; you have to traverse the list from the beginning.

> *Example*

```python
#create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# create Linked List
class LinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty

    def append(self, data):
        """ Appends a new node to the end of the list. """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        """ Prints all the elements in the list. """
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

```

> *Usage*

```python
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)

llist.print_list()  # Output: 1 2 3

```
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

You can use the **`deque`** method from the **`collections`** library to implement stack operations but the methodologies can be applied using built-in python **`Lists`** as show below.

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

Irrespective of your choice of scripting language, all *Queue* data structures should implement the following functionalities:
- **Enqueue:** Adds an item to the rear of the queue.
- **Dequeue:** Removes the front item from the queue.
- **Front/Peek:** Returns the front element without removing it.
- **Rear:** Returns the last element without removing it (not always used in basic queue implementations).
- **isEmpty:** Checks if the queue is empty.
- **isFull:** Checks if the queue is full (*relevant for queues with a fixed size, like array-based queues*).

> The primary feature of a queue is that it allows access to only the front element, and items are added at the rear.


#### **`Time Complexities of Queue :`**

|         **`Operation`**               |       **`Time Complexity`**                                                   | 
|---------------------------------------|:-----------------------------------------------------------------------------:|  
| **`Enqueue`**                         | *O(1)* - Constant time to add an element to the rear.                         | 
| **`Dequeue`**                         | *O(1)* - Constant time to remove the front element.                           |   
| **`Front/Peek`**                      | *O(1)* - Constant time to look at the front element.                          |
| **`Rear`**                            | *O(1)* - Constant time to look at the rear element (*if supported*).          |
| **`isEmpty/isFull`**                  | *O(1)* - Constant time to check                                               |


> Space complexity for a queue containing *n* elements is *O(n)*.


You can use the **`deque`** method from the **`collections`** library to implement queue operations as shown below:

```python
from collections import deque

#Initialize queue data structure
queue = deque()
```

```python
#Enqueue
queue.append(item)


#Dequeue
item = queue.popleft()
```

```python
#Front/peek
front = queue[0]


#Rear
rear = queue[-1]
```

```python
is_empty = not queue
```

> Although these operations can be done using Python's built-in lists data structure, it is not recommended. Using **`deque`** from the **`collections`** module is the recommended way to implement a queue in Python because of its efficient **`popleft()`** operation.

#### **`Heaps`**:


Heaps are specialized tree-based data structures that satisfies the heap property. It is an important structure because it's efficient for priority queue operations. There are primarily two types of heaps:

1. **Max Heap:** 
    - For any given node *`I`*, the value of *`I`* is greater than or equal to the values of its children. 
    - The largest element is found at the *root*.
2. **Min Heap:** 
    - For any given node *`I`*, the value of *`I`* is less than or equal to the values of its children. 
    - The smallest element is found at the *root*.

Some common operations with heaps include:
- **Insertion:** Insert a new node takes *`O(logn)`* time.
- **Deletion:** Deleting the maximum element (in a max heap) or the minimum element (in a min heap), also known as *heapify*, takes *`O(logn)`* time.
- **Peek:** Get the maximum item from a max heap or the minimum item from a min heap in *`O(1)`* time without removing it.

Heaps are typically implemented as binary trees, but don't necesarily have to be binary. The important thing is not the number of children each node has, but that the tree satisfies the heap property.

> The space complexity for a heap containing *`O(n)`*.

Python has a built-in library called **`heapq`** that provides functions to convert a regular list into a heap (implemented as a binary tree). By default, it creates a min heap. If you want to use a max heap, you can invert the order by multiplying the elements by -1.


```python
import heapq
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
heapq.heapify(nums)  # Transforms nums in-place into a heap
```

```python
#insertion
heapq.heappush(nums, value)
```

```python
min_value = heapq.heappop(nums)  # Returns and removes the smallest value from the heap
```

```python
min_value = nums[0]
```

```python
#create max heap
max_heap = [-1 * i for i in nums]
heapq.heapify(max_heap)
```

```python
#insertion into max-heap
heapq.heappush(max_heap, -1 * value)
```

```python
#deletion from max-heap
max_value = -1 * heapq.heappop(max_heap)
```

#### **`Depth First Search`**:

- Depth–first search (*DFS*) is an algorithm for traversing/searching trees and graph data structures. Starting from the root, explore as far as possible along each branch before backtracking.
- Stacks are the main Data Structures needed when implementing *DFS* to keep track of the nodes discovered during traversal on specified branches which helps in backtracking of the graph.
- *DFS* can be implemented both iteratively and *recursively*.









