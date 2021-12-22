import time
import logging

from concurrent.futures import ThreadPoolExecutor


logging.basicConfig(level=logging.DEBUG, format='\n%(threadName)s: %(message)s')


def super_task(a, b):
    time.sleep(1)
    logging.info(f'Terminamos la tarea compleja {a} - {b}!!\n')


if __name__ == '__main__':

    executor = ThreadPoolExecutor(max_workers=4)


    executor.submit(super_task, 0,1)
    executor.submit(super_task, 2,3)
    executor.submit(super_task, 4,5)
    executor.submit(super_task, 6,7)
    executor.submit(super_task, 8,9)
