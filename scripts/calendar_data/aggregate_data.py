import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import logging
import logging.config
from my_logging.logging_config import LOGGING
from pathlib import Path
from datetime import datetime, timedelta
import json

logging.config.dictConfig(LOGGING)
logger = logging.getLogger(__name__)

def collect_events_from_feeds_folder(feeds_root_folder):
    all_events = []
    # Recursively search for all events.json files in the folder tree
    for events_file in feeds_root_folder.rglob('events.json'):
        logger.info(f"Reading events from {events_file}")
        try:
            with open(events_file, 'r', encoding='utf-8') as f:
                events = json.load(f)
                all_events.extend(events)
                logger.info(f"Loaded {len(events)} events from {events_file}")
        except Exception as e:
            logger.error(f"Failed to read events from {events_file}: {e}")

    logger.info(f"Total events collected: {len(all_events)}")
    return all_events

def filter_events_by_date_range(events, start_date, end_date):
    filtered_events = []
    for event in events:
        try:
            event_start = datetime.fromisoformat(event['start']).date()
            event_end = datetime.fromisoformat(event['end']).date()
            if event_start <= end_date and event_end >= start_date:
                filtered_events.append(event)
        except Exception as e:
            logger.error(f"Failed to parse event dates for event {event}: {e}")

    logger.info(f"Total events after filtering: {len(filtered_events)}")
    return filtered_events

def save_events_to_file(events, output_folder):
    if not os.path.exists(output_folder):
        logger.info("The output folder does not exist. Creating it.")
        try:
            os.makedirs(output_folder)
        except Exception as e:
            logger.error(f"Failed to create output folder {output_folder}: {e}")
            return

    # Group events by YYYYMM of their start date
    events_by_month = {}
    for event in events:
        try:
            event_start = datetime.fromisoformat(event['start'])
            month_key = event_start.strftime('%Y%m')
            
            if month_key not in events_by_month:
                events_by_month[month_key] = []
            events_by_month[month_key].append(event)
        except Exception as e:
            logger.error(f"Failed to parse event start date for event {event}: {e}")

    # Save each month's events to a separate file
    for month_key, month_events in events_by_month.items():
        output_file = Path(output_folder) / f"{month_key}.json"
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(month_events, f, indent=2, ensure_ascii=False)
            logger.info(f"Saved {len(month_events)} events to {output_file}")
        except Exception as e:
            logger.error(f"Failed to save events to {output_file}: {e}")

            
def main():
    root_dir = Path(__file__).parent.parent.parent
    calendar_feeds_dir = root_dir / "data" / "calendar_feeds"

    if not calendar_feeds_dir.exists():
        logger.error(f"Calendar feeds directory does not exist: {calendar_feeds_dir}")
        return
    
    # Calculate the data range: from today plus 45 days ahead
    today = datetime.now().date()
    end_date = today + timedelta(days=45)
    logger.info(f"Aggregating events from {today.isoformat()} to {end_date.isoformat()}")

    all_events = collect_events_from_feeds_folder(calendar_feeds_dir)
    filtered_events = filter_events_by_date_range(all_events, today, end_date)
    output_folder = root_dir / "data" / "aggregate_feed"
    save_events_to_file(filtered_events, output_folder)

if __name__ == "__main__":
    main()
