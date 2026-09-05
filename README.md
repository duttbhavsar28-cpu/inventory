# 📦 Inventory Optimization — Dynamic Reorder & Stock Management

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Analytics-darkblue.svg)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Computation-blue.svg)](https://numpy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An operations analytics system that automates stock replenishment decisions by calculating **Economic Order Quantity (EOQ)**, **Safety Stock (95% service level)**, **Reorder Points (ROP)**, and dynamic replenishment alerts.

---

## 🎯 Business Problem

Balancing inventory is a critical operational challenge:
- **Excess Inventory**: Capital locked in storage space, insurance, and risk of depreciation or obsolescence.
- **Stock Depletion**: Backorders, unfulfilled orders, expedited shipping fees, and churned customers.

This engine programmatically continuously audits current warehouse levels against calculated safety buffers and lead-time demands.

---

## 🧮 Core Formulations

| Metric | Formula | Description |
| :--- | :--- | :--- |
| **Annual Demand ($D$)** | $D = \text{daily\_demand\_avg} \times 365$ | Projected annual unit consumption |
| **Annual Holding Cost ($H$)** | $H = \text{unit\_cost} \times \text{holding\_cost\_pct}$ | Carrying cost per unit per annum |
| **Economic Order Quantity ($\text{EOQ}$)** | $\sqrt{\frac{2 \times D \times S}{H}}$ | Batch order size that minimizes total setup and storage costs |
| **Safety Stock ($\text{SS}$)** | $Z \times \sqrt{L} \times \sigma_d$ | Buffer protecting against supplier delays & demand spikes ($Z=1.65 \approx 95\%$ service level) |
| **Reorder Point ($\text{ROP}$)** | $(L \times d) + \text{SS}$ | Exact inventory threshold to trigger purchase requisitions |
| **Reorder Trigger** | $\text{Current Stock} \le \text{ROP}$ | Automated boolean action flag for purchasing teams |

---

## 📦 Requirements

- Python 3.8+
- `numpy`
- `pandas`

Install required dependencies:
```bash
pip install numpy pandas
```

---

## 🚀 Quick Start & Usage

```bash
git clone https://github.com/duttbhavsar28-cpu/inventory.git
cd inventory
python inventory-optimization.py
```

### Script Execution Example

```python
import pandas as pd
from inventory_optimization import calculate_inventory_metrics

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
```

### Sample Output

```text
        sku  current_stock  reorder_point     eoq  trigger_reorder
0  SKU-A101            190          197.0   552.0             True
1  SKU-B202             85           63.0    78.0            False
2  SKU-C303            310          344.0  1135.0             True
```

---

## 🗣️ 30-Second Interview Pitch

> *"I developed an inventory optimization module that calculates Safety Stock, Reorder Points, and Economic Order Quantities (EOQ) across product lines. By analyzing demand variance and lead times, it flags at-risk SKUs and triggers automated replenishment alerts—maintaining a 95% customer service level while minimizing warehouse holding costs."*

---

## 📄 License

Distributed under the MIT License.
