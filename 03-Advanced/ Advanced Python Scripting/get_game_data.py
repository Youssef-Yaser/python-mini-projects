import os
import json
import shutil
from subprocess import PIPE, run
import sys

GAME_DIR_PATTERN = "game"
GAME_CODE_EXTENSION = ".go"
GAME_COMPILE_COMMAND = ["go", "build"]


def find_all_game_paths(source):
    game_paths = []

    for root, dirs, files in os.walk(source):
        for directory in dirs:
            if GAME_DIR_PATTERN in directory.lower():
                game_paths.append(os.path.join(root, directory))

    return game_paths


def get_name_from_paths(paths, to_strip):
    new_names = []

    for path in paths:
        _, dir_name = os.path.split(path)

        name = dir_name.replace(to_strip, "")
        name = name.replace("_", " ").strip()

        new_names.append(name)

    return new_names


def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def copy_and_overwrite(source, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)

    shutil.copytree(source, dest)


def make_json_metadata_file(path, game_dirs):
    data = {
        "gameNames": game_dirs,
        "numberOfGames": len(game_dirs)
    }

    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    print("Metadata created:", path)


def is_go_installed():
    """Check if Go compiler is available."""
    try:
        result = run(["go", "version"], stdout=PIPE, stderr=PIPE, universal_newlines=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False


def compile_game_code(path):
    if not is_go_installed():
        print("⚠️  Go compiler not found. Skipping compilation for:", path)
        return

    code_file_name = None

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(GAME_CODE_EXTENSION):
                code_file_name = file
                break
        break

    if code_file_name is None:
        print("No Go file found in", path)
        return

    command = GAME_COMPILE_COMMAND + [code_file_name]
    run_command(command, path)


def run_command(command, path):
    cwd = os.getcwd()
    os.chdir(path)

    result = run(
        command,
        stdout=PIPE,
        stderr=PIPE,
        universal_newlines=True
    )

    if result.returncode == 0:
        print("Compiled successfully in", path)
    else:
        print("Compile error in", path)
        print(result.stderr)

    os.chdir(cwd)


def main(source, target):

    source_path = os.path.abspath(source)
    target_path = os.path.abspath(target)

    game_paths = find_all_game_paths(source_path)

    if not game_paths:
        print("No game folders found.")
        return

    new_game_dirs = get_name_from_paths(game_paths, "_game")

    create_dir(target_path)

    for src, dest in zip(game_paths, new_game_dirs):
        dest_path = os.path.join(target_path, dest)

        print(f"\nCopying {src} -> {dest_path}")
        copy_and_overwrite(src, dest_path)

        print("Compiling...")
        compile_game_code(dest_path)

    json_path = os.path.join(target_path, "metadata.json")
    make_json_metadata_file(json_path, new_game_dirs)

    print("\nAll done ✅")


if __name__ == "__main__":

    if len(sys.argv) != 3:
        raise Exception("Usage: python script.py <source_dir> <target_dir>")

    source, target = sys.argv[1:]
    main(source, target)
