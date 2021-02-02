# .env ファイルをロードして環境変数へ反映
import os
from dotenv import load_dotenv


load_dotenv()
CHROMEDRIVER_PATH = os.getenv('CHROMEDRIVER_PATH')
