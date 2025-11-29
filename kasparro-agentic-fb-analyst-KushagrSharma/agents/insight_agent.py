class InsightAgent:
    def analyze_campaign_performance(self, df):
        print("💡 Insight Agent: Analyzing campaign performance...")
        
        if df is not None:
            campaign_stats = df.groupby('campaign_name').agg({
                'roas': 'mean',
                'ctr': 'mean', 
                'spend': 'sum',
                'revenue': 'sum'
            }).round(2)
            top_3 = campaign_stats.nlargest(3, 'roas')
            bottom_3 = campaign_stats.nsmallest(3, 'roas')
            
            print("   🏆 Top 3 Campaigns by ROAS:")
            for campaign, data in top_3.iterrows():
                print(f"      - {campaign}: ROAS={data['roas']}, Spend=${data['spend']}")
                
            print("   📉 Bottom 3 Campaigns by ROAS:")
            for campaign, data in bottom_3.iterrows():
                print(f"      - {campaign}: ROAS={data['roas']}, Spend=${data['spend']}")
            
            return campaign_stats, top_3, bottom_3
        
        print("   ⚠️ No data available for analysis")
        return None, None, None