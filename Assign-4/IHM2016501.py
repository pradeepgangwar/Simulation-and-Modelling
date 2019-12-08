## Submitted by IHM2016501 | Pradeep Gangwar


# Global variables
S = 6                 # Wing area
T = 1450              # Thrust  
p = 0.5255            # Air density
k = 0.013             # dw/dt
K = 0.035             # constant
cd = 0.025            # Constant
interval = 600       # Print interval

## Distance covered
distance_covered = 0

## Delta v to calculate change in velocity in an interval
def delta_v(v, w, delta_t):
    numerator = 2*k*K*w*delta_t
    denominator = S*p*v*(cd*S*p*v*v - T)
    return (numerator/denominator)

## Delta w to calculate change in weight in an interval
def delta_w(delta_t):
    return -k*delta_t

## Function to simulate the aircraft model
def simulate(v_initial, w_inital, t_initial, t_final, delta_t):
    global distance_covered

    steps = ((t_final - t_initial)/delta_t) + 1
    v = v_initial
    w = w_inital
    for i in range(int(steps)):
        v += delta_v(v, w, delta_t)
        distance_covered += v*delta_t
        w += delta_w(delta_t)

        # Print current situation
        if (i % interval == 0):
            print("Velocity: {} Weight: {}, Distance: {}, Time: {}".format(v,w,distance_covered,i))

        ## If aircraft is out of fuel. Break
        if (w < 0):
            print("No fuel now")
            break

    print("Total distance coveredis : {}".format(distance_covered))

if __name__=='__main__':
    v_initial = 153              # Initial velocity
    w_inital = 10000             # Initial weight
    t_initial = 0                # Inital time
    t_final = 1*60*60            # Simulation time
    delta_t = 0.01               # Time interval Delta t

    simulate(v_initial, w_inital, t_initial, t_final, delta_t)
