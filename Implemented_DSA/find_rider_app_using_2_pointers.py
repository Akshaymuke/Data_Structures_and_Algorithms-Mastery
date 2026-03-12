from fastapi import FastAPI, Query, HTTPException
from typing import List

# Mock data: A pre-sorted list of available driver prices
DRIVER_PRICES = [12.5, 15.0, 22.0, 25.5, 30.0, 45.0, 55.0, 75.0, 100.0]

# 1. Initialize the app
app = FastAPI()

@app.get("/")
def read_root():
    return "Hello Passenger!! How are you ?"

@app.get("/search_rides")
async def available_rides(min_price:int ,max_price:int):
    # two pointers implementation
    left = 0
    right = len(DRIVER_PRICES) - 1

    # Move left pointer forward to find the first price >= min_price
    while left <= right and DRIVER_PRICES[left] < min_price:
        left += 1

    # Move right pointer backward to find the last price <= max_price
    while right >= left and DRIVER_PRICES[right] > max_price:
        right -= 1

    # The valid range is everything between 'left' and 'right' (inclusive)
    # If left > right, it means no prices fell within the range
    if left > right:
        return {
            "min_selected": min_price,
            "max_selected": max_price,
            "available_rides": []
        }

    # Slicing the sorted list to get the results
    results = DRIVER_PRICES[left : right + 1]
    return {
        "min_selected_price": min_price,
        "max_selected_price": max_price,
        "count of rides available": len(results),
        "available_rides": results
    }
