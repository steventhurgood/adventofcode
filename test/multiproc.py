import multiprocessing as mp
from typing import Mapping
import time
import random

import logging

log_format = '%(asctime)s [%(process)d] %(message)s'
logging.basicConfig(format=log_format)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def thing_doer(value: int, shared_cache: Mapping[int, int]):
    logger.info(f'Starting thing_doer {value}')
    time.sleep(random.random() * 3)
    if value in shared_cache:
        logger.info(f'{value} in shared cache: {shared_cache[value]}')
        return shared_cache[value]
    logger.info(f'{value} not in {shared_cache}')
    result = 100 * value
    logger.info(f'Calculating f({value}) = {result}')
    shared_cache[value] = result
    logger.info('Done')
    return result


if __name__ == '__main__':

    num_procs = 10
    with mp.Manager() as manager:
        shared_cache = manager.dict()
        queue = manager.Queue()
        inputs = [random.randint(0, 3) for _ in range(num_procs)]
        procs = []

        def managed_thing_doer(value):
            return thing_doer(value, shared_cache)

        with mp.Pool() as p:
            results = p.map(managed_thing_doer, inputs)
            logger.info(results)
