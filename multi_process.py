import multiprocessing

result =['suburbs']

def cal_root(numbers):
    global result
    for n in numbers:
        result.append(n**0.5)

    print('inside process' + str(result))

if __name__=="__main__":
    numbers = [36,25,64]

    p = multiprocessing.Process(target=cal_root, args=(numbers,))

    p.start()
    p.join()

    print('outside process ' + str(result))