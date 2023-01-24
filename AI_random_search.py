import random as np

dict={"S0": ["S1","S0"],

    "S1": ["S0" ,"S2"],

    "S2": ["S2" ,"S1"]}


def randomSearch(initial_Node,target_Node):
    current_Node=initial_Node
    while(True):
        lent=len(dict[current_Node])
        if(current_Node==target_Node):
            return "success"
        elif(lent==0):
            return "failed"
        else:
            current_Node=dict[current_Node][np.randint(0,lent-1)]




print(randomSearch("S0","S3"))
