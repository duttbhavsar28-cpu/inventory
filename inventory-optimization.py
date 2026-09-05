import numpy as np
import pandas as pd

def calculate_inventory_metrics(df, holding_cost_pct=0.20, order_cost=50.0, service_z=1.65):
    """
    df requires: ['sku', 'daily_demand_avg', 'daily_demand_std', 'lead_time_days', 
                  'unit_cost', 'current_stock']
    service_z: 1.65 corresponds to ~95% service level.
    """
    # Annual demand (assuming 365 business days)
    df['annual_demand'] = df['daily_demand_avg'] * 365
    df['annual_holding_cost'] = df['unit_cost'] * holding_cost_pct
    
    # EOQ = sqrt((2 * D * S) / H)
    df['eoq'] = np.sqrt((2 * df['annual_demand'] * order_cost) / df['annual_holding_cost']).round(0)
    
    # Safety Stock = Z * sqrt(LeadTime * (std_demand)^2)
    df['safety_stock'] = (service_z * np.sqrt(df['lead_time_days']) * df['daily_demand_std']).round(0)
    
    # Reorder Point = (LeadTime * AvgDailyDemand) + SafetyStock
    df['reorder_point'] = (df['lead_time_days'] * df['daily_demand_avg'] + df['safety_stock']).round(0)
    
    # Trigger purchase flag
    df['trigger_reorder'] = df['current_stock'] <= df['reorder_point']
    return df

# Example Data
data = {
    'sku': ['SKU-A101', 'SKU-B202', 'SKU-C303'],
    'daily_demand_avg': [25, 4, 60],
    'daily_demand_std': [5, 1.2, 12],
    'lead_time_days': [7, 14, 5],
    'unit_cost': [15.0, 120.0, 8.5],
    'current_stock': [190, 85, 310]
}
results = calculate_inventory_metrics(pd.DataFrame(data))
print(results[['sku', 'current_stock', 'reorder_point', 'eoq', 'trigger_reorder']])