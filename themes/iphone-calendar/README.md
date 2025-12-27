# iPhone Calendar Hugo Theme

A modern, responsive Hugo theme with iPhone-style design, featuring both calendar and standard page layouts, with light/dark modes and color-blind accessibility support.

![iPhone Calendar Theme](https://via.placeholder.com/800x600?text=iPhone+Calendar+Theme)

## Features

- 📱 **iPhone-Style Design** - Clean, modern interface inspired by iOS
- 📅 **Dual Layout System** - Calendar pages for events, standard pages for content
- 🌓 **Dark Mode Support** - Automatic, light, and dark themes with smooth transitions
- ♿ **Accessibility First** - Color-blind mode with enhanced contrast and patterns
- 📱 **Fully Responsive** - Optimized for mobile, tablet, and desktop
- 🎨 **Beautiful Event Colors** - 8 distinct color schemes for event categorization
- ⚡ **Performance Optimized** - Minimal CSS, no external dependencies
- 🔍 **Touch Optimized** - Perfect touch targets and gestures for mobile devices
- 🎯 **Complete Theme** - Handles all page types (home, single, list, calendar)

## Installation

### As a Hugo Module (Recommended)

```bash
hugo mod init github.com/yourusername/yoursite
```

Add to your `hugo.toml`:

```toml
[module]
  [[module.imports]]
    path = "github.com/bertcafecito/my-town-square/themes/iphone-calendar"
```

### As a Git Submodule

```bash
cd your-hugo-site
git submodule add https://github.com/bertcafecito/my-town-square.git themes/iphone-calendar
```

### Manual Installation

1. Download the theme
2. Extract to `themes/iphone-calendar` in your Hugo site
3. Update your `hugo.toml` to use the theme

## Configuration

Update your `hugo.toml`:

```toml
theme = 'iphone-calendar'

[params]
  description = 'Your community events calendar'
  author = 'Your Name'
```

## Usage

### Page Types

The theme automatically handles different page types:

#### 1. Calendar Pages
Add `layout = "calendar"` to the front matter:

```markdown
---
title: "Community Calendar"
layout: calendar
---

Welcome to our community events calendar!
```

Calendar pages display:
- Interactive month-by-month calendar grid
- Event dots on days with events
- Event list panel showing selected day's events
- Theme toggle and color-blind mode controls
- Month navigation (previous/next/today)

#### 2. Standard Pages
For regular content pages (about, support, etc.), simply create them without the calendar layout:

```markdown
---
title: "About Us"
---

Your content here...
```

Standard pages display:
- Header with site title and navigation menu
- Theme toggle button
- Main content area
- Footer

#### 3. Home Page
The home page uses `index.html` layout automatically and shows your site title and welcome content.

#### 4. List Pages
List pages (categories, tags, sections) use `list.html` layout automatically.

### Event Data Structure

The theme expects event data in `data/aggregate_feed/` as JSON files:

```json
[
  {
    "summary": "Event Title",
    "start": "2025-01-15T14:00:00Z",
    "end": "2025-01-15T16:00:00Z"
  }
]
```

**Directory structure:**
```
data/
  aggregate_feed/
    202501.json
    202502.json
    202503.json
```

Each file should contain an array of events for that month.

### Event Data Format

Events should include:
- `summary` (string): Event title
- `start` (ISO 8601 datetime): Event start time
- `end` (ISO 8601 datetime): Event end time

Example:
```json
[
  {
    "summary": "Town Hall Meeting",
    "start": "2025-01-20T19:00:00Z",
    "end": "2025-01-20T21:00:00Z"
  },
  {
    "summary": "Community Cleanup Day",
    "start": "2025-01-25T09:00:00Z",
    "end": "2025-01-25T12:00:00Z"
  }
]
```

## Customization

### Color Themes

The theme uses CSS variables for easy customization. Override in your site's CSS:

```css
:root {
  --cal-accent: #007AFF;
  --cal-bg: #FFFFFF;
  --cal-text: #000000;
}

[data-theme="dark"] {
  --cal-accent: #0A84FF;
  --cal-bg: #000000;
  --cal-text: #FFFFFF;
}
```

### Event Colors

Eight predefined colors are available for events:
- Blue (`--cal-blue`)
- Orange (`--cal-orange`)
- Pink (`--cal-pink`)
- Purple (`--cal-purple`)
- Green (`--cal-green`)
- Red (`--cal-red`)
- Yellow (`--cal-yellow`)
- Teal (`--cal-teal`)

Events are automatically assigned colors based on their title hash.

## Theme Features

### Accessibility Controls

- **Theme Toggle**: Cycles between light, dark, and auto modes
- **Color Blind Mode**: Enhanced contrast with pattern overlays on event dots

### Calendar Features

- Month navigation with previous/next buttons
- "Back to Today" quick navigation
- Day selection to view events
- Event indicators (dots) on days with events
- Responsive grid layout
- Touch-optimized for mobile devices

### Event Display

- Time-based or all-day event indicators
- Organized by start time
- Color-coded event cards
- Smooth animations and transitions
- "No events" empty state

## Browser Support

- Chrome/Edge (latest 2 versions)
- Firefox (latest 2 versions)
- Safari (latest 2 versions)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Performance

- No external dependencies
- Minimal CSS (~950 lines, ~25KB minified)
- JavaScript included inline for optimal loading
- CSS variables for theme switching (no JavaScript re-renders)

## Accessibility Features

- WCAG 2.1 AA compliant
- Keyboard navigation support
- Focus indicators for all interactive elements
- High contrast mode support
- Reduced motion support for `prefers-reduced-motion`
- Touch target sizes meet accessibility guidelines (44x44px minimum)
- Screen reader friendly
- Color-blind friendly patterns

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see [LICENSE](../../LICENSE) file for details

## Credits

Developed by [Albert Marrero](https://github.com/bertcafecito)

Inspired by the iOS Calendar app design.

## Support

For issues, questions, or contributions, please visit:
- [GitHub Repository](https://github.com/bertcafecito/my-town-square)
- [Issue Tracker](https://github.com/bertcafecito/my-town-square/issues)

## Changelog

### Version 1.0.0 (Initial Release)
- iPhone-style calendar interface
- Light/dark/auto theme modes
- Color-blind accessibility mode
- Responsive design for all devices
- Event data integration from Hugo data files
- Touch-optimized interactions
