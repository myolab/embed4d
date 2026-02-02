"""
Launch the embed4d FastAPI server to serve the 3D viewer over HTTP.

Run:
    python examples/demo_server.py
    python examples/demo_server.py --port 8080
    python examples/demo_server.py --port 8080 --model path/to/motion.glb

Requires: pip install embed4d  (fastapi/uvicorn are core dependencies)
"""

import argparse

from embed4d.viewer_server import launch

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="embed4d FastAPI viewer server")
    parser.add_argument("--port", type=int, default=None, help="Port (default: auto)")
    parser.add_argument(
        "--model", type=str, default=None, help="Path to GLB/GLTF/FBX file"
    )
    args = parser.parse_args()
    url = launch(port=args.port, model_file=args.model)
    print(f"Viewer at: {url}")
    try:
        import time

        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
