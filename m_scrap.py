# author: Razu Ahmed

# ---------------------------
#       BBC News Scrap
# ---------------------------

from web_scrap import w_log
from web_scrap import w_scrap

# error log
w_log.set_custom_log_info('html/error.log')


news_scrap = w_scrap.NewsScraper(w_scrap.url_ds,w_log)
news_scrap.retrieve_webpage()
news_scrap.write_webpage_as_html() #by default: BBC News
news_scrap.read_webpage_as_html()
news_scrap.convert_data_to_bs4()
news_scrap.parse_soup_to_simple_html()


