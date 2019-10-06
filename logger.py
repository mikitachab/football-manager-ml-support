import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('data_prepare_pipeline')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('pipeline.log')
formatter = logging.Formatter('%(levelname)s %(asctime)s: %(message)s', "%Y-%m-%d %H:%M:%S")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
