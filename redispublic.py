#-*- coding: utf-8 -*-

import redis, logging


def redisConnect():
    try:
        redisPool = redis.ConnectionPool(host='10.30.17.119', port=7800, decode_responses=True, db=5, socket_timeout=10,password='aiNcxzojSUCBiKqB2dJz')
        r = redis.Redis(connection_pool=redisPool)
        return r
    except ConnectionError as error:
        logging.error(error)
        return error
    except redis.RedisError as error:
        logging.error(error)
        return error

