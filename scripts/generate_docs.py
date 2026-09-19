import ast
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
DOCS = ROOT / "docs"

INDEX_FILE = DOCS / "index.md"
USAGE_FILE = DOCS / "usage.md"


def get_python_files():
    """Find all Python source files inside src/."""
    if not SRC.exists():
        return []

    return sorted(SRC.rglob("*.py"))


def analyze_file(file_path):
    """Extract useful documentation information from a Python file."""
    try:
        source = file_path.read_text(encoding="utf-8")
        tree = ast.parse(source)
    except Exception as error:
        print(f"Could not analyze {file_path}: {error}")
        return None

    functions = []
    classes = []
    imports = []

    module_docstring = ast.get_docstring(tree)

    for node in tree.body:

        # Functions
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            functions.append({
                "name": node.name,
                "docstring": ast.get_docstring(node),
                "arguments": [
                    arg.arg
                    for arg in node.args.args
                ],
            })

        # Classes
        elif isinstance(node, ast.ClassDef):
            class_info = {
                "name": node.name,
                "docstring": ast.get_docstring(node),
                "methods": [],
            }

            for child in node.body:
                if isinstance(
                    child,
                    (ast.FunctionDef, ast.AsyncFunctionDef)
                ):
                    class_info["methods"].append({
                        "name": child.name,
                        "docstring": ast.get_docstring(child),
                        "arguments": [
                            arg.arg
                            for arg in child.args.args
                        ],
                    })

            classes.append(class_info)

        # Imports
        elif isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)

        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.append(node.module)

    return {
        "file": file_path.relative_to(ROOT).as_posix(),
        "module_docstring": module_docstring,
        "functions": functions,
        "classes": classes,
        "imports": sorted(set(imports)),
    }


def analyze_project():
    """Analyze all Python files in src/."""
    results = []

    for file_path in get_python_files():
        result = analyze_file(file_path)

        if result:
            results.append(result)

    return results


def clean_description(text):
    """Turn a docstring into a short readable description."""
    if not text:
        return None

    lines = [
        line.strip()
        for line in text.strip().splitlines()
        if line.strip()
    ]

    if not lines:
        return None

    return " ".join(lines)


def generate_index(project):
    """Generate the MkDocs home page."""
    project_name = ROOT.name.replace("-", " ").replace("_", " ").title()

    lines = []

    lines.append(f"# {project_name}")
    lines.append("")

    lines.append(
        "This documentation is automatically generated from "
        "the project's source code."
    )
    lines.append("")

    lines.append("## Project Overview")
    lines.append("")

    descriptions_found = False

    for file_info in project:
        description = clean_description(
            file_info["module_docstring"]
        )

        if description:
            descriptions_found = True

            lines.append(
                f"### `{file_info['file']}`"
            )
            lines.append("")
            lines.append(description)
            lines.append("")

    if not descriptions_found:
        lines.append(
            "The project contains Python source files "
            "documented using Python docstrings."
        )
        lines.append("")

    lines.append("## Source Files")
    lines.append("")

    if project:

        for file_info in project:

            lines.append(
                f"- `{file_info['file']}`"
            )

    else:
        lines.append("No Python source files were found.")

    lines.append("")

    lines.append("## Available Functions")
    lines.append("")

    functions_found = False

    for file_info in project:

        if file_info["functions"]:

            functions_found = True

            lines.append(
                f"### `{file_info['file']}`"
            )
            lines.append("")

            for function in file_info["functions"]:

                description = clean_description(
                    function["docstring"]
                )

                if description:
                    lines.append(
                        f"- **`{function['name']}()`** — "
                        f"{description}"
                    )
                else:
                    lines.append(
                        f"- **`{function['name']}()`**"
                    )

            lines.append("")

    if not functions_found:
        lines.append(
            "No top-level functions were found."
        )
        lines.append("")

    lines.append("## Classes")
    lines.append("")

    classes_found = False

    for file_info in project:

        if file_info["classes"]:

            classes_found = True

            lines.append(
                f"### `{file_info['file']}`"
            )
            lines.append("")

            for class_info in file_info["classes"]:

                description = clean_description(
                    class_info["docstring"]
                )

                if description:
                    lines.append(
                        f"- **`{class_info['name']}`** — "
                        f"{description}"
                    )
                else:
                    lines.append(
                        f"- **`{class_info['name']}`**"
                    )

            lines.append("")

    if not classes_found:
        lines.append(
            "No classes were found."
        )
        lines.append("")

    lines.append(
        "Technical API documentation is available "
        "through the Doxygen documentation."
    )
    lines.append("")

    INDEX_FILE.write_text(
        "\n".join(lines),
        encoding="utf-8"
    )

    print(
        f"Generated: {INDEX_FILE}"
    )


def generate_usage(project):
    """Generate usage documentation from source-code docstrings."""
    project_name = ROOT.name.replace("-", " ").replace("_", " ").title()

    lines = []

    lines.append("# Usage")
    lines.append("")

    lines.append(
        f"This page describes the available functions and "
        f"classes in **{project_name}**."
    )
    lines.append("")

    if not project:
        lines.append(
            "No Python source files were found."
        )
        lines.append("")

    for file_info in project:

        lines.append(
            f"## `{file_info['file']}`"
        )
        lines.append("")

        description = clean_description(
            file_info["module_docstring"]
        )

        if description:
            lines.append(description)
            lines.append("")

        # Functions
        for function in file_info["functions"]:

            lines.append(
                f"### `{function['name']}()`"
            )
            lines.append("")

            description = clean_description(
                function["docstring"]
            )

            if description:
                lines.append(description)
                lines.append("")
            else:
                lines.append(
                    "No description was provided."
                )
                lines.append("")

            if function["arguments"]:

                lines.append("**Parameters:**")
                lines.append("")

                for argument in function["arguments"]:

                    lines.append(
                        f"- `{argument}`"
                    )

                lines.append("")

            lines.append("**Example:**")
            lines.append("")

            arguments = function["arguments"]

            if arguments:
                example_arguments = ", ".join(
                    ["value" for _ in arguments]
                )

                lines.append("```python")
                lines.append(
                    f"{function['name']}({example_arguments})"
                )
                lines.append("```")
            else:
                lines.append("```python")
                lines.append(
                    f"{function['name']}()"
                )
                lines.append("```")

            lines.append("")

        # Classes
        for class_info in file_info["classes"]:

            lines.append(
                f"### Class `{class_info['name']}`"
            )
            lines.append("")

            description = clean_description(
                class_info["docstring"]
            )

            if description:
                lines.append(description)
                lines.append("")

            if class_info["methods"]:

                lines.append("#### Methods")
                lines.append("")

                for method in class_info["methods"]:

                    method_description = clean_description(
                        method["docstring"]
                    )

                    if method_description:
                        lines.append(
                            f"- **`{method['name']}()`** — "
                            f"{method_description}"
                        )
                    else:
                        lines.append(
                            f"- **`{method['name']}()`**"
                        )

                lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(
        "For detailed API information, see the "
        "automatically generated Doxygen documentation."
    )
    lines.append("")

    USAGE_FILE.write_text(
        "\n".join(lines),
        encoding="utf-8"
    )

    print(
        f"Generated: {USAGE_FILE}"
    )


def main():
    DOCS.mkdir(exist_ok=True)

    project = analyze_project()

    print(
        f"Found {len(project)} Python source file(s)."
    )

    generate_index(project)
    generate_usage(project)

    print("Documentation generation completed.")


if __name__ == "__main__":
    main()