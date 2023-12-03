import multiprocessing

bind = "0.0.0.0:7040"
workers = multiprocessing.cpu_count() * 2 + 1