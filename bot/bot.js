const puppeteer = require('puppeteer');

const performTest = async (
    screenshotFilename = 'results.png'
) => {
    // The URL of the test.
    const url = 'http://0.0.0.0:6543/';

    // Launch the headless browser and create a new tab.
    const browser = await puppeteer.launch({
        //args: ['--no-sandbox', '--disable-setuid-sandbox'],
        //headless: true
    });
    const page = await browser.newPage();

    // Visit the page and take a screenshot.
    await page.goto(url);

    let [height, width] = await page.evaluate(() => {
        return [
            document.getElementsByTagName('html')[0].offsetHeight,
            document.getElementsByTagName('html')[0].offsetWidth
        ]
    })
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