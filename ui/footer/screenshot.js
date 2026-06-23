const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
  console.log('Starting screenshot generation...');
  
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  
  try {
    const page = await browser.newPage();
    
    // Set viewport to iPhone X size (390 x 844)
    await page.setViewport({
      width: 390,
      height: 844,
      deviceScaleFactor: 2
    });
    
    // Navigate to local HTML file
    const filePath = path.join(__dirname, 'movie-footer-only-mockup.html');
    const fileURL = 'file://' + filePath.replace(/\\/g, '/');
    console.log('Loading:', fileURL);
    
    await page.goto(fileURL, { waitUntil: 'networkidle0' });
    
    // Wait a bit for rendering
    await page.waitForTimeout(500);
    
    // Capture screenshot
    const outputPath = path.join(__dirname, 'movie-footer-mockup.png');
    await page.screenshot({
      path: outputPath,
      type: 'png',
      omitBackground: false
    });
    
    console.log('✓ Screenshot saved:', outputPath);
    
  } catch (error) {
    console.error('Error:', error);
    process.exit(1);
  } finally {
    await browser.close();
  }
})();
