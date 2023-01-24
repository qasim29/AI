dict={"S0": ["S1","S0"],

    "S1": ["S0" ,"S2"],

    "S2": ["S2" ,"S1"]}

def open_List_Search(initial_Node,target_Node):
    visited = []
    fringe = []
    fringe.append(initial_Node)
    while(True):
        lent=len(fringe)
        if(lent == 0):
            return "failed" 
        current_Node=fringe.pop(0)
        if(current_Node == target_Node):
            return "success"
        else:
            visited.append(current_Node)
            for i in dict[current_Node]:
                if i not in visited:
                    fringe.append(i)        


print(open_List_Search("S0","S3"))