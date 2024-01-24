#!/usr/bin/env python3
"""
A script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def log_stats() -> None:
    """
    Provides some stats about Nginx logs stored in MongoDB
    """
    try:
        client = MongoClient('mongodb://127.0.0.1:27017')
        nginx_collection = client.logs.nginx
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return

    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    total_logs = nginx_collection.count_documents({})
    stats = f"{total_logs} logs\nMethods:\n"

    for m in method:
        method_count = nginx_collection.count_documents({"method": m})
        stats += f'\tmethod {m}: {method_count}\n'

    status_check_count = nginx_collection.count_documents({"method":
                                                           "GET", "path":
                                                           "/status"})
    stats += f"{status_check_count} status check"

    print(stats)


if __name__ == '__main__':
    log_stats()
