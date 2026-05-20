import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from main import app  # noqa: E402

output = ROOT / "openapi.json"
output.write_text(json.dumps(app.openapi(), indent=2) + "\n")
print(f"Wrote {output}")
