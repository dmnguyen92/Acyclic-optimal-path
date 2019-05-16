from graph_loop import *

if __name__ == "__main__":
    G = graph()
    
    # Receive nodes input
    n = input('Enter number of nodes: ')
    print('Enter nodes in format "node_name weight" ')
    for i in range(int(n)):
        temp = input()
        node_name, weight = temp.split(' ')
        node_name = str(node_name)
        weight = float(weight)
        G.add_node(node_name, weight)
        
    # Receive edge input
    m = input('Enter number of edges: ')
    print('Enter edges in format "node_start node_end" ')
    for i in range(int(m)):
        temp = input()
        node_start, node_end = temp.split(' ')
        node_start = str(node_start)
        node_end = str(node_end)
        G.add_edge(node_start, node_end)
    
    start_node = input('Enter start node: ')
    
    loops = G.get_loop()
    if len(loops)>0:
        print('Loops detected with the following nodes: \n')
        for loop in loops:
            print(loop)
        print('Please try again!')
    else:
        print('Maximum weight path: %.0f' %G.find_max_path(start_node))        
    