from pydantic import BaseModel
from typing import Optional, Dict, Any

class LegacyOpsAction(BaseModel):
    command: str = ""
    target: str = ""

class LegacyOpsObservation(BaseModel):
    cwd: str
    stdout: str
    stderr: str
    current_phase: int
    done: bool
    reward: float
    metadata: Optional[Dict[str, Any]] = None