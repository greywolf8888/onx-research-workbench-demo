from __future__ import annotations

import json
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

from demo_repository import candidates, kline

ROOT = Path(__file__).resolve().parents[2]


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT / "frontend"), **kwargs)

    def _json(self, payload: dict) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        path = urlparse(self.path).path
        if path == "/health":
            self._json({"ok": True, "mode": "sanitized-demo"})
            return
        if path == "/api/candidates":
            self._json(candidates())
            return
        if path.startswith("/api/kline/"):
            self._json(kline(path.rsplit("/", 1)[-1]))
            return
        return super().do_GET()


def main() -> None:
    server = ThreadingHTTPServer(("127.0.0.1", 8765), Handler)
    print("ONX Research Workbench Demo: http://127.0.0.1:8765/")
    server.serve_forever()


if __name__ == "__main__":
    main()
