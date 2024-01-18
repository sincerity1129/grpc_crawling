from handlers.logger import Logger
from pb2file.server import serve

logger = Logger.set_logger(filename='logs/main.log')
serve(logger)