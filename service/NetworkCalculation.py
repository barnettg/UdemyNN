import math

class NetworkCalculation:
    def applyForwardPropogation(nodes, weights, instance):

        for j in range(len(nodes)):
            if nodes[j].get_is_bias_unit() == True:
                nodes[j].set_net_value(1)

        #instance = [0, 0, 0]

        # transfer input features to input layer
        for j in range(len(instance) - 1):
            var = instance[j]

            # itterate on all nodes
            for k in range(len(nodes)):
                if j+1 == nodes[k].get_index():
                    nodes[k].set_net_value(var)
        # -----------------------

        for j in range(len(nodes)): # 0 level is input and bias has no connection to prvious level
            if nodes[j].get_level() > 0 and nodes[j].get_is_bias_unit() == False:
                net_input = 0
                net_output = 0

                target_index = nodes[j].get_index()

                for k in range(len(weights)):

                    if target_index == weights[k].get_to_index():

                        wi = weights[k].get_value()

                        source_index = weights[k].get_from_index()

                        for m in range(len(nodes)):
                            if source_index == nodes[m].get_index():
                                xi = nodes[m].get_net_value()

                                net_input = net_input + (xi * wi)
                                break
                # ------------------------------
                net_output = 1 / (1 + math.exp(-net_input))
                nodes[j].set_net_input_value(net_input)
                nodes[j].set_net_value(net_input)



        return nodes