# Hash Tables

A hash table is a data structure that stores key-value pairs. It uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.

![alt text](image.png)

Elements are accessed by keys. The hash function takes a key and returns an index in the hash table. The hash table will have an array of buckets, each with a unique index. The hash function will return the index of the bucket where the key-value pair should be stored. Hash tables stores the data in a very efficient way so that retrieval can be very fast. Hash tables are based on a concept called hashing

## Hashing functions

A hash function is a function that converts an input (or 'key') into an integer value. The hash function is used to map the key to a specific location in the hash table. The hash function should be deterministic, meaning that the same input will always produce the same output. The hash function should also be fast to compute. In practice, most hash functions are not perfect and can sometimes produce the same output for different inputs. This is called a 'collision'. There are different ways to handle collisions, such as chaining or open addressing.
If we try to develop a hash function that avoids collisions, this becomes very slow, and a slow hash function does not serve the purpose of the hash table. So, we use a fast hash function and try to find a strategy to resolve the collisions rather than trying to find a perfect hash function

Example:

```python
def myhash(s):
       mult = 1
       hv = 0
       for ch in s:
           hv += mult * ord(ch)
           mult += 1
       return hv
```

### Resolving Collisions

![alt text](image-1.png)

There are two main ways to resolve collisions in a hash table: chaining and open addressing.

### Open Addressing
