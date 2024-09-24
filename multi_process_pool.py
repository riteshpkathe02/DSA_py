from multiprocessing import Pool
import time
'''
#Simple Function
def sq_root(n):
    return n**0.5

if __name__ == "__main__":
    arr = [1,4,16,25]
    p = Pool() #Object of pool class
    result = p.map(sq_root,arr) #Method of p class(function, input) THIS FUNCTION/METHOD DIVIDES WORK OF PROCESSING ACROSS MULTIPLE CORES OF CPU
    print(result)
'''

#Complex Function
def f(n):
    sum=0
    for x in range(n):
        sum += x**2
    return sum

if __name__ == "__main__":

    t1 = time.time() #Creating timestamp
    p = Pool(processes=3) #Creates 3 processes at a time
    result =p.map(f,range(20000))
    p.close()
    p.join()

    print("Pool took: ", time.time()-t1)

    t2 = time.time()
    res = []
    for x in range(20000):
        res.append(f(x))

    print("Serial processing took : ", time.time()-t2)