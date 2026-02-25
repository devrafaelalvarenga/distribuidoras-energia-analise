from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Protocol
import pandas as pd


@dataclass(frozen=True)
class SourceConfig:
    type: str
    dataset: str
    options: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class SourceInfo:
    source_type: str
    dataset: str
    origin: str
    request: Dict[str, Any]
    notes: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class FetchResult:
    df: pd.DataFrame
    info: SourceInfo


class Fetcher(Protocol):
    def fetch(self, config: SourceConfig) -> FetchResult: ...
