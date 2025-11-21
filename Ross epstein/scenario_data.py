from scenario import ScenarioMoral, ScenarioNormal
from graph import Graph, GraphNode

game_graph = Graph()

start_key = "start"
start_node = GraphNode(scenario=ScenarioNormal(
    prompt="a dragon swops down how do you survive",
    options=[
        "hide in basement",
        "escape into the forest"
    ]
))
game_graph.add_node(id=start_key, node=start_node)

arrive_at_forest_key = "arrive at forest"
arrive_at_forest_node = GraphNode(scenario=ScenarioNormal(
    prompt="you enter the forest wat do you do now",
    options=[
        "find help",
        "search for weapon"
    ]
))
game_graph.add_node(id=arrive_at_forest_key, node=arrive_at_forest_node)


game_graph.add_edge(from_id=start_key, to_id=arrive_at_forest_key)