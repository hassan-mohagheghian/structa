from pathlib import Path

from structa.core.generator import ProjectGenerator
from structa.core.presets import resolve_preset
from structa.core.presets import PRESETS


class StructaEngine:
    def __init__(self):
        pass

    def generate(self, root: Path, structure: str, patterns: list[str]):
        gen = ProjectGenerator(root)

        # 1. base structure
        if structure == "modular-monolith":
            gen.create_base_structure()

        # 2. default module (starter module)
        gen.create_module("core", patterns)

    def resolve(self, preset_name: str):
        return resolve_preset(preset_name)

    def list_presets(self):
        return list(PRESETS.keys())
