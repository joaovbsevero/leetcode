import importlib
import os
from enum import StrEnum
from typing import TYPE_CHECKING

import typer

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


def main(module_name: Modules):
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
        result = module.run(*args)  # type: ignore
        if result != expected:
            results.append(f"{args} => {result} != {expected}")

    if results:
        text = typer.style("Failed", fg=typer.colors.RED)
        typer.echo(f"{text}, results:\n")
        for result in results:
            typer.echo(f"   - {result}\n")
    else:
        typer.secho("Passed", fg=typer.colors.GREEN)


if __name__ == "__main__":
    typer.run(main)
