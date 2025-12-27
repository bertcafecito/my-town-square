# My Town Square Scripts

Python package for automating calendar event data management for the My Town Square community hub.

## 📦 Package Structure

This package follows Python packaging standards (PEP 517/518) with a proper module hierarchy:

```
scripts/
├── __init__.py              # Package initialization
├── setup.py                 # Package installation configuration
├── requirements.txt         # All Python dependencies
├── my_logging/              # Shared logging utilities
│   ├── __init__.py
│   ├── logging_config.py    # Centralized logging configuration
│   └── logging_filters.py   # Custom logging filters
├── calendar_data/           # Calendar event data processing
│   ├── __init__.py
│   ├── requirements.txt     # Module-specific dependencies
│   ├── fetch_data.py        # Fetch events from iCal feeds
│   ├── aggregate_data.py    # Aggregate events by month
│   └── summarize_data.py    # Generate event summaries
└── extract_pdf_dates/       # PDF date extraction utilities
    ├── __init__.py
    └── board_of_education_calendar/
        ├── __init__.py
        ├── requirements.txt # Module-specific dependencies
        └── main.py          # Extract dates from BOE PDFs
```

## 🐍 Python Standards Implemented

### 1. **Package Structure**
- Each directory contains `__init__.py` making it a proper Python package
- Modules are organized by functionality
- Shared utilities (`my_logging`) are at the package root level

### 2. **Dependency Management**
- Root `requirements.txt` contains all dependencies
- Individual modules have their own `requirements.txt` for documentation
- `setup.py` uses `setuptools` for proper package installation

### 3. **Import Structure**
- Modules use relative imports within the package
- Shared utilities are accessible via `from my_logging import ...`
- No sys.path manipulation needed when installed properly

### 4. **Installation Options**

#### Option A: Install as Editable Package (Recommended for Development)
```bash
cd scripts
pip install -e .
```

#### Option B: Install Dependencies Only
```bash
cd scripts
pip install -r requirements.txt
```

### 5. **Running Scripts**

After installation as a package, scripts can be run as modules:

```bash
# From project root
python -m scripts.calendar_data.fetch_data
python -m scripts.calendar_data.aggregate_data
python -m scripts.calendar_data.summarize_data

# Extract dates from PDF
python -m scripts.extract_pdf_dates.board_of_education_calendar.main
```

### 6. **GitHub Actions Integration**

The workflow at `.github/workflows/update-calendar-data.yml` automatically:
- Installs the scripts package using `pip install -e .`
- Runs the data pipeline daily at 1 AM EST
- Commits and pushes updated calendar data
- Can be triggered manually via workflow_dispatch

The workflow uses the proper package structure for reliable execution.

## 📋 Module Descriptions

### `my_logging/`
Centralized logging configuration shared across all scripts:
- **logging_config.py**: Dictionary-based logging configuration
- **logging_filters.py**: Custom filters for log messages

### `calendar_data/`
Scripts for fetching and processing calendar event data:
- **fetch_data.py**: Fetches events from iCal URLs and saves to JSON
- **aggregate_data.py**: Aggregates events into monthly JSON files
- **summarize_data.py**: Creates yearly summaries of events

### `extract_pdf_dates/`
Tools for extracting event dates from PDF documents:
- **board_of_education_calendar/main.py**: Extracts school calendar events from PDF

## 🔧 Development

### Adding New Scripts
1. Create a new module directory under `scripts/`
2. Add `__init__.py` with module docstring
3. Update `setup.py` if adding new dependencies
4. Update root `requirements.txt` with any new dependencies
5. Document in this README

### Code Standards
- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Include docstrings for modules, classes, and functions
- Use the shared `my_logging` configuration for consistency

## 📝 Dependencies

See `requirements.txt` for the complete list. Key dependencies:
- `icalendar`: iCal feed parsing
- `requests`: HTTP requests for data fetching
- `PyPDF2`: PDF text extraction
- `python-json-logger`: Structured JSON logging
- `python-dateutil`: Date parsing and manipulation

## 🚀 Quick Start

```bash
# 1. Navigate to scripts directory
cd scripts

# 2. Install the package in development mode
pip install -e .

# 3. Run data fetching pipeline
python -m calendar_data.fetch_data
python -m calendar_data.aggregate_data
python -m calendar_data.summarize_data
```

## 📚 Further Reading

- [PEP 8 - Style Guide](https://peps.python.org/pep-0008/)
- [Python Packaging Guide](https://packaging.python.org/)
- [PEP 517/518 - Build System](https://peps.python.org/pep-0517/)
