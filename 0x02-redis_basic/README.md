# 0x02. Redis basic

## Overview
This README provides a basic understanding of Redis (REmote DIctionary Server), an open-source, in-memory data structure store used as a database, cache, and message broker. Redis supports various data structures such as strings, hashes, lists, sets, and more. This document covers the essential concepts, features, and usage of Redis.

## Installation
```bash
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```
## Key Features

- In-Memory Data Store: Redis stores data in-memory, making it exceptionally fast for read and write operations.
- Data Structures: Redis supports various data structures like strings, lists, sets, sorted sets, hashes, bitmaps, hyperloglogs, and geospatial indexes, allowing for versatile data storage and manipulation.
- Persistence: Redis offers options for data persistence, including snapshotting and append-only file (AOF) persistence, ensuring data durability.
- Replication: Redis supports master-slave asynchronous replication, enabling data redundancy and fault tolerance.
- Pub/Sub Messaging: Redis facilitates message passing between clients through its Pub/Sub messaging system.
- Lua Scripting: Redis allows the execution of Lua scripts, providing flexibility and customization.
- Transactions: Redis supports transactions, allowing multiple commands to be executed atomically.

## Basic Usage
Once Redis is installed and running, you can interact with it via the Redis command-line interface (`redis-cli`) or through client libraries available in various programming languages.

### Example Commands:
- Setting a Key-Value Pair:
  ```
  SET key value
  ```

- Getting the Value for a Key:
  ```
  GET key
  ```

- Working with Lists:
  ```
  LPUSH list_key value1 value2    // Left Push
  RPUSH list_key value3 value4    // Right Push
  LRANGE list_key 0 -1            // Get all elements of the list
  ```

- Using Sets:
  ```
  SADD set_key member1 member2   // Add members to a set
  SMEMBERS set_key               // Get all members of a set
  ```

## Additional Resources
- [Redis Documentation](https://redis.io/documentation)
- [Redis Commands Reference](https://redis.io/commands)
- [Redis GitHub Repository](https://github.com/redis/redis)
---
