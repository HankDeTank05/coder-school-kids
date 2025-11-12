from scenario import ScenarioMoral, ScenarioNormal

start = ScenarioNormal(
    prompt="a dragon swops down how do you survive",
    options=[
        "hide in basement",
        "escape into the forest"
    ]
)

arrive_at_foest = ScenarioNormal(
    prompt="you enter the forest wat do you do now",
    options=[
        "find help",
        "search for weapon"
    ]
)