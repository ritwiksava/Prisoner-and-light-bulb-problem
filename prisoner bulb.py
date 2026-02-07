import random 
def simulate_prisoners(n):
    leader_count = 0
    bulb = random.choice([0,1])
    has_signaled = [False] *  n #this is like their permission . if they already signaled it will be set to true which means they cant turn the bulb on again 
    visits = [0] * n #were declaring an array for all the pisoners and when a prisoner is chosen we update his index with 1 
    total_visits = 0
    

    while leader_count < (n-1) :
        prisoner = random.randint(0 , n-1) #choosing a prisoner and updating it 
        visits[prisoner] += 1
        total_visits += 1 

        # for leader 
        if prisoner == 0 : #ie if the prisoner who entered is the leader (we choose prisoner 0 to be the leader)
            if bulb == 1 :
                bulb = 0 
                leader_count += 1 
        # for prisoners other than leader
        else :  
            if not has_signaled[prisoner] and bulb == 0 :
                bulb = 1 
                has_signaled[prisoner] = True
    return visits , total_visits 

print(simulate_prisoners(100))




