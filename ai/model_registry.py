from typing import Dict


class ModelRegistry:
    def __init__(self):
        self._models: Dict[str, object] = {}

    def register(self, name: str, model: object):
        self._models[name] = model

    def get(self, name: str):
        if name not in self._models:
            raise KeyError(f"Model '{name}' is not registered.")
        return self._models[name]

    def exists(self, name: str):
        return name in self._models

    def list_models(self):
        return list(self._models.keys())