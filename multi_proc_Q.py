import multiprocessing

def calc_square(numbers, q): #Process 2(Child)
    for n in numbers:
        q.put(n**2)

if __name__=="__main__": #Process 1(Parent)
    numbers = [4,3,2]
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=calc_square, args=(numbers,q))

    p.start()
    p.join()

    while q.empty() is False:
        print(q.get())