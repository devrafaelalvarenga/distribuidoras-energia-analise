from __future__ import annotations

from pathlib import Path
import pandas as pd


def write_parquet(df: pd.DataFrame, out_dir: Path, *, filename: str = "part-00001.parquet") -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / filename
    df.to_parquet(out_path, index=False)
    return out_path
