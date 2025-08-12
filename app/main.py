from pathlib import Path
from typing import Optional, List

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.database import get_bucket
from app.web.gradient import gradients
from app.web.icon import icon_for

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
# Context
# -------------------------------------------------

def _base_context(request: Request):
    return {
        "request": request,
        "settings": {
            "title": "Alla Romana",
            "background": gradients('holly')
        }
    }

def _context(request: Request):
    expenses, net, settlements, users = get_bucket(request.path_params.get('bucket'))

    result = {
        "bucket": bucket,
        "expenses": expenses,
        "net": net,
        "settlements": settlements,
        "users": users,
        "icon_for": icon_for,
    }
    result |= _base_context(request)
    return result

# -------------------------------------------------
# Routes
# -------------------------------------------------
@app.get("/bucket/{bucket}/user/{user}", response_class=HTMLResponse)
async def bucket(request: Request):
    return templates.TemplateResponse("/new/index.html", _context(request))

@app.get("/bucket/{bucket}/user/{user}/add", response_class=HTMLResponse)
async def bucket(request: Request):
    return templates.TemplateResponse("/new/edit.html", _context(request))

@app.post("/bucket/{bucket}/user/{user}/add", response_class=HTMLResponse)
async def bucket(request: Request,
                 amount: float = Form(...),  # required
                 description: str = Form(...),  # required
                 payedby: str = Form(...),  # required
                 sharedby: Optional[List[str]] = Form([])  # optional, defaults to empty list
                 ):

    print(amount)
    print(description)
    print(payedby)
    print(sharedby)

    return templates.TemplateResponse("/new/bucket.html", _context(request))

@app.exception_handler(StarletteHTTPException)
async def custom_404_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return templates.TemplateResponse('error.html', _base_context(request))
    # Let FastAPI handle other HTTP exceptions
    raise exc