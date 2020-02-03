const puppeteer = require('puppeteer');

const performTest = async (
    screenshotFilename = 'results.png'
) => {
    // The URL of the test.
    const url = 'https://shopify-app.yottos.com/';

    // Launch the headless browser and create a new tab.
    const browser = await puppeteer.launch({
        //args: ['--no-sandbox', '--disable-setuid-sandbox'],
        headless: true
    });
    const page = await browser.newPage();
    await page.setUserAgent('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36');

    // Visit the page and take a screenshot.
    await page.goto(url);

    let [height, width] = await page.evaluate(() => {
        return [
            document.getElementsByTagName('html')[0].offsetHeight,
            document.getElementsByTagName('html')[0].offsetWidth
        ]
    })
    let progress = 0;
    while (progress < 100)
    {
        await page.mouse.move(progress, progress);
        progress++;
    }
    await page.mouse.move(width, height);
    await page.screenshot({
        path: screenshotFilename,
        clip: {
            x: 0,
            y: 0,
            width,
            height
        }
    });

    // Clean up the browser before exiting.
    await browser.close();
};

(async () => {
    await performTest();
})();