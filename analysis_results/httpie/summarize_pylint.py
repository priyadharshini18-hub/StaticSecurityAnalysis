import os
import re

def read_file(path):
    for enc in ["utf-8", "utf-16", "latin-1"]:
        with open(path, "r", encoding=enc, errors="ignore") as f:
                return f.read()
    raise RuntimeError(f"Cannot read file {path}")

content = read_file("pylint_security.txt")

issue_patterns = {
    "broad-exception-caught": r"\(broad-exception-caught\)",
    "subprocess-run-check": r"\(subprocess-run-check\)",
    "eval-used": r"\(eval-used\)",
    "exec-used": r"\(exec-used\)",
    "deprecated-module": r"\(deprecated-module\)",
}

issue_counts = {k: len(re.findall(v, content)) for k, v in issue_patterns.items()}
total_issues = sum(issue_counts.values())

def count_python_files(path="."):
    py_files = []
    for root, _, files in os.walk(path):
        for f in files:
            if f.endswith(".py"):
                py_files.append(os.path.join(root, f))
    return py_files

project_path = "httpie"  
py_files = count_python_files(project_path)
total_files = len(py_files)

loc = 0
for file in py_files:
    try:
        with open(file, encoding="utf-8", errors="ignore") as fp:
            loc += sum(1 for _ in fp)
    except Exception:
        pass

print("Preliminary Results from Pylint")
print("Code scanned:")
print(f"\tTotal files scanned: {total_files}")
print(f"\tTotal lines of code: {loc}\n")

print("Run metrics:")
print("\tTotal issues (by type):")
for k, v in issue_counts.items():
    print(f"\t\t{k}: {v}")
print(f"\tTotal issues: {total_issues}")
