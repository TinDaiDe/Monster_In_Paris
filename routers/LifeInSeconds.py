from datetime import date
from fastapi import APIRouter, Request, HTTPException, Query
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse

# Import hàm tính toán từ folder project
from project.LifeInSeconds import calculate_life_stats

router = APIRouter(
    prefix="/life-in-seconds",
    tags=["Life In Seconds"]
)

# Khai báo đường dẫn tới folder templates ở thư mục gốc
templates = Jinja2Templates(directory="templates")

# 1. Route GET trả về giao diện HTML thông qua Jinja2
@router.get("/")
async def render_life_in_seconds(request: Request):
    return templates.TemplateResponse(
        request= request,
        name= "LifeInSeconds.html",
    )

# 2. API tính toán dữ liệu (fetch ngầm từ giao diện)
@router.get("/api/calculate")
async def calculate_endpoint(birth_date: date = Query(..., description="Ngày sinh YYYY-MM-DD")):
    try:
        data = calculate_life_stats(birth_date)
        return JSONResponse(status_code=200, content=None) #Sửa ở đây nữa nè
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi tính toán: {str(e)}")