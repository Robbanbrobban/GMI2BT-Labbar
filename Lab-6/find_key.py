import os
import concurrent.futures
import multiprocessing
import psutil
import time
import numpy as np
# Skapar en meny

clear = lambda: os.system('cls')
def menu():
    print(f'+———————————————( Find key)——————————————+')
    print(' | 1. Start searching key                 |')
    print(' | 2. Exit program                        |')
    print(f'+————————————————————————————————————————+')
    print("Total cores:", psutil.cpu_count(logical=True))

# init global variables for processes


def init_globals(key_not_found, hidden_key):
    global KEY_NOT_FOUND
    global HIDDEN_KEY
    KEY_NOT_FOUND = key_not_found
    HIDDEN_KEY = hidden_key


def program():
    # kollar antalet kärnor i processorn
    cpu_cores = psutil.cpu_count(logical=True)
    # skapa lista av cpuerna
    cpu_core = []
    for i in range(cpu_cores):
        cpu_core.append(i)
    # Eftersom varje kärna ska ta en del av talet så behöver vi dela upp det
    
    #Dela Variablen på dem olika kärnorna
    key_not_found = multiprocessing.Value('i', True)
    
    #sätter hidden_key_max för att kunna styra hur stort tal
    hidden_key_max = np.uint32(5000000)
    hidden_key = np.random.randint(low=0, high=hidden_key_max, dtype=np.uint32)
    keys = keyspace(cpu_cores, hidden_key_max)
    
    print(f'================| Config |================')
    print(f'          Cpus: {cpu_cores}')
    print(f'          Range: 0 - {hidden_key_max}')
    print(f'          Hidden Key: {hidden_key}')
    print(f'==========================================')
  
    
    # sätta timer
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=cpu_cores,
                                                initializer=init_globals, initargs=(key_not_found, hidden_key)) as executor:
        for result in executor.map(find_hidden_key, cpu_core, keys['start'], keys['end']):
            print(result)
    # Stop timer
    stop = time.perf_counter()
    timer = stop - start
    kps = around_kps(hidden_key, keys['start'], timer, cpu_cores)
    whole_keyspace = time.strftime('%H:%M:%S', time.gmtime(int(hidden_key_max / kps)))
    
    print(f'============================| Info |===========================')
    print(f'          Finished in {round(timer, 2)} seconds')
    print(f'          Around {round(kps, 2)} per second was tested   ')
    print(f'          To Brute whole keypace would take: {whole_keyspace}')
    print(f'===============================================================')
    print()
    input('Press Enter to try again')
    
    #Dela upp talet till varje cpu genom att skapa en start lista och slut lista
def keyspace(cpu, max_num):
    offset = int(max_num / cpu)
    offset_temp = offset
    #börjar på 0
    list_start = [0]
    list_end = []
    for i in range(cpu):
        list_start.append(offset)
        list_end.append(offset)
        offset += offset_temp
    list_start.pop()
    list_end.pop()
    list_end.append(max_num)
    return{'start': list_start, 'end': list_end}

#
def find_hidden_key(cpu, cur_key, end_key):
    print(f'  Cpu: {cpu} keyspace start at {cur_key} and end at {end_key}')
    
    while KEY_NOT_FOUND.value and (cur_key <= end_key):
        if cur_key == HIDDEN_KEY:
            KEY_NOT_FOUND.value = False
            print(f'  Hidden Key found by CPU {cpu}: {cur_key}')
        else:
            cur_key += 1
        if cur_key % 1000000 == 0:
            print(f'  Cpu: {cpu} is at value: {cur_key}')
    return f'  Cpu: {cpu} reached key {cur_key}'

def around_kps(key, start, time_taken, cpus):
    i = 0
    key_start = 0
    while cpus > i and key > start[i]:
        i += 1
        key_start = start [i-1]
    #    
    return ((key - key_start) / time_taken) * cpus
            
if __name__ == '__main__':
    while True:
        clear()
        menu()
        choice = input('    Your choice: ')
        if choice == '1':
            program()
        elif choice == '2':
            print('Program Shutting down...')
            # Exit Program
            break
        else:
            print(f'+————————————————————————————————————————————————————————————+')
            print(" |                 Choose a vaild number                      |")
            print(f'+————————————————————————————————————————————————————————————+')
