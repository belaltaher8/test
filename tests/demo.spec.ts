import { test, expect } from '@playwright/test';
import path from 'path';

const pageUrl = `file://${path.resolve(__dirname, '../index.html')}`;

test.describe('Playwright Demo Page', () => {
  test('has correct title', async ({ page }) => {
    await page.goto(pageUrl);
    await expect(page).toHaveTitle('Playwright Demo');
  });

  test('displays heading', async ({ page }) => {
    await page.goto(pageUrl);
    await expect(page.locator('h1')).toHaveText('Hello, Playwright!');
  });

  test('greets with custom name', async ({ page }) => {
    await page.goto(pageUrl);
    await page.fill('#name-input', 'Alice');
    await page.click('#greet-btn');
    await expect(page.locator('#message')).toHaveText('Hello, Alice!');
  });

  test('greets with default message when no name entered', async ({ page }) => {
    await page.goto(pageUrl);
    await page.click('#greet-btn');
    await expect(page.locator('#message')).toHaveText('Hello, World!');
  });
});
