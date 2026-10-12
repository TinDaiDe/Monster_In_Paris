from fastapi import FastAPI
import importlib
from pathlib import Path
import routers
app = FastAPI()

router_dir =  Path(__file__).parent / "routers"

for file in router_dir.glob("*.py"):
    if file.stem == "__init__":
        continue
    module_name = f"routers.{file.stem}"
    module = importlib.import_module(module_name)
    if hasattr(module, "router"):
        app.include_router(module.router)