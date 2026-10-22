"""Build the book locally with code execution.

Why this script: on some Windows machines `jupyter-book build --execute` fails with
"fetch failed" because Node resolves `localhost` to IPv6 while the Jupyter server
it starts listens on IPv4. Here we start the Jupyter server ourselves on
127.0.0.1 and pass its address to Jupyter Book via JUPYTER_BASE_URL/JUPYTER_TOKEN.

Usage (from the repository root, inside the virtual environment):
    python code/build_local.py          # static HTML in _build/html
    python code/build_local.py start    # live preview at http://localhost:3000
"""
import os
import secrets
import shutil
import socket
import subprocess
import sys
import time
import urllib.request


def free_port() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def main() -> int:
    mode = sys.argv[1] if len(sys.argv) > 1 else "build"
    port, token = free_port(), secrets.token_hex(16)
    server = subprocess.Popen(
        [sys.executable, "-m", "jupyter_server", "--ip=127.0.0.1", f"--port={port}",
         f"--IdentityProvider.token={token}", "--ServerApp.open_browser=False"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    try:
        url = f"http://127.0.0.1:{port}"
        for _ in range(60):  # wait until the server answers
            try:
                urllib.request.urlopen(f"{url}/api?token={token}", timeout=1)
                break
            except OSError:
                time.sleep(0.5)
        else:
            print("Jupyter server did not start", file=sys.stderr)
            return 1
        env = dict(os.environ, JUPYTER_BASE_URL=url, JUPYTER_TOKEN=token)
        # Look next to this interpreter first, so the venv need not be activated
        scripts = os.path.dirname(sys.executable)
        jb = shutil.which("jupyter-book", path=scripts) or shutil.which("jupyter-book") or "jupyter-book"
        args = [jb, "start", "--execute"] if mode == "start" else [jb, "build", "--execute", "--html"]
        return subprocess.call(args, env=env)
    finally:
        server.terminate()
        server.wait()


if __name__ == "__main__":
    sys.exit(main())
