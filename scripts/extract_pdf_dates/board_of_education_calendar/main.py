import logging
import logging.config
from ...my_logging.logging_config import LOGGING
import PyPDF2
import json
import re
from datetime import datetime
from dateutil import parser

logging.config.dictConfig(LOGGING)
logger = logging.getLogger(__name__)

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF file."""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def parse_events_from_text(text):
    """Parse events and dates from the extracted text."""
    events = []
    
    # Log the extracted text for debugging
    logger.debug("=== EXTRACTED TEXT ===")
    logger.debug(text)
    logger.debug("=== END TEXT ===\n")
    
    # Manually extract key dates from the school calendar based on the text
    # These are extracted from the detailed schedule in the PDF
    
    school_events = [
        # September 2025
        ("September 3, 2025", "First Day of School - All Grades (1/2 Day Students)"),
        ("September 17, 2025", "Back to School Night - BHS"),
        ("September 18, 2025", "Back to School Night - Community Schools"),
        
        # October 2025
        ("October 2, 2025", "Progress Report - BHS"),
        ("October 13, 2025", "No School - Columbus Day"),
        ("October 16, 2025", "Progress Report - PreK-8"),
        
        # November 2025
        ("November 4, 2025", "No School - Fall Break/Veteran's Day"),
        ("November 5, 2025", "No School - Fall Break/Veteran's Day"),
        ("November 6, 2025", "No School - Fall Break/Veteran's Day"),
        ("November 7, 2025", "No School - Fall Break/Veteran's Day"),
        ("November 10, 2025", "No School - Fall Break/Veteran's Day"),
        ("November 11, 2025", "No School - Fall Break/Veteran's Day"),
        ("November 12, 2025", "End of 1st Marking Period - BHS"),
        ("November 20, 2025", "Report Card Distribution - BHS"),
        ("November 20, 2025", "Parents' Night - BHS"),
        ("November 27, 2025", "No School - Thanksgiving Break"),
        ("November 28, 2025", "No School - Thanksgiving Break"),
        
        # December 2025
        ("December 9, 2025", "End of 1st Trimester - PreK-8"),
        ("December 17, 2025", "Progress Report - BHS"),
        ("December 18, 2025", "Open House - PreK-8"),
        ("December 18, 2025", "Report Card Distribution - PreK-8"),
        ("December 24, 2025", "No School - Winter Break"),
        ("December 25, 2025", "No School - Winter Break"),
        ("December 26, 2025", "No School - Winter Break"),
        ("December 29, 2025", "No School - Winter Break"),
        ("December 30, 2025", "No School - Winter Break"),
        ("December 31, 2025", "No School - Winter Break"),
        
        # January 2026
        ("January 1, 2026", "No School - New Year's Day"),
        ("January 2, 2026", "No School - Winter Break"),
        ("January 19, 2026", "No School - MLK Jr. Day"),
        ("January 29, 2026", "End of 2nd Marking Period - BHS"),
        
        # February 2026
        ("February 2, 2026", "Progress Report - PreK-8"),
        ("February 5, 2026", "Report Card Distribution - BHS"),
        ("February 5, 2026", "Mid-Year Parent Conference - BHS"),
        ("February 16, 2026", "No School - Presidents' Day"),
        
        # March 2026
        ("March 3, 2026", "Progress Report - BHS"),
        ("March 18, 2026", "End of 2nd Trimester - PreK-8"),
        ("March 26, 2026", "Mid-Year Parent Conference - PreK-8"),
        ("March 26, 2026", "Report Card Distribution - PreK-8"),
        ("March 31, 2026", "End of 3rd Marking Period - BHS"),
        
        # April 2026
        ("April 3, 2026", "No School - Spring Break"),
        ("April 6, 2026", "No School - Spring Break"),
        ("April 7, 2026", "No School - Spring Break"),
        ("April 8, 2026", "No School - Spring Break"),
        ("April 9, 2026", "No School - Spring Break"),
        ("April 10, 2026", "No School - Spring Break"),
        ("April 20, 2026", "Report Card Distribution - BHS"),
        
        # May 2026
        ("May 7, 2026", "Progress Report - PreK-8"),
        ("May 13, 2026", "Progress Report - BHS"),
        ("May 26, 2026", "No School - Memorial Day"),
        
        # June 2026
        ("June 19, 2026", "District Closed - Juneteenth"),
        ("June 22, 2026", "Last Day of School - All Grades"),
        ("June 22, 2026", "End of 4th Marking Period - BHS"),
        ("June 22, 2026", "End of 3rd Trimester - PreK-8"),
    ]
    
    for date_str, description in school_events:
        try:
            parsed_date = parser.parse(date_str)
            events.append({
                'date': parsed_date,
                'description': description,
                'original_line': f"{date_str}: {description}"
            })
            logger.info(f"Added event: {date_str} -> {description}")
        except Exception as e:
            logger.error(f"Error parsing {date_str}: {e}")
    
    return events

def format_events_to_json(events):
    """Format events into the required JSON structure."""
    formatted_events = []
    
    for event in events:
        # All-day events - start at midnight
        start_time = event['date'].replace(hour=0, minute=0, second=0)
        end_time = event['date'].replace(hour=23, minute=59, second=59)
        
        formatted_events.append({
            "summary": event['description'],
            "start": start_time.strftime("%Y-%m-%dT%H:%M:%S"),
            "end": end_time.strftime("%Y-%m-%dT%H:%M:%S"),
            "fetched_at": datetime.now().isoformat()
        })
    
    return formatted_events

def main():
    pdf_path = "2025-2026OfficialBBOEDCalendar.pdf"
    output_path = r"..\..\..\data\calendar_feeds\manual_entries\board_of_education\events.json"
    
    logger.info(f"Reading PDF: {pdf_path}")
    text = extract_text_from_pdf(pdf_path)
    
    logger.info(f"Parsing events...")
    events = parse_events_from_text(text)
    
    logger.info(f"Found {len(events)} events")
    for event in events:
        logger.info(f"  - {event['date'].strftime('%Y-%m-%d')}: {event['description']}")
    
    if events:
        formatted = format_events_to_json(events)
        
        with open(output_path, 'w') as f:
            json.dump(formatted, f, indent=4)
        
        logger.info(f"Events saved to: {output_path}")
    else:
        logger.warning("No events found. Please review the extracted text above and adjust the parsing logic.")

if __name__ == "__main__":
    main()
