from scrapy.cmdline import execute

import sys
import os


website = "guazi"
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", website, '-s', 'DOWNLOAD_DELAY=2.5'])

