# from onegpt.data_ingestion import data_loader
from src.data_ingestion.data_loader import Loader
# from src.data_loader import Loader
# from src.logging.data_loader import Loader
from src.logging import logger

data = Loader().csvloader()
print(data)

logger.info('All Good Buddy!!!')