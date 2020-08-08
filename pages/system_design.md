---
layout: page
title:  System Design
---

system design


data partitioning and replication
- range based partitioning:
    - all URL's starting with 'A' goes into this bucket
    - can store less frequently used letters in one bucket/node
    - could become unblanced
- hash-based partitioning
    - use a key hash to map to one of 1-256 servers
    - could still lead to overloaded partitions? can be solved by consistent hashing?

    
