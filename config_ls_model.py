from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel


class Model(BaseModel):
    #def __init__(self, *args, **kwargs):
        #super().__init__(args, kwargs)
        #self.target_path = None

    source_folder_path: Path
    target_file_path: Path
