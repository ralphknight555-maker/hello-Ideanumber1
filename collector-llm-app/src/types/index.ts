export interface PriceData {
    source: string;
    price: number;
    dateFetched: Date;
}

export interface EarningsInfo {
    totalEarnings: number;
    totalCosts: number;
    profit: number;
}

export interface TgcData {
    itemName: string;
    itemPrice: number;
    sellerInfo: string;
}

export type PriceSource = 'PriceCharter' | 'TGCWebsite';