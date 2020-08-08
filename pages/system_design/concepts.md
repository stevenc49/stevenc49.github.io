---
layout: page
title:  System Design - Concepts
---

[architecting systems for scale](https://lethain.com/introduction-to-architecting-systems-for-scale/)

- Message Queues (RabbitMQ and kafka)
    - buffer where producers add expensive workload tasks
    - worker consumers take and process tasks

- Periodic Tasks
    - Like 'link cleanup service' in link shortener
    
- Map-Reduce
