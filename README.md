
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

Data structures and aAlgorithms are fundamental concepts in Computer Science, which are used for the efficient storage and manipulation of data.
Data Structures specifically, refer to the organization, storage and retrival of data, while algorithms refer to the instructions that are utilized to solve a particular problem.





### **`Data Structures`**:


###### **`Hash Maps`**:


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

> However, in the worst-case scenario, these operations can degrade to O(n), where n is the number of entries in the hash table. 
- **`Space Complexity`**
The space complexity for a hash table is *`O(n)`*, where *n* is the number of entries. This accounts for the storage of keys and their associated values.




###### **`Arrays`**:
###### **`Linked List`**:
###### **`Stacks`**:
###### **`Queue`**:




