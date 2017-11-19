class Node:
    def get_index(self):
        return self.__index

    def set_index(self, index):
        self.__index = index

    def get_label(self):
        return self.__label

    def set_label(self, label):
        self.__label = label


    def get_is_bias_unit(self):
        return self.__is_bias_unit


    def set_is_bias_unit(self, is_bias_unit):
        self.__is_bias_unit = is_bias_unit


    #---------------------------
    
    def get_level(self):
        return self.__level

    def set_level(self, level):
        self.__level = level
    #---------------------------

    def get_net_input_value(self):
        return self.__net_input_value

    def set_net_input_value(self, net_input_value):
        self.__net_input_value = net_input_value

    def get_net_value(self):
        return self.__net_value

    def set_net_value(self, net_value):
        self.__net_value = net_value