import const
from scraping_manager import ScrapingManager

def main():
    scraped_data = None
    card_name = input('card_name: ')
    if card_name in const.CARDS:
        scraped_data = ScrapingManager(card_name).main()
    print(scraped_data)

main()