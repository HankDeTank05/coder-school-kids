from scenario import ScenarioMoral, ScenarioNormal

class Graph:
    pass

class GraphNode:

    def __init__(self, scenario: ScenarioNormal | ScenarioMoral):
        self._scenario = scenario
