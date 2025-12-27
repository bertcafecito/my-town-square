import PyPDF2
import json
import re
from datetime import datetime
from dateutil import parser

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
    
    # Print the extracted text for debugging
    print("=== EXTRACTED TEXT ===")
    print(text)
    print("=== END TEXT ===\n")
    
    # Manually extract key dates from the school calendar based on the text
    # These are extracted from the detailed schedule in the PDF
    
    school_events = [
        # September 2025
        ("September 3, 2025", "First Day of School - All Grades (1/2 Day Students)"),
        ("September 17, 2025", "Back to School Night - BHS"),
        ("September 18, 2025", "Back to School Night - Community Schools"),
        
        # October 2025
        ("October 2, 2025", "Progress Report - BHS"),
        ("October 16, 2025", "Progress Report - PreK-8"),
        
        # November 2025
        ("November 12, 2025", "End of 1st Marking Period - BHS"),
        ("November 20, 2025", "Report Card Distribution - BHS"),
        ("November 20, 2025", "Parents' Night - BHS"),
        
        # December 2025
        ("December 9, 2025", "End of 1st Trimester - PreK-8"),
        ("December 17, 2025", "Progress Report - BHS"),
        ("December 18, 2025", "Open House - PreK-8"),
        ("December 18, 2025", "Report Card Distribution - PreK-8"),
        
        # January 2026
        ("January 29, 2026", "End of 2nd Marking Period - BHS"),
        
        # February 2026
        ("February 2, 2026", "Progress Report - PreK-8"),
        ("February 5, 2026", "Report Card Distribution - BHS"),
        ("February 5, 2026", "Mid-Year Parent Conference - BHS"),
        
        # March 2026
        ("March 3, 2026", "Progress Report - BHS"),
        ("March 18, 2026", "End of 2nd Trimester - PreK-8"),
        ("March 26, 2026", "Mid-Year Parent Conference - PreK-8"),
        ("March 26, 2026", "Report Card Distribution - PreK-8"),
        ("March 31, 2026", "End of 3rd Marking Period - BHS"),
        
        # April 2026
        ("April 20, 2026", "Report Card Distribution - BHS"),
        
        # May 2026
        ("May 7, 2026", "Progress Report - PreK-8"),
        ("May 13, 2026", "Progress Report - BHS"),
        
        # June 2026
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
            print(f"Added event: {date_str} -> {description}")
        except Exception as e:
            print(f"Error parsing {date_str}: {e}")
    
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
    pdf_path = r"c:\Users\albert.marrero\code\my-town-square\data\calendar_feeds\manual_entries\2025-2026OfficialBBOEDCalendar.pdf"
    output_path = r"c:\Users\albert.marrero\code\my-town-square\data\calendar_feeds\manual_entries\board_of_education\events.json"
    
    print(f"Reading PDF: {pdf_path}")
    text = extract_text_from_pdf(pdf_path)
    
    print(f"\nParsing events...")
    events = parse_events_from_text(text)
    
    print(f"\nFound {len(events)} events")
    for event in events:
        print(f"  - {event['date'].strftime('%Y-%m-%d')}: {event['description']}")
    
    if events:
        formatted = format_events_to_json(events)
        
        with open(output_path, 'w') as f:
            json.dump(formatted, f, indent=4)
        
        print(f"\nEvents saved to: {output_path}")
    else:
        print("\nNo events found. Please review the extracted text above and adjust the parsing logic.")

if __name__ == "__main__":
    main()
