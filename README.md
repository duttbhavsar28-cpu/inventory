# Inventory Optimization

A Python implementation for calculating key inventory metrics including Economic Order Quantity (EOQ), Safety Stock, Reorder Point (ROP), and automated reorder triggers.

## Features

- **Economic Order Quantity (EOQ)**: Calculates optimal order quantity to minimize holding and ordering costs.
- **Safety Stock**: Determines buffer stock required to protect against demand fluctuations and lead-time variance.
- **Reorder Point (ROP)**: Identifies exact stock thresholds to trigger purchase orders based on average daily demand and lead time.
- **Reorder Trigger**: Automated boolean flags indicating when current stock falls below reorder points.

## Requirements

- Python 3.8+
- `numpy`
- `pandas`

## Usage

```bash
python inventory-optimization.py
```

### Output Example

```
        sku  current_stock  reorder_point     eoq  trigger_reorder
0  SKU-A101            190          197.0   552.0             True
1  SKU-B202             85           63.0    78.0            False
2  SKU-C303            310          344.0  1135.0             True
```
