# iPhone-Style Calendar - Feature Guide

## 🎨 Overview

Your calendar now features a modern, iOS-inspired design that works beautifully across all devices - from phones to desktops. It includes comprehensive accessibility features including light/dark themes and color blindness support.

## ✨ Key Features

### 📱 Responsive Design
- **Mobile Phones (< 768px)**: Optimized touch interface with bottom navigation
- **Tablets (768px - 1023px)**: Comfortable medium-sized layout
- **Laptops & Desktops (> 1024px)**: Full-featured calendar view
- **Large Screens (> 1440px)**: Enhanced spacing and sizing

### 🌓 Theme System
Click the sun/moon icon (☀️/🌙) in the top-right to cycle through themes:
1. **Light Mode**: Clean white background with dark text
2. **Dark Mode**: Black background optimized for OLED screens
3. **Auto Mode**: Automatically matches your system preferences

Themes are saved in your browser so your preference persists between visits.

### 👁️ Color Blind Support
Click the eye icon (👁️) to enable color blind mode:
- Uses high-contrast color combinations
- Adds patterns/borders to event dots for distinction
- Works with both light and dark themes
- Preference is saved in your browser

### 🎯 iPhone Calendar Design Elements

#### Header Section
- **Back to Today**: Click "← YEAR" to jump to today's date
- **Month Navigation**: Arrow buttons to move between months
- **Quick Actions**: View toggle, search, and add buttons

#### Calendar Grid
- **Today Indicator**: Red circle highlights today's date
- **Event Dots**: Colorful dots below dates show events
  - Up to 3 dots displayed per day
  - "+N" indicator for additional events
- **Interactive Cells**: Hover/tap effects for better feedback

#### Events List
- **Date Badge**: Shows selected day with abbreviated weekday
- **Colored Event Cards**: Each event has a distinctive color bar
- **Time Display**: Shows start/end times or "all-day" for full-day events
- **Smooth Animations**: Events slide in smoothly when displayed

### 🎨 Event Colors
Events are automatically assigned colors based on their title:
- **Blue** (#007AFF) - Primary events
- **Orange** (#FF9500) - Scheduled activities
- **Pink** (#FF2D55) - Special occasions
- **Purple** (#AF52DE) - Meetings
- **Green** (#34C759) - Completed/confirmed
- **Red** (#FF3B30) - Important/urgent
- **Yellow** (#FFCC00) - Pending
- **Teal** (#5AC8FA) - Optional events

### ♿ Accessibility Features

#### Keyboard Navigation
- All buttons and days are keyboard accessible
- Clear focus indicators (blue outline)
- Tab through interactive elements

#### Touch Optimization
- 44x44px minimum touch targets
- Smooth tap animations
- Optimized for one-handed use on mobile

#### Screen Reader Support
- Semantic HTML structure
- ARIA labels on all buttons
- Meaningful alt text and descriptions

#### Motion Sensitivity
- Respects `prefers-reduced-motion` setting
- Animations can be disabled system-wide

#### High Contrast Mode
- Detects and respects system high contrast preferences
- Adds borders and enhanced visibility

### 📱 Mobile-Specific Features

#### Bottom Navigation Bar
- Quick access to "Today" and home
- Badge notifications for upcoming events
- Always visible for easy navigation

#### Optimized Layout
- Full-width design on mobile
- Larger touch targets
- Simplified header controls
- Calendar fills the screen efficiently

## 🛠️ Technical Details

### CSS Variables System
All colors, spacing, and radii are controlled through CSS variables, making it easy to customize:
- `--cal-bg`: Background color
- `--cal-text`: Primary text color
- `--cal-accent`: Interactive element color
- `--cal-spacing-*`: Consistent spacing scale
- `--cal-radius-*`: Border radius scale

### Theme Persistence
Themes and accessibility preferences are stored in `localStorage`:
- `calendar-theme`: Current theme (light/dark/auto)
- `color-blind-mode`: Color blind mode enabled/disabled

### Browser Support
- Modern browsers (Chrome, Firefox, Safari, Edge)
- iOS Safari 12+
- Android Chrome 90+
- Fallback support for older browsers

## 🎯 Usage Tips

1. **Finding Events**: Click any day to see events for that date
2. **Quick Today**: Click the year in top-left to return to today
3. **Theme Switching**: Use sun/moon icon for better visibility
4. **Color Blindness**: Enable eye icon for pattern-based event indicators
5. **Sharing**: URL stays on current month for easy sharing

## 🔄 Future Enhancements (Optional)
The design is ready for:
- Event creation/editing
- Calendar syncing
- Multiple calendar sources
- Event search functionality
- Export to iCal format

## 📝 Notes

- All animations use smooth cubic-bezier curves for iOS-like feel
- Shadow system creates depth and hierarchy
- San Francisco font stack matches Apple devices
- Print-friendly styles included
- Fully accessible with screen readers

---

**Enjoy your new iPhone-style calendar! 📅**
