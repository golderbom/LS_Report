from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel


class Model(BaseModel):
    source_path: Path
    target_path: Path
