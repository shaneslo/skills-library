#!/usr/bin/env python3
"""Build the catalog, then serve dist/ over HTTP for local review.

Usage:
    python build/serve.py            # build, then serve on :8000
    python build/serve.py --port 9000
    python build/serve.py --no-build # serve the existing dist/ as-is

The page is a single offline HTML file. Serving it over HTTP is only a
convenience for review in a browser; the file itself loads nothing external.
"""
import argparse
import functools
import http.server
import socketserver
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DIST = REPO / "dist"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--no-build", action="store_true", help="skip the build step")
    args = parser.parse_args()

    if not args.no_build:
        result = subprocess.run([sys.executable, str(REPO / "build" / "build.py")])
        if result.returncode != 0:
            return result.returncode

    index = DIST / "skills-library.html"
    if not index.exists():
        print(f"No build at {index}. Run without --no-build first.", file=sys.stderr)
        return 1

    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(DIST))
    with socketserver.TCPServer(("0.0.0.0", args.port), handler) as httpd:
        url = f"http://localhost:{args.port}/skills-library.html"
        print(f"Serving {DIST} at {url}")
        print("Ctrl-C to stop.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
