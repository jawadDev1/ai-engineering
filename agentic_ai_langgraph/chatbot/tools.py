from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
import requests
import os

# Tools
search_tool = DuckDuckGoSearchRun()

@tool
def calculator_tool(first_num: float, second_num: float, operation: str) -> dict:
    """
    Perform basic arithmetic operation on two numbers.
    Supported operations: add, sub, mul, div 
    """

    try:
        if operation == "add":
            result = first_num + second_num
        
        elif operation == "sub":
            result = first_num - second_num
        
        elif operation == "mul":
            result = first_num * second_num
        elif operation == "div":
            if second_num == 0:
                return {"error": "Division by zero is not allowed"}
            result = first_num / second_num
        else:
            return {"error": f"Unsupported operation '{operation}'"}

        return {
            "first_num": first_num,
            "second_num": second_num,
            "operation": operation,
            "result": result,
        }

    except Exception as e:
        return {"error": str(e)}

@tool
def get_stock_price_tool(symbol: str) -> dict:
    """
    Fetch latest stock price for a given symbol (e.g. 'AAPL', 'TSLA') 
    using Alpha Vantage with API Key in the url
    """
        
    apiKey = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={apiKey}'
    r = requests.get(url)
    return r.json()

