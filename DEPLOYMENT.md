# Deployment Checklist

Before deploying My Town Square to production, complete the following tasks:

## Configuration

- [ ] Update `baseURL` in `hugo.toml` to your production URL
- [ ] Update `robots.txt` in `static/` folder with production sitemap URL
- [ ] Verify all menu links work correctly
- [ ] Test social media links (if added)

## Content Review

- [ ] Review all page content for typos and accuracy
- [ ] Verify calendar data is up-to-date
- [ ] Check that About page reflects current information
- [ ] Ensure Support page has correct contribution methods

## Technical Checks

- [ ] Run `hugo --minify` successfully builds site
- [ ] Test site on multiple browsers (Chrome, Firefox, Safari, Edge)
- [ ] Test responsive design on mobile devices
- [ ] Verify calendar functionality works (navigation, event display)
- [ ] Check for any console errors in browser dev tools
- [ ] Test dark mode switching
- [ ] Verify all images load correctly (if any)

## SEO & Performance

- [ ] Verify meta descriptions are present
- [ ] Check sitemap.xml is generated
- [ ] Test page load speed
- [ ] Validate HTML (https://validator.w3.org/)
- [ ] Check accessibility (screen readers, keyboard navigation)

## Data & Scripts

- [ ] Run data fetching scripts to ensure latest events
- [ ] Verify event data displays correctly on calendar
- [ ] Set up automated data updates (cron job or GitHub Actions)
- [ ] Check that date/time formats are correct

## Deployment

- [ ] Choose hosting platform (GitHub Pages, Netlify, Vercel, etc.)
- [ ] Set up custom domain (if applicable)
- [ ] Configure HTTPS/SSL certificate
- [ ] Test production deployment
- [ ] Set up analytics (optional)
- [ ] Configure backup strategy

## Post-Launch

- [ ] Monitor for errors or issues
- [ ] Collect user feedback
- [ ] Plan regular content updates
- [ ] Schedule periodic event data refreshes

## Notes

_Add any specific notes or customizations for your deployment here_
