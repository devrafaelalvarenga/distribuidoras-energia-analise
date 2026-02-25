from __future__ import annotations

from typing import Dict
from distribuidoras_energia_analise.ingestion.sources.base import Fetcher


class SourceRegistry:
    def __init__(self) -> None:
        self._fetchers: Dict[str, Fetcher] = {}

    def register(self, source_type: str, fetcher: Fetcher) -> None:
        self._fetchers[source_type] = fetcher

    def get(self, source_type: str) -> Fetcher:
        if source_type not in self._fetchers:
            available = ", ".join(sorted(self._fetchers.keys()))
            raise KeyError(f"Fonte '{source_type}' não registrada. Disponíveis: {available}")
        return self._fetchers[source_type]
