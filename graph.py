class graph():
    '''
    Class to store the graph
    '''
    def __init__(self):
        self.nodes = {}
        
    def add_node(self, node_name, weight):
        '''
        Function to add single node to the graph. Each node is a dictionary with two keys:
        'weight': the weight of the node, 'adjacent': list of node's name that can be connected from the current node
        
        :param node_name: str, the name of the node
        :param weight: float, weight of the node
        '''
        try:
            temp_dict = self.nodes[node_name]
        except:
            temp_dict = {}
            temp_dict['weight'] = 0
            temp_dict['adjacent'] = []
        temp_dict['weight'] = weight
        self.nodes[node_name] = temp_dict
        
    def add_edge(self, start_node, end_node):
        '''
        Function to add single edge to the graph. Each node is a dictionary with two keys:
        'weight': the weight of the node
        'adjacent': list of node's name that can be connected from the current node
        
        :param start_node: str, name of the depature node
        :param end_node: str, name of the destination node
        '''
        
        try:
            temp = self.nodes[start_node]
            temp = self.nodes[end_node]
        except:
            print('Node does not exist!')
            return
        if end_node not in self.nodes[start_node]['adjacent']:
            self.nodes[start_node]['adjacent'].append(end_node)
        
    
    def __dfs(self, node, sum_path, visited):
        '''
        Function to calculate optimal sum path using dynamic programming
        
        :param node: str, name of the current node
        :param sum_path: maximum sum of subsequent path starting from this node
        :param visited: dict, record which node has been visited
        '''
        # Check to be visited
        visited[node] = True
        out_list = self.nodes[node]['adjacent']
        
        # Carry out depth first search to all connected nodes
        for adj_node in out_list:
            if not visited[adj_node]:
                self.__dfs(adj_node, sum_path, visited)
                
            # Compare the new path with the current value
            sum_path[node] = max(sum_path[node], self.nodes[adj_node]['weight'] + sum_path[adj_node])
        
        
    def find_max_path(self, start_node):
        '''
        Function to calculate optimal sum path
        
        :param start_node: str, the starting point
        '''
        # Initiated visited status and path sum for all nodes
        visited = {}
        sum_path = {}
        for node in self.nodes.keys():
            visited[node] = False
            sum_path[node] = 0
        visited[start_node] = True
        
        # Carry out search for 
        self.__dfs(start_node, sum_path, visited)
        sum_path_max = sum_path[start_node] + self.nodes[start_node]['weight']
        return sum_path_max
    
    ######################################################################
    # This concludes the solution for acyclic graph
    # The codes that follow deal with cyclic graph (with loop)
    # The codes are adapted from https://www.geeksforgeeks.org/strongly-connected-components/
    ####################################################################
    
    def dfs_util(self, node, visited, node_circle):
        '''
        Function to recursively travel the graph and record loop if found
        
        :param node: str, the current node
        :param visited: dict, record of visited node
        :param node_circle: list, record of possible loop
        '''
        visited[node] = True
        node_circle.append(node)
        for node_now in self.nodes[node]['adjacent']:
            if visited[node_now] == False:
                self.dfs_util(node_now, visited, node_circle)
                
                
    def fill_order(self, node, visited, stack):
        '''
        Function to recursively travel the graph and store order in a stack
        
        :param node: str, the current node
        :param visited: dict, record of visited node
        :param stack: list, stack list recording travelled node
        '''
        visited[node] = True
        for adj_node in self.nodes[node]['adjacent']:
            if visited[adj_node] == False:
                self.fill_order(adj_node, visited, stack)
        stack = stack.append(node)

        
    def get_transpose(self):
        '''
        Function to reverse the graph's direction
        '''
        g = graph()
        for node in self.nodes.keys():
            g.add_node(node, self.nodes[node]['weight'])
            
        for node in self.nodes.keys():
            for adj_node in self.nodes[node]['adjacent']:
                g.add_edge(adj_node, node)
        return g
    
    def get_loop(self):
        '''
        Function find all the loops in the graph
        '''
        stack = []
        visited = {}
        for node in self.nodes.keys():
            visited[node] = False
            
        for node in self.nodes.keys():
            if visited[node] == False:
                self.fill_order(node, visited, stack)
                
        G_transpose = self.get_transpose()
        visited = {}
        for node in self.nodes.keys():
            visited[node] = False
            
        node_list = []
        while stack:
            node = stack.pop()
            if visited[node]==False:
                node_circle = []
                G_transpose.dfs_util(node, visited, node_circle)
                if len(node_circle) >= 2:
                    node_list.append(node_circle)
                
        return node_list
    
    
# Driver Code  
if __name__ == "__main__":
    G = graph()

    G.add_node('A',2)
    G.add_node('B',1)
    G.add_node('C',3)
    G.add_node('D',3)
    G.add_node('E',4)
    G.add_node('F',6)
    G.add_node('G',3)
    
    G.add_edge('A','F')
    G.add_edge('F','G')
    G.add_edge('A','B')
    G.add_edge('A','C')
    G.add_edge('C','D')
    G.add_edge('B','D')
    G.add_edge('D','E')
    
    G.find_max_path('A')
    
    
    
