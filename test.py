from src.data_ingestion.data_loader import Loader
from src.logging import logger

data = Loader().csvloader()
print(data)
print('sumit')

logger.info('All Good Buddy!!!')