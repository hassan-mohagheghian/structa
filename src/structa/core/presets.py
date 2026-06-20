from dataclasses import dataclass


@dataclass
class ArchitecturePreset:
    structure: str
    patterns: list[str]


PRESETS = {
    "modular-monolith-ddd-cqrs": ArchitecturePreset(
        structure="modular-monolith",
        patterns=["ddd", "cqrs"],
    ),
    "modular-monolith-ddd": ArchitecturePreset(
        structure="modular-monolith",
        patterns=["ddd"],
    ),
    "modular-monolith-cqrs": ArchitecturePreset(
        structure="modular-monolith",
        patterns=["cqrs"],
    ),
}


def resolve_preset(name: str) -> ArchitecturePreset:
    if name in PRESETS:
        return PRESETS[name]

    # fallback: treat raw input as structure only
    return ArchitecturePreset(structure=name, patterns=[])
