import pandas as pd

class DataAgent:
    def load_and_analyze_data(self, filepath):
        print("📊 Data Agent: Loading and analyzing dataset...")
        try:
            df = pd.read_csv(filepath)
            print(f"   ✅ Dataset loaded: {len(df)} rows, {len(df.columns)} columns")
            
            # Basic analysis
            total_campaigns = df['campaign_name'].nunique()
            date_range = f"{df['date'].min()} to {df['date'].max()}"
            avg_roas = df['roas'].mean()
            avg_ctr = df['ctr'].mean()
            
            print(f"   📊 Total Campaigns: {total_campaigns}")
            print(f"   📅 Date Range: {date_range}")
            print(f"   💰 Average ROAS: {avg_roas:.2f}")
            print(f"   🎯 Average CTR: {avg_ctr:.2f}%")
            
            return df, total_campaigns, date_range, avg_roas, avg_ctr
            
        except FileNotFoundError:
            print("   ❌ Dataset file not found.")
            return None, 0, "", 0, 0