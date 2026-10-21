"""Run every verification script in code/verify/ and fail if any check fails."""
import pathlib
import runpy
import sys

HERE = pathlib.Path(__file__).resolve().parent


def main() -> int:
    scripts = sorted(p for p in HERE.glob("verify_*.py"))
    failed = []
    for script in scripts:
        print(f"=== {script.name} ===")
        try:
            runpy.run_path(str(script), run_name="__main__")
        except SystemExit as exc:
            if exc.code not in (0, None):
                failed.append(script.name)
        except Exception as exc:  # report and continue with the other scripts
            print(f"ERROR: {exc!r}")
            failed.append(script.name)
    print()
    print(f"{len(scripts) - len(failed)}/{len(scripts)} scripts passed")
    if failed:
        print("FAILED:", ", ".join(failed))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
