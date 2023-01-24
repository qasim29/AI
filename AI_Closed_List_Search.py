


dict={"S0": ["S1","S0"],

    "S1": ["S0" ,"S2"],

    "S2": ["S2" ,"S1"]}

def closed_List_Search(initial_Node,target_Node):
    current_Node=initial_Node
    visited=[]
    while(True):
        if(current_Node==target_Node):
            return "success"
        else:
            visited.append(current_Node)
            flag=True
            for i in dict[current_Node]:
                current_Node=i
                if (current_Node not in visited):
                    flag=False
                    break
            else:
                return "failed"
            if(flag):
                return "failed"


print(closed_List_Search("S0","S3"))