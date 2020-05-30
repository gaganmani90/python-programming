import os
from pathlib import Path

LOCATION_WW = "1"
LOCATION_INDIA = "23424848"  # PARENT ID
LOCATION_INDIA_NAGPUR = "2282863"
LOCATION_INDIA_JAIPUR = "2295401"
LOCATION_INDIA_LUCKNOW = "2295377"
LOCATION_INDIA_KANPUR = "2295378"
LOCATION_INDIA_PATNA = "2295381"
LOCATION_INDIA_RANCHI = "2295383"
LOCATION_INDIA_KOLKATA = "2295386"
SEATTLE = "2490383"
NY = "2459115"

# twitter trends keys
TREND_NAME = 'name'
TREND_VOLUME = 'tweet_volume'

# CACHE KEYS
TRENDS_VOLUME = "trends"
TREND_COUNT = "size"
GRAPH = "graphs"

# location json file
LOCATION_FILE_NAME = "places.json"  # all woeid
LOCATION_PATH = os.path.join('twitter', 'util', LOCATION_FILE_NAME)
ROOT = str(Path(os.path.dirname(os.path.abspath(__file__))).parent.parent)
KEY_WOEID = 'woeid'
KEY_PARENT_ID = 'parentid'
KEY_NAME = 'name'
KEY_COUNTRY_CODE = 'countryCode'

LOG_CONFIG_NAME = "logging_config.ini"

# database
DB_NAME = 'twitter_trends'
TABLE_LOCATION = 'LOCATION'
TABLE_TREND = 'TREND'

TREND_HARD_LIMIT = 20;
ENABLE_DB = True
