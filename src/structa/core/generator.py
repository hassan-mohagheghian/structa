from pathlib import Path


class ProjectGenerator:
    def __init__(self, root: Path):
        self.root = root

    # ----------------------------
    # STRUCTURE LAYER
    # ----------------------------
    def create_base_structure(self):
        (self.root / "shared" / "__init__.py").mkdir(parents=True, exist_ok=True)
        (self.root / "modules" / "__init__.py").mkdir(parents=True, exist_ok=True)
        (self.root / "__init__.py").touch(exist_ok=True)

    # ----------------------------
    # MODULE GENERATION
    # ----------------------------
    def create_module(self, name: str, patterns: list[str]):
        module = self.root / "modules" / name

        domain = module / "domain"
        app = module / "application"
        infra = module / "infrastructure"
        interface = module / "interface"

        domain.mkdir(parents=True, exist_ok=True)
        infra.mkdir(parents=True, exist_ok=True)
        interface.mkdir(parents=True, exist_ok=True)
        app.mkdir(parents=True, exist_ok=True)

        # DDD layer
        if "ddd" in patterns:
            (domain / "__init__.py").touch()
            (infra / "__init__.py").touch()
            (interface / "__init__.py").touch()

        # CQRS layer
        if "cqrs" in patterns:
            (app / "commands" / "__init__.py").mkdir(parents=True, exist_ok=True)
            (app / "queries" / "__init__.py").mkdir(parents=True, exist_ok=True)
        else:
            (app / "use_cases" / "__init__").mkdir(parents=True, exist_ok=True)
        # fallback marker
        (module / "__init__.py").touch()
