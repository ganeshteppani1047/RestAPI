
# import sys
# import json

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/v1/add")
def add(x: float, y: float) -> dict:
    """
    Adds two numbers and returns the result.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        dict: A dictionary with operation details and the result.
    """
    return {
        "operation": "add",
        "status": "success",
        "x": x,
        "y": y,
        "result": x + y
    }

@app.get("/v1/subtract")
def subtract(x: float, y: float) -> dict:
    """
    Subtracts the second number from the first and returns the result.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        dict: A dictionary with operation details and the result.
    """
    return {
        "operation": "subtract",
        "status": "success",
        "x": x,
        "y": y,
        "result": x - y
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)



# if __name__ == "__main__":
#     x=sys.argv[1]
#     y=sys.argv[2]
#     print(add(int(x),int(y)))

# if __name__ == "__main__":
#     lines = sys.stdin.read().split()
#     x = int(lines[0])
#     y = int(lines[1])
#     print(add(x, y))

# import requests

# url = "https://open-weather13.p.rapidapi.com/city"

# querystring = {"city":"new york","lang":"EN"}

# headers = {
# 	"x-rapidapi-key": "f2bc195163mshbe4342df77c3b55p1e9887jsn13163b1033f8",
# 	"x-rapidapi-host": "open-weather13.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(json.dumps(response.json(), indent=1))
