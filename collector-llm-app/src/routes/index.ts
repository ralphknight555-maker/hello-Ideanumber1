import { Router } from 'express';
import { fetchPriceData, parsePriceData } from '../services/priceSources';
import { TgcScraper } from '../services/tgcScraper';
import { EarningsEstimator } from '../services/earningsEstimator';

const router = Router();

router.get('/prices', async (req, res) => {
    try {
        const priceData = await fetchPriceData();
        const parsedData = parsePriceData(priceData);
        res.json(parsedData);
    } catch (error) {
        res.status(500).json({ error: 'Failed to fetch price data' });
    }
});

router.get('/tgc', async (req, res) => {
    try {
        const scraper = new TgcScraper();
        const data = await scraper.scrapeData();
        res.json(data);
    } catch (error) {
        res.status(500).json({ error: 'Failed to scrape TGC data' });
    }
});

router.post('/estimate-earnings', async (req, res) => {
    try {
        const { priceData, tgcData } = req.body;
        const estimator = new EarningsEstimator();
        const earnings = estimator.estimateEarnings(priceData, tgcData);
        res.json({ earnings });
    } catch (error) {
        res.status(500).json({ error: 'Failed to estimate earnings' });
    }
});

export default router;