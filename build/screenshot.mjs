// Capture screenshots of the offline skills-library catalog for review.
// Usage: PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node build/screenshot.mjs
import { chromium } from 'playwright';
import { fileURLToPath } from 'url';
import { dirname, resolve } from 'path';
import { existsSync } from 'fs';

const here = dirname(fileURLToPath(import.meta.url));
const repo = resolve(here, '..');
const htmlPath = resolve(repo, 'dist/skills-library.html');
const outDir = resolve(repo, 'docs/screenshots');

const execCandidates = [
  process.env.CHROME_BIN,
  '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
].filter(Boolean);
const executablePath = execCandidates.find((p) => existsSync(p));

const browser = await chromium.launch({ executablePath, args: ['--no-sandbox'] });
const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
await page.goto('file://' + htmlPath, { waitUntil: 'networkidle' });

// 1. Full catalog, top of page.
await page.screenshot({ path: resolve(outDir, 'catalog-top.png') });

// 2. Full page, entire catalog.
await page.screenshot({ path: resolve(outDir, 'catalog-full.png'), fullPage: true });

// 3. An open entry dialog (the exemplar).
const card = page.locator('[data-id="gl-reconciler-break-triage"], #gl-reconciler-break-triage-dialog').first();
await page.evaluate(() => {
  const d = document.getElementById('gl-reconciler-break-triage-dialog');
  if (d && typeof d.showModal === 'function') d.showModal();
  else if (d) d.setAttribute('open', '');
});
await page.waitForTimeout(400);
await page.screenshot({ path: resolve(outDir, 'entry-dialog.png') });

await browser.close();
console.log('Wrote screenshots to', outDir);
