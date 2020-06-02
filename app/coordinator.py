import uvicorn

from app.db.mongo_init import Mongo
from app.main import FastAPI, app
from app.utils.logger import logger


class Coordinator:
    def __init__(self):
        self.app = FastAPI()
        self.mgdb = Mongo()

    def run(self):
        uvicorn.run(app)
        logger.info("People register ready...")
