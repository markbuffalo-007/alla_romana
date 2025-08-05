from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# -------------------------------------------------
# Create / configure the FastAPI application
# -------------------------------------------------
app = FastAPI(title="FastAPI-Jinja Boilerplate")

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# Serve static files (e.g., CSS, JS, images)
app.mount(
    "/static",
    StaticFiles(directory=str(BASE_DIR / "static")),
    name="static",
)


# -------------------------------------------------
# Routes
# -------------------------------------------------
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Render the home page (templates/index.html).
    Pass the request and any context vars to Jinja2.
    """
    context = {
        "request": request,    # **must** include for Jinja2Templates
        "title": "Hello, Jinja2 + FastAPI!",
        "items": ["🍎 Apple", "🍐 Pear", "🍌 Banana"],
    }
    return templates.TemplateResponse("index.html", context)