window.legacyShowCookieBar({
  content: 'your-cookie-bar-html',
  cookie_groups: ['your-cookie-group'],
  cookie_decline: 'your-decline-cookie-setting',
  beforeDeclined: function () {
  // your code to run before the user declines
  },
});