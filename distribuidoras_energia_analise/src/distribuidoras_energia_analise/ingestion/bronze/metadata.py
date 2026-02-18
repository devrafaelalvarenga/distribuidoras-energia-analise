from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import pandas as pd


@dataclass(frozen=True)
class BronzeMeta:
    dataset: str
    source_url: str
    extracted_at_utc: str
    row_count: int
    columns: list[str]
    dtypes: dict[str, str]
    file_name: str
    file_size_bytes: int
    file_sha256: str


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def build_and_write_meta(
    *,
    df: pd.DataFrame,
    dataset: str,
    source_url: str,
    data_file_path: Path,
    out_dir: Path,
) -> Path:
    """
    Monta e grava _meta.json na mesma partição (out_dir).
    """
    extracted_at_utc = datetime.now(timezone.utc).isoformat()

    meta = BronzeMeta(
        dataset=dataset,
        source_url=source_url,
        extracted_at_utc=extracted_at_utc,
        row_count=int(len(df)),
        columns=list(df.columns.astype(str)),
        dtypes={str(k): str(v) for k, v in df.dtypes.astype(str).to_dict().items()},
        file_name=data_file_path.name,
        file_size_bytes=data_file_path.stat().st_size,
        file_sha256=_sha256_file(data_file_path),
    )

    out_path = out_dir / "_meta.json"
    out_path.write_text(json.dumps(asdict(meta), ensure_ascii=False, indent=2), encoding="utf-8")
    return out_path
