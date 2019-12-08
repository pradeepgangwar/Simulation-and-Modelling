## Submitted by IHM2016501 | Pradeep Gangwar

import time
import queue
import threading 

# Queue to maintain customer services and other imp. global variables
customers = queue.Queue()
cust_served = 0
curr_time = 0
queue_length_cumulative = 0
server_idle_time = 0
server_idle = True

"""
Simulating a clock
"""
def clock(num_customers):
    global curr_time
    global cust_served
    global server_idle_time
    global server_idle
    global queue_length_cumulative
    global customers

    while cust_served < num_customers:
        curr_time += 1
        time.sleep(1)
        if server_idle:
            server_idle_time += 1
        queue_length_cumulative += customers.qsize()
        

"""
 Function to serve customers request
"""
def server(num_customers):
    global curr_time
    global server_idle
    global cust_served

    while cust_served < num_customers:
        if not customers.empty():
            server_idle = False
            cust_no, arrival, departure = customers.get()
            print( "Server: Customer no. {} has started executing task".format(cust_no) )
            time.sleep(departure)
            print( "Customer no. {} has finished the task. Departing at time {}.".format(cust_no, int(curr_time)) )
            cust_served += 1
        else:
            server_idle = True

"""
 Function to maintain customer queue
"""
def customer_queue():
    file = open('input.txt', 'r')
    num_customers = int(file.readline())

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
    num_customers = int(file.readline())
    file.close()
    
    try:
        t1 = threading.Thread(target=customer_queue, args=())
        t2 = threading.Thread(target=server, args=(num_customers,))
        t3 = threading.Thread(target=clock, args=(num_customers,))
        
    except Exception as e:
        print(e)

    t1.start() 
    t2.start()
    t3.start()
  
    # Wait here for threads to finish
    t3.join()
    t1.join()
    t2.join()
    

    print("\nFinal Results are:\n")
    print("Total simulation time is: {}".format(curr_time))
    print("Avarage queue length is: {}".format(queue_length_cumulative/curr_time))
    print("Total Idle time of server was: {}".format(server_idle_time))
