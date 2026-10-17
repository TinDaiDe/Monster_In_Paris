from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import importlib
from pathlib import Path
import routers
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
router_dir =  Path(__file__).parent / "routers"

for file in router_dir.glob("*.py"):
    if file.stem == "__init__":
        continue
    module_name = f"routers.{file.stem}"
    module = importlib.import_module(module_name)
    if hasattr(module, "router"):
        app.include_router(module.router)