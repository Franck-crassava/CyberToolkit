import argparse
import subprocess
import os
import sys

MODULES_DIR = "modules"

def list_modules():
    modules = [name for name in os.listdir(MODULES_DIR)
               if os.path.isdir(os.path.join(MODULES_DIR, name))]
    return modules

def run_module(module_name, args):
    module_path = os.path.join(MODULES_DIR, module_name)
    script_path = os.path.join(module_path, f"{module_name.replace('-', '_')}.py")

    if not os.path.exists(script_path):
        print(f"❌ Module '{module_name}' not found or missing main script.")
        sys.exit(1)

    # Pass CLI args to the module script
    command = [sys.executable, script_path] + args
    subprocess.run(command)

def main():
    parser = argparse.ArgumentParser(
        description="🛠️ CyberToolkit - Modular Cybersecurity CLI Toolkit"
    )
    parser.add_argument("module", help="Module name to run (e.g. password-generator)")
    parser.add_argument("module_args", nargs=argparse.REMAINDER, help="Arguments for the module")

    args = parser.parse_args()

    available = list_modules()
    if args.module not in available:
        print(f"❌ Unknown module '{args.module}'. Available modules:")
        for mod in available:
            print(f"  - {mod}")
        sys.exit(1)

    run_module(args.module, args.module_args)

if __name__ == "__main__":
    main()

