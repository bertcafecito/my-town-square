import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import logging
import logging.config
from my_logging.logging_config import LOGGING

from datetime import datetime
from pathlib import Path
from icalendar import Calendar
import requests
import json

logging.config.dictConfig(LOGGING)
logger = logging.getLogger(__name__)

def fetch_ical_data(url):
    fetched_at = datetime.now().isoformat()
    response = requests.get(url)
    response.raise_for_status()
    try:
        cal = Calendar.from_ical(response.content)
    except Exception as e:
        logger.error(f"Failed to parse iCal data from {url}: {e}")
        return []
    
    events = []
    for component in cal.walk():
        if component.name == "VEVENT":
            event_summary = component.get('summary')
            event_start = component.get('dtstart').dt.isoformat()
            event_end = component.get('dtend').dt.isoformat()
            
            events.append({
                "summary": event_summary,
                "start": event_start,
                "end": event_end,
                "fetched_at": fetched_at
            })
    return events

def save_events_to_file(events, output_folder):
    if not os.path.exists(output_folder):
        logger.info("The output folder does not exist. Creating it.")
        try:
            os.makedirs(output_folder)
        except Exception as e:
            logger.error(f"Failed to create output folder {output_folder}: {e}")
            return  

    try:
        output_file = os.path.join(output_folder, "events.json")
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(events, json_file, indent=4, ensure_ascii=False)
        return output_file
    except Exception as e:
        logger.error(f"Failed to write events to file {output_file}: {e}")

    
def main():

    # Calender Feeds
    feeds = [
        {
            "name": "Public Library",
            "url": "https://bayonnelibrary.libcal.com/ical_subscribe.php?src=p&cid=17197",
            "feed_type": "ical",
            "output_folder": "data/calendar_feeds/public_library/"
        },
        {
            "name": "Board of Education",
            "url": "https://www.bboed.org/cf_calendar/feed.cfm?type=ical&feedID=E3C0D58EC5E44405AD6A31D2556243CD",
            "feed_type": "ical",
            "output_folder": "data/calendar_feeds/board_of_education/"
        }
    ]

    for feed in feeds:

        feed_name = feed.get("name", "Unnamed Feed")
        feed_type = feed.get("feed_type", None)
        feed_url = feed.get("url", None)
        output_folder = feed.get("output_folder", None)

        if feed_type is None:
            logger.warning(f"Feed type not specified for feed: {feed_name}")
            continue

        if feed_url is None:
            logger.warning(f"Feed URL not specified for feed: {feed_name}")
            continue

        if feed_type == "ical":
            logger.info(f"The feed type for '{feed_name}' is 'ical'. Proceeding to fetch data.")
            try:
                events = fetch_ical_data(feed_url)
                logger.info(f"Fetched {len(events)} events for the {feed_name}")
            except Exception as e:
                logger.error(f"Error fetching data for the {feed_name}: {e}")

            if output_folder is not None:
                root_dir = Path(__file__).parent.parent.parent
                output_folder = root_dir / output_folder
                output_file = save_events_to_file(events, output_folder)
                logger.info(f"Saved events to {output_file}")
            else:
                logger.warning(f"Output folder not specified for feed: {feed_name}")
            continue

        logger.warning(f"Unsupported feed type '{feed_type}' for feed: {feed_name}")

        
if __name__ == "__main__":
    main()