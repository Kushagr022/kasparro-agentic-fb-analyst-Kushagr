class PlannerAgent:
    def plan(self, query):
        print("📋 Planner Agent: Breaking down query into tasks...")
        
        tasks = {
            "Analyze ROAS drop": [
                "Load and analyze Facebook Ads data",
                "Identify ROAS trends and drops", 
                "Find underperforming campaigns",
                "Generate hypotheses for ROAS drop",
                "Validate hypotheses with data",
                "Suggest new creative ideas for low-CTR campaigns"
            ]
        }
        
        selected_tasks = tasks.get(query, [])
        for i, task in enumerate(selected_tasks, 1):
            print(f"   Task {i}: {task}")
            
        return selected_tasks