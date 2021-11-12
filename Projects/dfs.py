# depth first search in graph
# taking graph as input
no_of_nodes=int(input())
graph=[list(map(int,input().strip().split())) for _ in range(no_of_nodes)]
visited=[0]*no_of_nodes
# remember nodes are numbers starts with 0
start_node=int(input())
visited[start_node]=1
stack=[]
stack.append(start_node)
print(start_node)
# running outer loop untill no more element is 
#  present in stack
while stack:
    check=stack[-1]
    start=0
    while start<no_of_nodes:
        # checking wether edge is present to node or not 
        if graph[check][start]==1 and visited[start]==0:
            stack.append(start)
            print(start)
            graph[check][start]=99
            visited[start]=1
            check=start
            start=-1
        start+=1
    stack.pop()
    # backtracking to see any missed edges
