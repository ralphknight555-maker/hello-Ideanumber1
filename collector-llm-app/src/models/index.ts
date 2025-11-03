export interface PriceData {
    id: string;
    source: string;
    price: number;
    dateFetched: Date;
}

export interface EarningsInfo {
    totalEarnings: number;
    totalCosts: number;
    profit: number;
    dateCalculated: Date;
}