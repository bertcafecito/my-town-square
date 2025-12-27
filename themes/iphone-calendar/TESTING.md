# iPhone Calendar Theme - Testing Guide

## Testing Checklist

### ✅ Basic Page Loading
1. **Home Page** - http://localhost:1313/
   - Should load with PaperMod theme
   - Navigation menu should be visible
   - Links to Calendar, About, and Support should work

2. **Calendar Page** - http://localhost:1313/calendar/
   - Should load with iPhone Calendar theme
   - Calendar grid should be visible
   - Current month should be displayed

3. **About Page** - http://localhost:1313/about/
   - Should load with PaperMod theme
   - Content should be readable

4. **Support Page** - http://localhost:1313/support/
   - Should load with PaperMod theme
   - Content should be readable

### ✅ Calendar Functionality

#### Month Navigation
- [ ] Click **Previous Month** button (←) - should navigate to previous month
- [ ] Click **Next Month** button (→) - should navigate to next month
- [ ] Click **Back to Today** button - should return to current month
- [ ] Year should update when changing months

#### Event Display
- [ ] Days with events should show colored dots (up to 3 dots)
- [ ] Days with more than 3 events should show "+N" indicator
- [ ] Today's date should have a red circle
- [ ] Clicking on a day should show events for that day
- [ ] Selected day should be highlighted

#### Event List
- [ ] Events should display with time
- [ ] All-day events should show "all-day"
- [ ] Events should have colored bars
- [ ] Events should be sorted by time
- [ ] Days without events should show "No events" message

#### Theme Controls
- [ ] Click **Theme Toggle** (☀️/🌙) button
  - Should cycle through: Light → Dark → Auto
  - Calendar colors should change
  - Theme preference should be saved in localStorage
  
- [ ] Click **Color Blind Mode** (👁️) button
  - Should toggle enhanced contrast
  - Event dots should show patterns
  - Should be saved in localStorage

#### Responsive Design
- [ ] Desktop (1440px+): Full layout with all features
- [ ] Tablet (768px-1023px): Adjusted spacing
- [ ] Mobile (< 768px): Compact layout, bottom navigation visible
- [ ] Touch interactions work on mobile devices

### ✅ Data Loading
- [ ] Browser console shows "Event data loaded:" message
- [ ] Events from `data/aggregate_feed/*.json` files are loaded
- [ ] Events appear on correct dates
- [ ] Multiple months of data are accessible

### ✅ Accessibility
- [ ] Keyboard navigation works (Tab, Enter)
- [ ] Focus indicators are visible
- [ ] Screen readers can access content
- [ ] Color contrast meets WCAG 2.1 AA standards
- [ ] Touch targets are at least 44x44px

### ✅ Performance
- [ ] Calendar loads in < 1 second
- [ ] No console errors
- [ ] CSS is minified and fingerprinted
- [ ] Smooth animations and transitions

## Browser Testing

Test in the following browsers:
- [ ] Chrome/Edge (latest)
- [ ] Firefox (latest)
- [ ] Safari (latest)
- [ ] Mobile Safari (iOS)
- [ ] Chrome Mobile (Android)

## Known Issues

None currently. If you find any issues, please report them!

## Quick Test Commands

```bash
# Start development server
hugo server -D

# Build for production
hugo --minify

# Check for build errors
hugo --logLevel debug
```

## Visual Verification

1. **Calendar Grid**
   - 7 columns (Sunday-Saturday)
   - Days properly aligned
   - Event dots visible and colored
   - Today indicator (red circle) on current date

2. **Event Cards**
   - Left color bar matches event color
   - Time displayed correctly
   - Title is readable
   - Hover effect works

3. **Theme Switching**
   - Light mode: White background, black text
   - Dark mode: Black background, white text
   - Colors adjust for theme
   - Smooth transition

## Event Data Format Test

Test with this sample event in `data/aggregate_feed/202512.json`:

```json
[
  {
    "summary": "Test Event",
    "start": "2025-12-26T14:00:00+00:00",
    "end": "2025-12-26T16:00:00+00:00"
  }
]
```

This should appear:
- As a colored dot on December 26
- In the event list with time "2:00 PM – 4:00 PM"
- With one of 8 color schemes

## Success Criteria

✅ All pages load without errors
✅ Calendar displays current month
✅ Events are visible on calendar
✅ Month navigation works
✅ Theme toggle works
✅ Events list updates when clicking days
✅ Responsive layout works on mobile
✅ No console errors
✅ Performance is smooth

## Troubleshooting

**Calendar not showing events:**
- Check browser console for errors
- Verify data files exist in `data/aggregate_feed/`
- Ensure JSON is valid
- Check that Hugo server restarted after data changes

**Styling issues:**
- Clear browser cache
- Check that `main.css` is loading
- Verify no CSS conflicts
- Check browser console for 404 errors

**Month navigation not working:**
- Check browser console for JavaScript errors
- Verify event listeners are attached
- Test in different browser

**Theme toggle not working:**
- Check localStorage is enabled
- Verify JavaScript is running
- Check for console errors
