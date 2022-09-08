glowCookies.start('en', { 
  analytics: 'G-XXX', 
  facebookPixel: 'XXX',
  HotjarTrackingCode: 'xxx',
  customScript: [{ type: 'custom', position: 'body', content: 'console.log('custom script');' }],
  // or 
  customScript: [{ type: 'src', position: 'head', content: 'https://www.googletagmanager.com/gtag/js?id=G-FH87DE17XF' }]
});

glowCookies.start('en', { 
  policyLink: 'https://www.privacypolicygenerator.info/live.php?token=pv9dRiKKr2GFN3kv7aNg3HgdE8lL288d'
  });

  glowCookies.start('en', { 
    style: 1, // 1, 2, 3
    hideAfterClick: true,
    border: 'none', // or 'border'
    position: 'right', // or 'left'
    bannerDescription: 'banner desc',
    bannerLinkText: 'banner link text',
    bannerBackground: '#000',
    bannerColor: '#fafafa',
    bannerHeading: '<h2>Cookies</h2>',
    acceptBtnText: 'accept btn text',
    acceptBtnColor: 'green',
    acceptBtnBackground: 'red',
    rejectBtnText: 'reject btn text',
    rejectBtnBackground: 'lightblue',
    rejectBtnColor: 'blue',
    manageColor: 'white',
    manageBackground: 'blue',
    manageText: 'cookies text'
  });