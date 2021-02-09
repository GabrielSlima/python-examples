from multiprocessing import Process
import time


def get_name(name):
    print("Processed: {}".format(name))
    time.sleep(5)


def update_status(jobs):
    status = []
    for job in jobs.values():
        status.append(job.is_alive())
    return status


def get_names_async(names, MAX_POOLS, each_request_timeout):
    end_item = MAX_POOLS
    start_item = 0
    total_processed_items = []
    while start_item <= len(names) - 1:
        jobs = {}
        for current_index, name in enumerate(names[start_item: end_item]):
            process = Process(target=get_name, args=(name,))
            process.start()
            total_processed_items.append(name)
            jobs[name] = process

        update_status(jobs)
        healthcheck_time = 0
        there_is_running_jobs = True
        while there_is_running_jobs in update_status(jobs):
            time.sleep(5)
            healthcheck_time += 5
            if healthcheck_time == each_request_timeout:
                raise Exception("Couldn't get all responses: {}".format(jobs))
        start_item = len(total_processed_items)
        end_item += MAX_POOLS
        print("Processed items: {}".format(jobs.keys()))
        print("Total processed items: {}".format(total_processed_items))


if __name__ == '__main__':
    names = ['Gabriel', "Caio", "Adriano", "Jagunço", "Marcelo", "Jonas", "Ana", "Samuel", "Messias"]
    jobs = []
    get_names_async(names, 5, 300)
