from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from assets.parsers import table_to_dict
import pandas as pd


def get_b3_data() -> pd.DataFrame:
    bot_opt = Options()
    bot_opt.add_argument('--headless')
    bot = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=bot_opt)
    bot.get('https://www.fundamentus.com.br/buscaavancada.php')
    bot.find_element(By.CLASS_NAME, 'buscar').click()
    table_element = bot.find_element(By.ID, 'resultado')
    table_data = table_to_dict(table_element)
    bot.quit()
    df = pd.DataFrame(table_data)
    df.columns = df.columns.str.upper()
    return df