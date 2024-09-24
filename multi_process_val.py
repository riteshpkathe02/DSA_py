import multiprocessing

def cal_square(numbers, v):
    v.value = 92.094

if __name__ == "__main__":
    numbers = [2,3,5]
    v = multiprocessing.Value('d', 0.0) #(type, value chi value)
    p = multiprocessing.Process(target=cal_square, args=(numbers,v))

    p.start()
    p.join()

    print(v.value)