# python-sample
# Python Sample Application 
(Phase 1)

1. This project contains Stores and Items.
2. We can perform operations using REST APIs like
   1. Add a store.
   2. Add an item to a particular store based on store ID.
   3. Get stores list.
   4. Get a particular store based on store ID.
   5. Get items list.
   6. Get a particular item based on item ID.

(Phase 2)
1. Integrate database to existing features of Phase 1.
2. Update configuration files according to environments.

(Phase 3) 

*NOTE - use command `redis-server` in terminal to connect to redis while running the branch on your local, otherwise you may encounter the following error: 

`[Error 61 connecting to localhost:6379. Connection refused.]`*

1. Integrate redis to existing features to store data of items and data.
2. Item and Store data is simultaneosuly stored in Database and Redis. But while storing in Redis, an expiration time is set (60 seconds).
3. First we try to fetch store/item information stored in redis, if not present means the key in redis has expired, only then query the database. And after DB query, store the same key-value pair in redis again.