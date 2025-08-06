from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

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

def _context(request: Request, bucket: str, payer: str):
    expenses, net, settlements = get_bucket(bucket)

    return {
        "request": request,
        "settings": {
            "title": "Alla Romana",
            "background": gradients('standard')
        },
        "bucket": bucket,
        "expenses": expenses,
        "net": net,
        "settlements": settlements,
        "current_user": payer,
        "icon_for": icon_for,
    }

# -------------------------------------------------
# Routes
# -------------------------------------------------
@app.get("/bucket/{bucket}/payer/{payer}", response_class=HTMLResponse)
async def read_root(request: Request, bucket: str, payer: str):
    return templates.TemplateResponse("index.html", _context(request, bucket, payer))

@app.get("/tab", response_class=HTMLResponse)
async def balances(request: Request, tab: str, bucket: str, payer: str):
    if tab == 'expenses':
        return templates.TemplateResponse("/fragments/expenses.html", _context(request, bucket, payer))
    if tab == 'balances':
        return templates.TemplateResponse("/fragments/balances.html", _context(request, bucket, payer))