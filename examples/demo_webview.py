"""
Open the embed4d viewer in a native desktop window (pywebview).

Run: python examples/demo_webview.py [model.glb]
Requires: pip install embed4d  (pywebview is a core dependency)
"""

import sys

from embed4d import open_viewer_webview

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else None
    open_viewer_webview(path, title="embed4d Viewer")
