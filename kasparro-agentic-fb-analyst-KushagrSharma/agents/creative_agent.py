class CreativeAgent:
    def generate_recommendations(self, bottom_campaigns):
        print("🎨 Creative Agent: Generating recommendations...")
        
        recommendations = {
            "creative_recommendations": [
                {
                    "target": "Low ROAS Campaigns",
                    "suggestions": [
                        "Refresh ad creatives with new visuals",
                        "Test different audience segments", 
                        "Implement urgency messaging in CTAs",
                        "Try carousel format for product showcases"
                    ]
                }
            ]
        }
        
        for suggestion in recommendations["creative_recommendations"][0]["suggestions"]:
            print(f"   💡 {suggestion}")
            
        return recommendations