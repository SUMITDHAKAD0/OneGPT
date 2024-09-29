from src.data_ingestion.data_loader import Loader
from src.logging import logger

data = Loader().csvloader()
print(data)

logger.info('All Good Buddy!!!')