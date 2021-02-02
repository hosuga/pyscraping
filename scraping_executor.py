import json
import const
from scraping_manager import ScrapingManager


def main():
    scraped_data = None
    card_name = input('CardName: ')
    if card_name in const.CARDS:
        scraped_data = ScrapingManager(card_name).main()
    json_scrapd_data = json.dumps(scraped_data, indent=2, ensure_ascii=False)
    print(json_scrapd_data)


main()
