from enum import Enum
from typing import List,Optional
from fastapi import FastAPI, Query, Header
from fastapi.responses import JSONResponse

import json
 

TEST_JWT="Bearer AQIC5wM2LY4SfczUhgppPLcqjZcE3QRslouqN3kUfnssBUQ.*AAJTSQACMDIAAlNLABM3NTQzNTMxNjcxNDgxNjI3NzYxAAJTMQACMDE.*"


app = FastAPI()

def open_resp(filename="response.json"):
    # открываем файл с примером response
    f = open(filename, encoding="utf-8")
    data = json.load(f)
    f.close()
    return data

    
class SortField(str, Enum):
    create_at = "create_at"
    update_at = "update_at"


class Order(str, Enum):
    asc = "asc"
    desc = "desc" 





@app.get("/orders")
def orders(filter_date_from: str,filter_date_to: str,sort_field: SortField,page_size: int,page_number: int,Authorization: str = Header(None),client_id: str = Query(..., max_length=100),user_id: Optional[str] = Query(None, max_length=100),tab: Optional[List[str]] = Query(None),type: Optional[List[str]] = Query(None),state: Optional[List[str]] = Query(None),filter_search: Optional[str] = Query(None, max_length=100),order: Optional[Order]=None):
    #мокаем ошибки валидации параметров запроса
    if page_size<1 or page_size>100:
        return JSONResponse(status_code=422, content={"trace":"some code","message":"page size must be between 1-100 including 1 and 100","code":"422","more_info":"more info","type":"form_validation"})
    
    if Authorization != TEST_JWT:
        return JSONResponse(status_code=401, content={"trace":"some code","message":"Unauthorized","code":"401","more_info":"more info","type":"system"})
    
    
    data = open_resp()
    return JSONResponse(status_code=200, content=data)
    
