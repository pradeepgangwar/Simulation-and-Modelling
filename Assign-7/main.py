## Submitted by IHM2016501 | Pradeep Gangwar

import time
import queue
import threading 

# Queue to maintain customer services and other imp. global variables
customers = queue.Queue()
cust_served = 0
curr_time = 0
queue_length_cumulative = 0
server_idle_time = []
server_idle = []

"""
Simulating a clock
"""
def clock(num_customers, num_server):
    global curr_time
    global cust_served
    global server_idle_time
    global server_idle
    global queue_length_cumulative
    global customers

    while cust_served < num_customers:
        curr_time += 1
        time.sleep(1)
        for i in range(num_server):
            if server_idle[i]:
                server_idle_time[i] += 1
        queue_length_cumulative += customers.qsize()
        

"""
 Function to serve customers request
"""
def server(num_customers, server_no, lock):
    global curr_time
    global server_idle
    global cust_served

    while cust_served < num_customers:
        if not customers.empty():
            server_idle[server_no - 1] = False

            ## Acquiring lock for the shared queue
            lock.acquire()
            cust_no, arrival, departure = customers.get()
            lock.release()

            print( "Server {}: Customer no. {} has started executing task".format(server_no, cust_no) )
            time.sleep(departure)
            print( "Server {}: Customer no. {} has finished the task. Departing at time {}.".format(server_no, cust_no, int(curr_time)) )

            lock.acquire()
            cust_served += 1
            lock.release()
        else:
            server_idle[server_no - 1] = True

"""
 Function to maintain customer queue
"""
def customer_queue(num_customers):
    file = open('input.txt', 'r')
    input_param = file.readline()

    global curr_time

    for i in range(num_customers):
        input = file.readline()
        arrival, departure = input.split()
        arrival = int(arrival)
        departure = int(departure)

        time.sleep(arrival)
        cust_tuple = (i+1, arrival, departure)
        customers.put(cust_tuple)
        print( "Customer no. {}: A new customer has arrived at time {}".format(i+1, int(curr_time)) )       
    
    file.close()


## Main Function ##
if __name__=='__main__':

    file = open('input.txt', 'r')
    input = file.readline()
    num_server, num_customers = input.split()
    num_server = int(num_server)
    num_customers = int(num_customers)
    file.close()


    ## Lock to lock resources
    lock = threading.Lock()

    # Initialize idle time for each server
    for i in range(num_server):
        server_idle.append(True)
        server_idle_time.append(0)
    
    try:
        t1 = threading.Thread(target=clock, args=(num_customers, num_server, ))
        t1.start()
        t2 = threading.Thread(target=customer_queue, args=(num_customers, ))
        t2.start()
        for i in range(num_server):
            t = threading.Thread(target=server, args=(num_customers, i+1, lock, ))
            t.start()
        
    except Exception as e:
        print(e)
  
    # Wait here for threads to finish
    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        t.join()
    

    print("\nFinal Results are:\n")
    print("Total simulation time is: {}".format(curr_time))
    print("Avarage queue length is: {}".format(queue_length_cumulative/curr_time))
    print("Avarage waiting time: {}".format(queue_length_cumulative/num_customers))
    print("Total Idle time of each server was:")
    for i in range(num_server):
        print("Server {}: {} seconds".format(i+1, server_idle_time[i]))

