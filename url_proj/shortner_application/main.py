from fastapi import FastAPI, HTTPException

app = FastAPI()

def raise_bad_req(message):
    raise HTTPException(status_code=400, detail=message)

@app.get("/check_num/{num}")
def check_if_evenOdd(num):
    try:
        num = int(num)
    except Exception as e:
        return "wrong type, integer only"    
    if num%2 == 0:
        return f"{num} is even"
    else:
         return f"{num} is odd"   


