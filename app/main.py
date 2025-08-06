import re
from pathlib import Path
from urllib.parse import unquote_plus

from fastapi import FastAPI, Request, Header
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.database import get_bucket
from app.icon import icon_for

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
        "title": "Alla Romana",
        "bucket": bucket,
        "expenses": expenses,
        "net": net,
        "settlements": settlements,
        "current_user": payer,
        "icon_for": icon_for,
    }

def _extract_bucket_payer(url: str) -> tuple[str, str]:
    """
    Extracts the bucket ID and payer name from URLs of the form
    .../bucket/<bucket_id>/payer/<payer_name>

    Returns
    -------
    (bucket_id, payer_name)  # both as str; cast bucket_id to int if you prefer
    """
    match = re.search(r"/bucket/([^/]+)/payer/([^/]+)", url)
    if not match:
        raise ValueError("URL does not match expected pattern")

    bucket_id, payer_name = match.groups()
    # Decode any percent-encoding in the payer name (e.g. Luca%20Brasi)
    return bucket_id, unquote_plus(payer_name)

# -------------------------------------------------
# Routes
# -------------------------------------------------
@app.get("/bucket/{bucket}/payer/{payer}", response_class=HTMLResponse)
async def read_root(request: Request, bucket: str, payer: str):
    return templates.TemplateResponse("index.html", _context(request, bucket, payer))

@app.get("/balances", response_class=HTMLResponse)
async def balances(request: Request, hx_current_url: str | None = Header(default=None)):
    bucket, payer = _extract_bucket_payer(hx_current_url)
    return templates.TemplateResponse("/fragments/balances.html", _context(request, bucket, payer))

@app.get("/expenses", response_class=HTMLResponse)
async def balances(request: Request, hx_current_url: str | None = Header(default=None)):
    bucket, payer = _extract_bucket_payer(hx_current_url)
    return templates.TemplateResponse("/fragments/expenses.html", _context(request, bucket, payer))