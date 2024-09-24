import time
import multiprocessing

# square_result=[]

def calc_square(numbers, result):
    # global square_result
    print("calculate square numbers")
    for idx, n in enumerate(numbers):
        # time.sleep(5)
        # print('square: ', n**2)
        # square_result.append(n**2)
        result[idx]=n**2
    # print('within a process result ' + str(square_result))
    

'''def calc_cube(numbers):
    print("calculate cube numbers")
    for n in numbers:
        time.sleep(5)
        print('cube: ', n**3)'''

if __name__=="__main__":
    arr = [2,3,4,5]
    result = multiprocessing.Array('i', 4) #('datatype',size) This is shared memory variable
    p1 = multiprocessing.Process(target=calc_square, args=(arr, result))
    # p2 = multiprocessing.Process(target=calc_cube, args=(arr,))


    p1.start()
    # p2.start()

    p1.join() #It'll wait until processes are executed
    # p2.join()
    
    # print('result ' + str(square_result))
    print(result[:]) 
    print("Done!")

'''
Every prcoess has its own address space(virtual memory).
Thus program variables are not shared between 2 processes.
We need to use inter-process communication techniques  to share data between processes.
'''