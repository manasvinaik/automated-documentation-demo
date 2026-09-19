from pathlib import Path


PROJECT_NAME = "Automated Documentation Demo"

DESCRIPTION = """
A simple Python calculator project demonstrating automated
documentation generation using GitHub Actions, Doxygen, and MkDocs.
"""


FEATURES = [
    "Addition",
    "Subtraction",
    "Multiplication",
    "Division",
]


def generate_readme():
    readme = f"""# {PROJECT_NAME}

{DESCRIPTION.strip()}

## Features

"""

    for feature in FEATURES:
        readme += f"- {feature}\n"

    readme += """
## Installation

Make sure Python is installed on your system.

Clone the repository:

```bash
git clone <repository-url>
cd auto-documentation-demo
```
"""

    return readme


if __name__ == "__main__":
    output_path = Path(__file__).resolve().parent.parent / "README.md"
    output_path.write_text(generate_readme(), encoding="utf-8")
