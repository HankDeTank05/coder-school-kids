from player import Player
import interact

class Scenario:
    
    def __init__(self, prompt: str):
        self._prompt = prompt

class ScenarioNormal(Scenario):

    def __init__(self, prompt: str, options: list[str]):
        super().__init__(prompt)
        self._options = options

    def interact(self) -> str:
        return interact.prompt_for_input(self._prompt, self._options)

class ScenarioMoral(Scenario):

    def __init__(self, prompt: str, choice_evil: str, choice_neutral: str, choice_good: str):
        super().__init__(prompt)
        self._choice_evil = choice_evil
        self._choice_neutral = choice_neutral
        self._choice_good = choice_good

    def interact(self) -> float:
        return interact.moral_choice(self._prompt, self._choice_evil, self._choice_neutral, self._choice_good)
















