---
layout: page
title:  System Design - instagram
---

[educative.io](https://www.educative.io/courses/grokking-the-system-design-interview/m2yDVZnQ8lG)

1. What is Instagram?
2. Requirements and Goals of the System
3. Some Design Considerations
4. Capacity Estimation and Constraints
5. High Level System Design
6. Database Schema
7. Data Size Estimation
8. Component Design
9. Reliability and Redundancy
10. Data Sharding
11. Ranking and News Feed Generation
12. News Feed Creation with Sharded Data
13. Cache and Load balancing


1-3. requirements

upload, view news feed, follow other users
tags not in scope



4. capacity estimates

2M new photos per day
avg photo size = 200KB
1 day of photos = 2M * 200KB = 400GB
10 years = 400GB * 265 * 10 = 1425TB


5. high level design
    - image hosting system needs two parts
    - object storage for storing photos
    - DB for storing image metadta

8. component design
    - since upload image is slow, split upload service and download service to different services


6. db schema

tables:
- photo
- user
- userFollow
- user photo cross reference


10. db sharing

partition based on userid
if we do 10 shards, then userid%10

considerations
- hot users, ppl with lots of followers
- some ppl have lots of photos
    - if we shard a single user's photos on multiple servers, will there be high latency?
    - storing all of a user's data in one shard could make it unavailable if it fails





other things to consider
- redundency - losing photos is not an option
