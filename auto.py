import re
import os
import sys

SETUP_PY = "setup.py"
TEST_SCRIPT = "tests/test.py"
PACKAGE_NAME = "verahession"

def increment_version(version_str):
    parts = version_str.strip().split(".")
    if len(parts) != 3:
        print("Version format unexpected, expected '0.1.X'")
        sys.exit(1)
    parts[-1] = str(int(parts[-1]) + 1)
    return ".".join(parts)

def update_setup_version():
    with open(SETUP_PY, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.search(r'version\s*=\s*"(0\.1\.\d+)"', content)
    if not match:
        print("Version string not found in setup.py")
        sys.exit(1)
    old_version = match.group(1)
    new_version = increment_version(old_version)
    new_content = content.replace(f'version="{old_version}"', f'version="{new_version}"')
    with open(SETUP_PY, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Version updated: {old_version} -> {new_version}")
    return new_version

def run_command(cmd):
    print(f"Running: {cmd}")
    ret = os.system(cmd)
    if ret != 0:
        print(f"Command failed with exit code {ret}")
        sys.exit(ret)

def main():
    new_version = update_setup_version()

    run_command("rm -rf build dist *.egg-info")
    run_command("python3 setup.py sdist bdist_wheel")
    run_command("twine upload dist/*")

    run_command(f"python3 -m pip uninstall -y {PACKAGE_NAME}")
    run_command(f"python3 -m pip install --user --editable .")

    repo_root = os.getcwd()
    # Set PYTHONPATH for test run inline in shell
    run_command(f"PYTHONPATH={repo_root} python3 {TEST_SCRIPT}")

if __name__ == "__main__":
    main()
