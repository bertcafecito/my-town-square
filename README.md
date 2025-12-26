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

3. Install Python dependencies for data scripts:
```bash
cd scripts/calendar_data
pip install -r requirements.txt
```

### Running Locally

Start the Hugo development server:
```bash
hugo server -D
```

Visit `http://localhost:1313` in your browser.

## 📊 Data Management

Event data is stored in JSON files under `data/aggregate_feed/` organized by month (YYYYMM.json).

### Fetching Event Data

Run the data fetching scripts:
```bash
cd scripts/calendar_data
python fetch_data.py      # Fetch raw event data
python aggregate_data.py  # Aggregate into monthly files
python summarize_data.py  # Create summaries
```

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
│   └── aggregate_feed/
├── layouts/             # Custom templates
│   └── _default/
│       └── calendar.html
├── scripts/             # Data fetching scripts
│   └── calendar_data/
├── themes/              # Hugo theme (PaperMod)
└── hugo.toml            # Site configuration
```

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
