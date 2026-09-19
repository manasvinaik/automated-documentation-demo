import ast
import os
from pathlib import Path


# Project root
ROOT = Path(__file__).resolve().parent.parent

# Source directory
SRC = ROOT / "src"

# Output README
README = ROOT / "README.md"


def get_project_name():
    """Get the project name from the repository folder name."""
    return ROOT.name.replace("-", " ").replace("_", " ").title()


def get_python_files():
    """Find all Python files inside the source directory."""
    if not SRC.exists():
        return []

    return sorted(SRC.rglob("*.py"))


def analyze_python_file(file_path):
    """Extract useful documentation information from a Python file."""

    try:
        source = file_path.read_text(encoding="utf-8")
        tree = ast.parse(source)
    except Exception as error:
        print(f"Could not analyze {file_path}: {error}")
        return None

    module_docstring = ast.get_docstring(tree)

    functions = []
    classes = []

    for node in tree.body:

        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            functions.append(node.name)

        elif isinstance(node, ast.ClassDef):
            classes.append(node.name)

            # Also document methods inside classes
            for child in node.body:
                if isinstance(
                    child,
                    (ast.FunctionDef, ast.AsyncFunctionDef)
                ):
                    functions.append(f"{node.name}.{child.name}")

    return {
        "file": file_path.relative_to(ROOT).as_posix(),
        "module_docstring": module_docstring,
        "functions": functions,
        "classes": classes,
    }


def get_project_structure():
    """Get important files and directories in the project."""

    ignored = {
        ".git",
        ".github",
        "__pycache__",
        "site",
        "doxygen",
        ".pytest_cache",
    }

    structure = []

    for path in sorted(ROOT.rglob("*")):

        if not path.is_file():
            continue

        relative = path.relative_to(ROOT)

        # Skip files inside ignored directories
        if any(part in ignored for part in relative.parts):
            continue

        structure.append(relative.as_posix())

    return structure


def get_dependencies():
    """Detect common dependency files."""

    dependencies = []

    requirements = ROOT / "requirements.txt"

    if requirements.exists():
        try:
            packages = []

            for line in requirements.read_text(
                encoding="utf-8"
            ).splitlines():

                line = line.strip()

                if line and not line.startswith("#"):
                    packages.append(line)

            if packages:
                dependencies.append(
                    ("Python", packages)
                )

        except Exception:
            pass

    package_json = ROOT / "package.json"

    if package_json.exists():
        dependencies.append(
            ("Node.js", ["package.json"])
        )

    return dependencies


def generate_readme():
    """Generate README content from the actual project."""

    project_name = get_project_name()

    python_files = get_python_files()

    analyzed_files = []

    for file_path in python_files:
        result = analyze_python_file(file_path)

        if result:
            analyzed_files.append(result)

    structure = get_project_structure()
    dependencies = get_dependencies()

    lines = []

    # ---------------------------------------------------------
    # TITLE
    # ---------------------------------------------------------

    lines.append(f"# {project_name}")
    lines.append("")

    # ---------------------------------------------------------
    # OVERVIEW
    # ---------------------------------------------------------

    lines.append("## Overview")
    lines.append("")

    module_descriptions = []

    for file_info in analyzed_files:

        if file_info["module_docstring"]:
            description = file_info["module_docstring"].strip()

            module_descriptions.append(
                f"**{file_info['file']}** — {description}"
            )

    if module_descriptions:
        lines.extend(module_descriptions)
    else:
        lines.append(
            "This project contains source code that is "
            "automatically documented using Doxygen and MkDocs."
        )

    lines.append("")

    # ---------------------------------------------------------
    # SOURCE FILES
    # ---------------------------------------------------------

    lines.append("## Source Files")
    lines.append("")

    if analyzed_files:

        for file_info in analyzed_files:

            lines.append(
                f"### `{file_info['file']}`"
            )
            lines.append("")

            if file_info["functions"]:

                lines.append("**Functions / Methods:**")
                lines.append("")

                for function in file_info["functions"]:
                    lines.append(f"- `{function}()`")

                lines.append("")

            if file_info["classes"]:

                lines.append("**Classes:**")
                lines.append("")

                for class_name in file_info["classes"]:
                    lines.append(f"- `{class_name}`")

                lines.append("")

    else:
        lines.append(
            "No Python source files were found in the `src` directory."
        )
        lines.append("")

    # ---------------------------------------------------------
    # PROJECT STRUCTURE
    # ---------------------------------------------------------

    lines.append("## Project Structure")
    lines.append("")

    lines.append("```text")

    for item in structure:
        lines.append(item)

    lines.append("```")
    lines.append("")

    # ---------------------------------------------------------
    # DEPENDENCIES
    # ---------------------------------------------------------

    lines.append("## Dependencies")
    lines.append("")

    if dependencies:

        for dependency_type, packages in dependencies:

            lines.append(f"### {dependency_type}")
            lines.append("")

            for package in packages:
                lines.append(f"- `{package}`")

            lines.append("")

    else:
        lines.append(
            "No dependency configuration files were detected."
        )
        lines.append("")

    # ---------------------------------------------------------
    # DOCUMENTATION
    # ---------------------------------------------------------

    lines.append("## Documentation")
    lines.append("")

    lines.append(
        "This project uses automated documentation generation."
    )
    lines.append("")

    lines.append(
        "- **Doxygen** generates technical documentation "
        "from source-code documentation."
    )

    lines.append(
        "- **MkDocs** builds the documentation website."
    )

    lines.append(
        "- **GitHub Actions** automatically regenerates "
        "the documentation when changes are pushed."
    )

    lines.append(
        "- **GitHub Pages** publishes the generated documentation."
    )

    lines.append("")

    # ---------------------------------------------------------
    # WRITE README
    # ---------------------------------------------------------

    README.write_text(
        "\n".join(lines),
        encoding="utf-8"
    )

    print(f"README generated successfully: {README}")


if __name__ == "__main__":
    generate_readme()