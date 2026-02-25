from __future__ import annotations

from pathlib import Path
from typing import Any, Dict
import yaml

from distribuidoras_energia_analise.ingestion.sources.base import SourceConfig
from distribuidoras_energia_analise.ingestion.sources.registry import SourceRegistry
from distribuidoras_energia_analise.ingestion.sources.ckan_csv import CKANCsvFetcher


def build_registry() -> SourceRegistry:
    registry = SourceRegistry()
    registry.register("ckan_csv", CKANCsvFetcher())
    return registry


def load_sources_config(path: str | Path) -> Dict[str, SourceConfig]:
    p = Path(path)
    raw = yaml.safe_load(p.read_text(encoding="utf-8"))

    datasets = raw.get("datasets", {})
    out: Dict[str, SourceConfig] = {}

    for dataset_name, cfg in datasets.items():
        out[dataset_name] = SourceConfig(
            type=cfg["type"],
            dataset=dataset_name,
            options=cfg.get("options", {}),
        )

    return out
