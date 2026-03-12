from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import HTMLResponse # Added for UI
from typing import List

# Mock data
DRIVER_PRICES = [12.5, 15.0, 22.0, 25.5, 30.0, 45.0, 55.0, 75.0, 100.0]

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    # We use a simple HTML form that sends data to /search_rides
    return """
    <html>
        <head>
            <title>Ride Search</title>
            <style>
                body { font-family: sans-serif; margin: 40px; line-height: 1.6; }
                .container { max-width: 400px; padding: 20px; border: 1px solid #ddd; border-radius: 8px; }
                input { width: 100%; padding: 8px; margin: 10px 0; display: block; }
                button { background-color: #007bff; color: white; border: none; padding: 10px 20px; cursor: pointer; width: 100%; border-radius: 4px; }
                button:hover { background-color: #0056b3; }
            </style>
        </head>
        <body>
            <div class="container">
                <h2>Hello Passenger!!</h2>
                <p>Find a ride that fits your budget:</p>
                <form action="/search_rides" method="get">
                    <label>Minimum Price:</label>
                    <input type="number" name="min_price" value="0" required>
                    
                    <label>Maximum Price:</label>
                    <input type="number" name="max_price" value="100" required>
                    
                    <button type="submit">Search Rides</button>
                </form>
            </div>
        </body>
    </html>
    """

@app.get("/search_rides")
async def available_rides(min_price: int, max_price: int):
    # Your existing two-pointer logic
    left = 0
    right = len(DRIVER_PRICES) - 1

    while left <= right and DRIVER_PRICES[left] < min_price:
        left += 1

    while right >= left and DRIVER_PRICES[right] > max_price:
        right -= 1

    if left > right:
        return {
            "min_selected": min_price,
            "max_selected": max_price,
            "available_rides": []
        }

    results = DRIVER_PRICES[left : right + 1]
    return {
        "min_selected_price": min_price,
        "max_selected_price": max_price,
        "count_of_rides_available": len(results),
        "available_rides": results
    }