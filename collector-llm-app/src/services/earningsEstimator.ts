export class EarningsEstimator {
    private priceData: any; // Replace 'any' with the appropriate type
    private tgcData: any; // Replace 'any' with the appropriate type

    constructor(priceData: any, tgcData: any) { // Replace 'any' with the appropriate type
        this.priceData = priceData;
        this.tgcData = tgcData;
    }

    estimateEarnings(): number {
        // Implement logic to estimate earnings based on priceData and tgcData
        let estimatedEarnings = 0;

        // Example calculation (replace with actual logic)
        estimatedEarnings = this.priceData.price * this.tgcData.quantity;

        return estimatedEarnings;
    }

    calculateProfit(cost: number): number {
        const earnings = this.estimateEarnings();
        return earnings - cost;
    }
}