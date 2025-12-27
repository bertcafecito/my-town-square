# My Town Square - Bayonne Community Events

A community hub for discovering local events in Bayonne, NJ - no social media required.

## 🎯 Purpose

My Town Square aggregates community events from various sources into one convenient calendar, making it easy for Bayonne residents to stay connected with local happenings without needing social media accounts.

## ✨ Features

- **📅 Interactive Calendar** - Browse events in an intuitive calendar view with iOS-inspired design
- **🔍 Easy Navigation** - Navigate between months and click dates to see event details
- **📱 Mobile Responsive** - Works seamlessly on phones, tablets, and desktops
- **🌓 Dark Mode Support** - Automatically adapts to system preferences
- **⚡ Fast & Lightweight** - Built with Hugo for optimal performance

## 🚀 Getting Started

### Prerequisites

- [Hugo Extended](https://gohugo.io/installation/) (v0.120.0 or later)
- Python 3.8+ (for data fetching scripts)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/bertcafecito/my-town-square.git
cd my-town-square
```

2. Initialize the theme submodule:
```bash
git submodule update --init --recursive
```

3. Install the Python scripts package:
```bash
cd scripts
pip install -e .
cd ..
```

This installs the scripts as a proper Python package following PEP 517/518 standards.

### Running Locally

Start the Hugo development server:
```bash
hugo server -D
```

Visit `http://localhost:1313` in your browser.

## 📊 Data Management

Event data is stored in JSON files under `data/aggregate_feed/` organized by month (YYYYMM.json).

### Fetching Event Data

The `scripts/` directory contains a Python package following Python packaging standards. Install and run:

```bash
cd scripts
pip install -e .              # Install package in development mode
python -m calendar_data.fetch_data      # Fetch raw event data
python -m calendar_data.aggregate_data  # Aggregate into monthly files
python -m calendar_data.summarize_data  # Create summaries
```

For detailed information about the scripts package structure and Python standards, see [`scripts/README.md`](scripts/README.md).

## 🏗️ Project Structure

```
my-town-square/
├── archetypes/          # Content templates
├── assets/              # CSS and other assets
│   └── css/extended/    # Custom calendar styling
├── content/             # Page content
│   ├── about.md
│   ├── calendar.md
│   └── support.md
├── data/                # Event data (JSON)
│   ├── aggregate_feed/  # Monthly aggregated events
│   ├── calendar_feeds/  # Source event feeds
│   └── summarize_feed/  # Yearly summaries
├── layouts/             # Custom templates
│   └── _default/
│       └── calendar.html
├── scripts/             # Python package for data automation
│   ├── __init__.py      # Package initialization
│   ├── setup.py         # Package installation config
│   ├── requirements.txt # All dependencies
│   ├── README.md        # Detailed scripts documentation
│   ├── my_logging/      # Shared logging utilities
│   ├── calendar_data/   # Event fetching and processing
│   └── extract_pdf_dates/ # PDF date extraction
├── themes/              # Hugo theme (iphone-calendar)
└── hugo.toml            # Site configuration
```

### Python Package Standards

The `scripts/` directory follows Python packaging best practices:
- **Proper package structure** with `__init__.py` files
- **Setup.py** for package installation (PEP 517/518)
- **Centralized dependencies** in root requirements.txt
- **Modular design** with separate packages for different functionality
- **Shared utilities** (`my_logging`) accessible across all modules

For detailed documentation on the Python package structure and standards, see [`scripts/README.md`](scripts/README.md).

## 🎨 Customization

### Updating Site Configuration

Edit `hugo.toml` to customize:
- Site title and description
- Menu items
- Social links
- Theme parameters

### Styling

Custom CSS is located in:
- `assets/css/extended/iphone-calendar.css` - iOS-inspired calendar styling
- Inline styles in `layouts/_default/calendar.html`

## 🚢 Deployment

### GitHub Pages

1. Update `baseURL` in `hugo.toml`:
```toml
baseURL = 'https://yourusername.github.io/my-town-square/'
```

2. Build the site:
```bash
hugo
```

3. Deploy the `public/` directory to GitHub Pages

### Netlify / Vercel

These platforms auto-detect Hugo and build automatically. Just:
1. Connect your repository
2. Set build command: `hugo`
3. Set publish directory: `public`

## 🤝 Contributing

Contributions are welcome! Whether it's:
- Bug reports
- Feature suggestions
- Code improvements
- Documentation updates

Please feel free to open an issue or submit a pull request.

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Built with [Hugo](https://gohugo.io/)
- Theme: [PaperMod](https://github.com/adityatelange/hugo-PaperMod)
- Calendar design inspired by iOS Calendar

## 📧 Contact

For questions or suggestions, please open an issue on GitHub.

---

**Made with ❤️ for the Bayonne community**
