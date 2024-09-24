import time
import threading

def calc_square(numbers):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(0.2)
        print('square: ', n**2)

def calc_cube(numbers):
    print("calculate cube numbers")
    for n in numbers:
        time.sleep(0.2)
        print('cube: ', n**3)

arr = [2,3,4,5]

t = time.time()
t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))

t1.start() #starts t1
t2.start() #starts t2

t1.join() #Joins to main program after completion of thread
t2.join()

print("Done in : ", time.time()-t)
print("DONE dana DONE")