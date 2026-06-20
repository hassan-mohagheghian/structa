from pathlib import Path
import typer

from structa.core.engine import StructaEngine

app = typer.Typer()
engine = StructaEngine()


@app.command()
def init(path: str, architecture: str = "modular-monolith-ddd-cqrs"):
    cwd = Path.cwd()
    project_root = cwd / path if path != "." else cwd

    preset = engine.resolve(architecture)

    # create base directories
    gen = engine
    gen.generate(
        root=project_root,
        structure=preset.structure,
        patterns=preset.patterns,
    )

    # config file
    (project_root / "structa.toml").write_text(f"""[architecture]
structure = "{preset.structure}"

[patterns]
ddd = {"true" if "ddd" in preset.patterns else "false"}
cqrs = {"true" if "cqrs" in preset.patterns else "false"}
""")

    typer.echo(
        f"Initialized project at {project_root} "
        f"with {preset.structure} + {preset.patterns}"
    )


@app.command()
def paradigms():
    for name in engine.list_presets():
        typer.echo(name)


@app.command()
def version():
    typer.echo("Structa v0.1.0")
