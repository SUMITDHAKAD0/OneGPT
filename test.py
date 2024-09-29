# from onegpt.data_ingestion import data_loader
from src.data_ingestion.data_loader import Loader
# from src.data_loader import Loader
# from src.logging.data_loader import Loader
from src.logging import logger

<<<<<<< HEAD
data = Loader().csvloader()
=======
data = Loader().webloader()
>>>>>>> 598c81eff96330aa6708df06ec4edf232aaa5fad
print(data)

logger.info('All Good Buddy!!!')