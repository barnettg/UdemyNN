from entity.Node import Node

class NetworkStructure:
    def create_nodes(num_of_features, hidden_nodes):


        nodes = []

        nodeIndex = 0 # unique node index id

        #----------------------

        print("input layer: \t", end='')
        #input layer

        #bias unit
        node = Node()
        node.set_level(0) # level 0 for inputs
        node.set_label("+1")
        node.set_index(nodeIndex)
        node.set_is_bias_unit(True)
        nodes.append(node)
        nodeIndex = nodeIndex + 1

        print(node.get_label(), "\t", end='')
        

        #-----------------------
        # remaining input layer nodes
        for i in range(num_of_features):
            node = Node()
            node.set_level(0) # level 0 for inputs
            node.set_label("X"+str(i+1))
            node.set_index(nodeIndex)
            node.set_is_bias_unit(False)
            nodes.append(node)
            nodeIndex = nodeIndex + 1

            print(node.get_label(), "\t", end='')

        print("")

        #-----------------------------
        #hidden layer
        #---------------------------------
        for i in range(len(hidden_nodes)):

            print("Hidden layer: ", end='')
            #bias unit
            node = Node()
            node.set_level(i+1) # hidden layers
            node.set_label("+1")
            node.set_index(nodeIndex)
            node.set_is_bias_unit(True)
            nodes.append(node)
            nodeIndex = nodeIndex + 1

            print(node.get_label(), "\t", end='')

            for j in range(hidden_nodes[i]):
                node = Node()
                node.set_level(i+1) # hidden layers
                node.set_label("N["+str(i+1)+"] ["+str(j+1)+"]")
                node.set_index(nodeIndex)
                node.set_is_bias_unit(False)
                nodes.append(node)
                nodeIndex = nodeIndex + 1

                print(node.get_label(), "\t", end='')
                
            print("")
        #-----------------------------
        #output layer
        #---------------------------------
        node = Node()
        node.set_level(1+len(hidden_nodes))
        node.set_label("output")
        node.set_index(nodeIndex)
        node.set_is_bias_unit(False)
        nodes.append(node)
        nodeIndex = nodeIndex + 1
        print("output layer: ", node.get_label())    
            
        return nodes
    
