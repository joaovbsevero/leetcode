from enum import StrEnum

import typer


class Modules(StrEnum):
    TRAPPING_WATER = "trapping_water"
    MEDIAN_OF_TWO_SORTED_ARRAYS = "median_of_two_sorted_arrays"
    SIMPLE_REGEX = "simple_regex"


def main(module_name: Modules):
    """
    Run the specified module with the provided test cases.

    Args:
        module_name: The name of the module to run.
    """

    match module_name:
        case Modules.TRAPPING_WATER:
            from . import trapping_water

            module = trapping_water
        case Modules.MEDIAN_OF_TWO_SORTED_ARRAYS:
            from . import median_of_two_sorted_arrays

            module = median_of_two_sorted_arrays
        case Modules.SIMPLE_REGEX:
            from . import simple_regex

            module = simple_regex
        case _:
            raise ValueError(f"Unknown module: {module_name}")

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
