from multiprocessing import Process


def execute(part_one, part_two):
    p1 = Process(target=part_one)
    p2 = Process(target=part_two)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Done!")
