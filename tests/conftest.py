import sys
from pathlib import Path

# Ensure `import embed4d` resolves when running tests
# from this folder.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
