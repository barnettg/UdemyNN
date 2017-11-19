from service.NetworkStructure import NetworkStructure
from service.NetworkConnection import NetworkConnection
from service.NetworkCalculation import NetworkCalculation

#             X1 X2  out  -> xor
instances = [[0, 0,   0], [0,1,1], [1,0,1], [1,1,0]]

num_of_features = len(instances[0]) -1 # inputs??

hidden_nodes = [3] # one hidden layer with 3 nodes

nodes = NetworkStructure.create_nodes(num_of_features, hidden_nodes)
#print("Nodes: " + str(nodes))

weights = NetworkConnection.create_weights(nodes, num_of_features, hidden_nodes)

for i in range(len(instances)):
    instance = instances[i]
    NetworkCalculation.applyForwardPropogation(nodes, weights, instance)

    print("actual: ", instance[len(instance)-1], " - prediction", nodes[len(nodes)-1].get_net_value())
