from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles

from data_manager.good_reads_data_manager import GoodReadsDataManager
from data_manager.data_loader import DataLoader
from handlers.error_handlers import load_error_handlers
from handlers.field_handlers import load_field_handlers
from handlers.review_handlers import load_review_handlers

GOODREADS_PATH = './data/data.csv'
data_manager = GoodReadsDataManager(DataLoader.load(file_location=GOODREADS_PATH))

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"))


@app.get("/")
def start():
    return FileResponse("goodreads.html")

load_review_handlers(app, data_manager)
load_field_handlers(app, data_manager)
load_error_handlers(app)


