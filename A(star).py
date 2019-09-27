graph = [[0,1,2,10,0,0,0,0],
         [0,0,0,0,5,0,0,0],
         [0,0,0,0,0,4,0,0],
         [0,0,0,0,0,6,0,0],
         [0,0,0,0,0,0,2,3],
         [0,0,0,0,0,0,0,7],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0]]
heuristic_value = {0:13,1:7,2:9,3:11,4:2,5:4,6:1,7:0}
path={}
def available_postions(i):
    pos=[]
    for j in range(0, len(graph[i])):
        if graph[i][j]!=0:
            pos.append(j)
    return pos
def pathgenerator(x,y):
    return (y*(10**len(str(x)))+x)
minpathkey,flag=0,0
while(1):
    avpos=available_postions(int(str(minpathkey)[0]))
    for x in avpos:
        if int(minpathkey) in list(path.keys()):
            path[pathgenerator(minpathkey,x)]=path[minpathkey]-heuristic_value[int(str(minpathkey)[0])]+graph[int(str(minpathkey)[0])][x]+heuristic_value[x]
            flag=1
        else:
            path[pathgenerator(minpathkey,x)] = heuristic_value[x]+graph[int(str(minpathkey)[0])][x]
    if flag==1:
        del path[minpathkey]
        flag=0
    minpathkey=min(path, key=path.get)
    if (len(available_postions(int(str(minpathkey)[0]))) == 0) and (str(minpathkey)[0] != str(len(graph)-1)):
        del path[minpathkey]
        minpathkey = min(path, key=path.get)
    if (str(minpathkey)[0] == str(len(graph)-1)):
        break
print(path)
print(list(path.keys()))        
