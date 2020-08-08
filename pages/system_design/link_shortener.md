---
layout: page
title:  System Design - link shortener
---

[educative.io](https://www.educative.io/courses/grokking-the-system-design-interview/m2ygV4E81AR)


7. data partitioning and replication
-----------------------
- range based partitioning:
    - all URL's starting with 'A' goes into this bucket
    - can store less frequently used letters in one bucket/node
    - could become unblanced
- hash-based partitioning
    - use a key hash to map to one of 1-256 servers
    - could still lead to overloaded partitions? can be solved by consistent hashing?



8. caching
------------

- to reduce DB load, can check cache before hitting the DB
- can precompute frequently used data and store in cache

- consider cache eviction policies like LRU
- what happens in a cache miss?
    -> fetch from backend DB
    -> update all cache replicas

- memcache
    - stores in memory to avoid giong to external disks
    - large distributed hashtable
    - reduces DB load
    - client server app over tcp/udp
    - NOT persistent

- redit
    - get/set operations
    - supports richer data types including string, hash, list



9. load balancers
----------------

- add LB at 3 layers
    - between users and app servers
    - between app servers and DB
    - between servers and cache servers

- round robin approach to distribute incoming requests



10. purging or DB cleanup (expired urls)
----------------------

Approaches
- active search for exipred links could put pressure on DB
- lazy cleanup could delete links as user requests them and delete if expired
- cleanup service to be schduled to run at low usage hours



11 and 12. analytics and security
--------------------

otehr requirements that needs to be considered
- 

