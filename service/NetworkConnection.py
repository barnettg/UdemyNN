from entity.Weight import Weight
import math
import random

class NetworkConnection:
    def create_weights(nodes, num_of_features, hidden_nodes):
        weights = []
        weight_index = 0 # wight id
        #           input layer     hidden nodes    output layer
        total_layers =    1 +       len(hidden_nodes) + 1
        print("Nodes:")
        for item in nodes:
            print("index: " + str(item.get_index())
                  + "  Label: " + str(item.get_label())
                  + "  Bias: " + str(item.get_is_bias_unit())
                  + "  Level: " + str(item.get_level())  )

        #-----------------------
        for i in range(total_layers-1): # -1 for  not output level
            for j in range(len(nodes)): # find nodes in current layer
                if nodes[j].get_level() == i: # find nodes in current layer
                    for k in range(len(nodes)): # search all nodes to find connections to next level
                        if nodes[k].get_level() == i+1: # found next level
                            if nodes[k].get_is_bias_unit() == False: # not a bias node
                                #there is a connection from nodes[j] to nodes[k]
                                #----
                                range_min = 0
                                range_max = 1
                                init_epsilon = math.sqrt(6) / (math.sqrt(num_of_features) + 1)
                                rand = range_min + (range_max - range_min) * random.random()
                                rand = rand * (2 * init_epsilon ) - init_epsilon
                                #----
                                
                                weight = Weight()
                                weight.set_weight_index(weight_index)
                                weight.set_from_index(nodes[j].get_index()) # current level
                                weight.set_to_index(nodes[k].get_index()) # next level
                                weight.set_value(rand)
                                weight_index = weight_index + 1
                                weights.append(weight)
                                print("from ", str(nodes[j].get_label())+ " to " + str(nodes[k].get_label() + ": " + str(rand)))
                            
            
        return weights
    
