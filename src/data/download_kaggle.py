from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi
from zipfile import ZipFile

def download_and_unzip(slug: str, dest: Path):
    dest = Path(dest); dest.mkdir(parents=True, exist_ok=True)
    api = KaggleApi(); api.authenticate()
    api.dataset_download_files(slug, path=dest, force=True, quiet=False)
    zips = sorted(dest.glob("*.zip"), key=lambda p: p.stat().st_mtime, reverse=True)
    if zips:
        with ZipFile(zips[0], "r") as zf:
            zf.extractall(dest)
        try: zips[0].unlink()
        except: pass
    return dest
