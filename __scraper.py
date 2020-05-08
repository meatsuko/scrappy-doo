import string, random, urllib, os, thread, array, sys


worker_threads = 64;
worker_unload = 0;

workOut = [0, 503, 4939, 4940, 4941, 12003, 12716, 5556, 5082]


def __scrapWorker():

    worker_mode = int(''.join(random.choice('5' + '7') for _ in range(1)))
    worker_mode = 5

    N, C, E = (2, 1, 2)

    if worker_mode == 6:
        N, C, E = (2, 2, 2)

    if worker_mode == 7:
        N, C, E = (2, 3, 2)

    while True:

        uri_part_0 = str(''.join(random.choice(string.ascii_uppercase + string.digits + string.lowercase) for _ in range(N)));
        uri_part_1 = str(''.join(random.choice(string.ascii_uppercase + string.digits + string.lowercase) for _ in range(C)));
        uri_part_2 = str(''.join(random.choice(string.ascii_uppercase + string.digits + string.lowercase) for _ in range(E)));


        file_name = "" + str(uri_part_0) + str(uri_part_1) + str(uri_part_2) + ".jpg"
        file_patn_name = "__content/" + file_name


        url = "http://i.imgur.com/" + str(file_name)

        urllib.urlretrieve(url, str(file_patn_name))

        file_size = os.path.getsize(str(file_patn_name))

        if file_size in workOut:
            os.remove(file_patn_name)
        else:
            print "[+] Valid: " + url




for worker_id in range(worker_threads):
    thread.start_new_thread(__scrapWorker, ())

while True:
    worker_unload = 1 + 1
