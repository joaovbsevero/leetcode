# LeetCode Solutions Command Line Tool

This module provides a command line tool designed to run various problems solved from LeetCode, complete with test cases. The tool is structured to allow easy execution and testing of different algorithmic solutions.

## Getting Started:
Prerequisites:
- Python 3.12+ is required to run the scripts.
- [`typer`](https://pypi.org/project/typer) module must be installed into your environment


## Installation:
1. Clone the repository:
```sh
git clone https://github.com/joaovbsevero/leetcode
```

2. Navigate to the repository directory:
```sh
cd leetcode
```

3. Install dependencies:
```sh
pip install -r requirements.txt
```

4. Run a help command to list the available solutions:
```sh
python -m leetcode --help
```

5. Run a solution
```sh
python -m leetcode simple_regex
```

## Structure

Every python file inside `leetcode` folder has a documentation and reference to
the original challenge in LeetCode. Also, the functions are well documented explaining
the thought process behind the execution to allow easy understanding.

There is also a VSCode configuration to automatically run the challenges and debug them
if needed.


## Acknowledgments:
- LeetCode for providing a platform to practice coding problems.
- The open-source community for continuous support and contributions.
