class Weight:
    def get_weight_index(self): # this id
        return self.__weight_index
    
    def set_weight_index(self, weight_index): # this id
        self.__weight_index = weight_index

    def get_from_index(self): # from node id
        return self.__from_node_index
    
    def set_from_index(self, from_node_index): # from node id
        self.__from_node_index = from_node_index

    def get_to_index(self): # to node id
        return self.__to_node_index
    
    def set_to_index(self, to_node_index): # to node id
        self.__to_node_index = to_node_index

    def get_value(self): # weight value
        return self.__value
    
    def set_value(self, value): # weight value
        self.__value = value
