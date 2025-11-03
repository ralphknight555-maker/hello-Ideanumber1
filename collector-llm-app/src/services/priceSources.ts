import axios from 'axios';

export interface PriceData {
    source: string;
    price: number;
    date: string;
}

export async function fetchPriceData(sourceUrl: string): Promise<PriceData[]> {
    try {
        const response = await axios.get(sourceUrl);
        return parsePriceData(response.data);
    } catch (error) {
        console.error('Error fetching price data:', error);
        throw new Error('Failed to fetch price data');
    }
}

export function parsePriceData(data: any): PriceData[] {
    // Implement parsing logic based on the structure of the data received
    const prices: PriceData[] = [];
    
    // Example parsing logic (this should be customized based on actual data structure)
    data.forEach((item: any) => {
        prices.push({
            source: item.source,
            price: item.price,
            date: item.date,
        });
    });

    return prices;
}