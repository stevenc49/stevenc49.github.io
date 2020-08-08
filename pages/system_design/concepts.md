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
    - once you start sharding your DB and SQL queries don't work
    - distributed data processing

- Platform Layer
    - an interface for other microservices to interact with a 3rd party




- long polling vs websockets vs server-sent events
    - ajax polling
        - many http reqs and responses
    - http long-polling (hanging GET)
        - client expects the server to not respond immediately
    - web-sockets
        - full deplex communication over tcp connection
    - server sent events

