import importlib
import json
import os
import subprocess
from copy import deepcopy
from enum import StrEnum
from pathlib import Path
from typing import TYPE_CHECKING

import typer

app = typer.Typer(add_completion=False)

enum_variants = "    "
for file in os.scandir("./leetcode"):
    if file.is_file() and file.name.endswith(".py") and not file.name.startswith("__"):
        clean_file_name = file.name.removesuffix(".py")
        enum_variants += f'{clean_file_name.upper()} = "{clean_file_name}"\n    '


exec(f"""
class Modules(StrEnum):
{enum_variants}pass
""")

if TYPE_CHECKING:

    class Modules(StrEnum):
        pass


@app.command()
def run(module_name: Modules):
    """
    Run the specified module with the provided test cases.

    Args:
        module_name: The name of the module to run.
    """

    try:
        module = importlib.import_module(f"leetcode.{module_name}")
    except ImportError:
        raise ValueError(
            f"Unknown module: {module_name}, supported modules are:\n -> "
            + "\n -> ".join(Modules.__members__)
        )

    typer.echo(f"Testing '{module_name}'")
    results = []
    for args, expected in module.test_cases():
        result = module.run(*deepcopy(args))  # type: ignore
        if result != expected:
            results.append(f"{args} => {result} != {expected}")

    if results:
        text = typer.style("Failed", fg=typer.colors.RED)
        typer.echo(f"{text}, results:\n")
        for result in results:
            typer.echo(f"   - {result}\n")
    else:
        typer.secho("Passed", fg=typer.colors.GREEN)


@app.command()
def sync():
    command = ["git", "ls-files", "-o", "--exclude-standard"]
    result = subprocess.run(command, stdout=subprocess.PIPE)
    string = result.stdout.decode("utf-8").strip()
    if not string:
        typer.secho("Synced", fg=typer.colors.GREEN)
        return

    file_path = Path(__file__).parents[1] / ".vscode" / "launch.json"
    with open(file_path) as f:
        data = json.load(f)

    for new_file in string.split("\n"):
        if not new_file.startswith("leetcode/"):
            continue
        if not new_file.endswith(".py"):
            continue

        script_name = new_file.removeprefix("leetcode/").removesuffix(".py")
        data["configurations"].append(
            {
                "name": " ".join(script_name.split("_")).title(),
                "type": "debugpy",
                "request": "launch",
                "module": "leetcode",
                "args": ["run", script_name],
            }
        )

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

    typer.secho("Synced", fg=typer.colors.GREEN)


if __name__ == "__main__":
    app()
