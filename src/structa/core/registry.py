from structa.paradigms.ddd import DDDParadigm


class ParadigmRegistry:
    def __init__(self):
        self._paradigms = {}

    def register(self, paradigm):
        self._paradigms[paradigm.name] = paradigm

    def get(self, name):
        return self._paradigms.get(name)

    def list(self):
        return list(self._paradigms.keys())


registry = ParadigmRegistry()

registry.register(DDDParadigm())
