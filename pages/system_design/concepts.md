---
layout: page
title:  System Design - Concepts
---



other system design resources
----------
- [reddit udacity architecture course](https://www.youtube.com/watch?v=pjNTgULVVf4&list=PLVi1LmRuKQ0NINQfjKLVen7J2lZFL35wP)
- [harvard scalabilty course](https://www.youtube.com/watch?v=-W9F__D3oY4)

- [grokking system design interviews](https://www.youtube.com/watch?v=ZgdS0EUmn70&list=PL73KFetZlkJSZ9vTDSJ1swZhe6CIYkqTL)
- https://github.com/donnemartin/system-design-primer

[back of the envelope calculations](https://www.reddit.com/r/cscareerquestions/comments/6c3x0h/for_system_design_interview_questions_are_back_of/)


___________________



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

