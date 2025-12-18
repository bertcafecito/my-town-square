import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import logging
import logging.config
from my_logging.logging_config import LOGGING
from pathlib import Path
from datetime import datetime
import json

logging.config.dictConfig(LOGGING)
logger = logging.getLogger(__name__)

def count_events_by_month(aggregate_folder):
    """
    Read all aggregate feed files and count events by month for each year.
    Returns a dictionary with year as key and monthly counts as value.
    """
    yearly_summaries = {}
    
    aggregate_path = Path(aggregate_folder)
    if not aggregate_path.exists():
        logger.error(f"Aggregate folder does not exist: {aggregate_folder}")
        return yearly_summaries
    
    # Process each YYYYMM.json file
    for json_file in aggregate_path.glob("*.json"):
        try:
            filename = json_file.stem  # e.g., "202601"
            if len(filename) != 6 or not filename.isdigit():
                logger.warning(f"Skipping file with unexpected name format: {json_file.name}")
                continue
            
            year = filename[:4]
            month = filename[4:6]
            
            # Load events from file
            with open(json_file, 'r', encoding='utf-8') as f:
                events = json.load(f)
            
            event_count = len(events)
            logger.info(f"File {json_file.name}: {event_count} events")
            
            # Initialize year if not exists
            if year not in yearly_summaries:
                yearly_summaries[year] = {}
            
            # Store count for this month
            yearly_summaries[year][month] = event_count
            
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON from {json_file.name}: {e}")
        except Exception as e:
            logger.error(f"Error processing {json_file.name}: {e}")
    
    return yearly_summaries

def save_yearly_summaries(yearly_summaries, output_folder):
    """
    Save yearly summaries to separate YYYY.json files.
    """
    output_path = Path(output_folder)
    output_path.mkdir(parents=True, exist_ok=True)
    
    for year, monthly_counts in yearly_summaries.items():
        output_file = output_path / f"{year}.json"
        
        # Sort months for consistent output
        sorted_counts = {month: monthly_counts[month] for month in sorted(monthly_counts.keys())}
        
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(sorted_counts, f, indent=2, ensure_ascii=False)
            logger.info(f"Saved yearly summary to {output_file}")
        except Exception as e:
            logger.error(f"Failed to save yearly summary for {year}: {e}")

def delete_past_aggregate_files(aggregate_folder, current_date=None):
    """
    Delete aggregate feed files from past months.
    Keeps files for the current month and future months.
    """
    if current_date is None:
        current_date = datetime.now()
    
    current_year_month = current_date.strftime("%Y%m")
    
    aggregate_path = Path(aggregate_folder)
    if not aggregate_path.exists():
        logger.error(f"Aggregate folder does not exist: {aggregate_folder}")
        return
    
    deleted_count = 0
    kept_count = 0
    
    for json_file in aggregate_path.glob("*.json"):
        try:
            filename = json_file.stem  # e.g., "202601"
            if len(filename) != 6 or not filename.isdigit():
                logger.warning(f"Skipping file with unexpected name format: {json_file.name}")
                continue
            
            # Delete if file is from past months
            if filename < current_year_month:
                json_file.unlink()
                logger.info(f"Deleted past aggregate file: {json_file.name}")
                deleted_count += 1
            else:
                logger.info(f"Keeping current/future file: {json_file.name}")
                kept_count += 1
                
        except Exception as e:
            logger.error(f"Error processing {json_file.name}: {e}")
    
    logger.info(f"Cleanup complete: Deleted {deleted_count} files, kept {kept_count} files")

def main():
    # Define paths
    base_path = Path(__file__).resolve().parents[2]
    aggregate_folder = base_path / 'data' / 'aggregate_feed'
    output_folder = base_path / 'data' / 'summarize_feed'
    
    logger.info("Starting yearly summary generation")
    logger.info(f"Aggregate folder: {aggregate_folder}")
    logger.info(f"Output folder: {output_folder}")
    
    # Count events by month for each year
    yearly_summaries = count_events_by_month(aggregate_folder)
    
    if not yearly_summaries:
        logger.warning("No data found to summarize")
    else:
        # Save yearly summaries
        save_yearly_summaries(yearly_summaries, output_folder)
        logger.info(f"Generated summaries for {len(yearly_summaries)} year(s)")
    
    # Delete past aggregate files
    logger.info("Starting cleanup of past aggregate files")
    delete_past_aggregate_files(aggregate_folder)
    
    logger.info("Yearly summary generation complete")

if __name__ == "__main__":
    main()
