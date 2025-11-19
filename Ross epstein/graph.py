from scenario import ScenarioMoral, ScenarioNormal

class GraphNode:

    def __init__(self, scenario: ScenarioNormal | ScenarioMoral):
        self._scenario = scenario

class Graph:
    
    def __init__(self):
        #             key type    val type
        #                 vvv  vvvvvvvvv
        self._nodes: dict[str, GraphNode] = {}
        # INFO ABOUT self._nodes
        # THE KEY IS a unique string id associated with a node (the value)
        # THE VALUE IS the associated node
        
        #             key type    val type
        #                 vvv  vvvvvvvvv
        self._edges: dict[str, list[str]] = {}
        # INFO ABOUT self._edges
        # THE KEY IS a unique string id for the source node (the node you're coming FROM)
        # THE VALUE IS a list of unique string id's for the destination node(s) (the node(s) you can go TO)

    def add_node(self, id: str, node: GraphNode):
        assert(id not in self._nodes.keys()) # make sure id is a unique key in self._nodes
        assert(id not in self._edges.keys()) # make sure id is a unique key in self._edges
        self._nodes[id] = node # creates an entry in the self._nodes dict: (key=id, value=node)
        self._edges[id] = [] # creates an entry in the self._edges dict: (key=id, value=empty list)

    def add_edge(self, from_id: str, to_id: str):
        assert(from_id in self._edges.keys()) # make sure from_id has an entry in the self._edges dictionary
        assert(to_id in self._nodes.keys()) # make sure to_id has an entry in the self._nodes dictionary
        assert(to_id not in self._edges[from_id]) # make sure that a connection from_id --> to_id does NOT already exist
        self._edges[from_id].append(to_id) # adds the following edge to the graph: from_id --> to_id

