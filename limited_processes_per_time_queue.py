from multiprocessing import Process
from multiprocessing import Queue
import time


def get_name(name, queue):
    time.sleep(2)
    queue.put("Processed: {}".format(name))


def update_status(jobs):
    status = []
    for job in jobs.values():
        status.append(job.is_alive())
    return status


def get_names_async(names, MAX_POOLS, each_request_timeout):
    end_item = MAX_POOLS
    start_item = 0
    total_processed_items = {}
    processed_names = Queue()
    while start_item <= len(names) - 1:
        jobs = {}
        for current_index, name in enumerate(names[start_item: end_item]):
            process = Process(target=get_name, args=(name, processed_names))
            process.start()
            process.join()
            jobs[name] = process
            total_processed_items[name] = process

        healthcheck_time = 0
        there_is_running_jobs = True
        while there_is_running_jobs in update_status(jobs):
            time.sleep(5)
            healthcheck_time += 5
            if healthcheck_time == each_request_timeout:
                raise Exception("Couldn't get all responses: {}".format(jobs))

        start_item = len(total_processed_items)
        end_item += MAX_POOLS
    return processed_names, total_processed_items


if __name__ == '__main__':
    names = ['Gabriel', "Caio", "Adriano", "Jagunço", "Marcelo", "Jonas", "Ana", "Samuel", "Messias"]
    jobs = []
    results, names = get_names_async(names, 5, 300)
    for processed_name in names:
        print("Name: {}, value: {}".format(processed_name, results.get()))
