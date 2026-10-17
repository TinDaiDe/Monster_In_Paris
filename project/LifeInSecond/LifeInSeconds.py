from datetime import datetime, date
from typing import Dict, Any

def calculate_life_stats(birth_date: date) -> Dict[str, Any]:
    """
    Tính toán toàn bộ các thống kê cuộc đời dựa trên ngày sinh.
    Chuẩn hóa toàn bộ thời gian thành giây.
    """
    now = datetime.now()
    birth_datetime = datetime.combine(birth_date, datetime.min.time())
    
    diff = now - birth_datetime
    total_seconds = int(diff.total_seconds())
    
    if total_seconds < 0:
        raise ValueError("Ngày sinh không thể nằm ở tương lai!")

    # Các hằng số quy đổi cơ bản
    total_minutes = total_seconds / 60
    total_hours = None
    total_days = None
    total_years = None
    # 1. Nhịp tim: trung bình ~72 - 80 nhịp/phút (~1.25 nhịp/giây)
    heartbeats = int(total_seconds * 1.25)
    
    # 2. Chớp mắt: trung bình ~17 lần/phút (~0.283 lần/giây, không tính lúc ngủ)
    # Giả định ngủ 8 tiếng (chớp mắt trong 16 tiếng thức mỗi ngày = 2/3 thời gian)
    waking_seconds = None
    blinks = None
    
    # 3. Hít thở: trung bình ~14 lần/phút
    breaths = None
    
    # 4. Thời gian ngủ: trung bình 1/3 cuộc đời (~8 tiếng/ngày)
    sleep_days = None
    
    # 5. Số bữa cơm: trung bình 3 bữa/ngày
    meals = None
    
    # 6. Lượng nước uống: trung bình ~2 lít/ngày
    water_liters = None
    
    # 7. Số bước chân: trung bình ~5,000 bước/ngày
    steps = None
    
    # 8. Số giấc mơ: trung bình 4 giấc mơ mỗi đêm
    dreams = None

    return {
        "birth_date": birth_date.strftime("%Y-%m-%d"),
        "total_seconds": total_seconds,
        "total_days": None #Sửa ở đây nữa nè
        "total_years": round(total_years, 2),
        "stats": [
            {
                "id": "heartbeats",
                "label": "Nhịp tim đã đập",
                "value": heartbeats,
                "unit": "nhịp",
                "desc": "Trung bình 75 nhịp mỗi phút"
            },
            {
                "id": "blinks",
                "label": "Bạn đã chớp mắt",
                "value": blinks,
                "unit": "lần",
                "desc": "Khoảng 17 lần mỗi phút khi thức"
            },
            {
                "id": "breaths",
                "label": "Số lần hít thở",
                "value": breaths,
                "unit": "lần",
                "desc": "Trung bình 14 nhịp thở/phút"
            },
            {
                "id": "sleep_days",
                "label": "Thời gian đã dành để ngủ",
                "value": sleep_days,
                "unit": "ngày",
                "desc": "Chiếm gần 1/3 cuộc đời của bạn"
            },
            {
                "id": "meals",
                "label": "Bữa cơm đã ăn",
                "value": meals,
                "unit": "bữa",
                "desc": "Ước tính 3 bữa ngon miệng mỗi ngày"
            },
            {
                "id": "water",
                "label": "Nước đã uống",
                "value": water_liters,
                "unit": "lít",
                "desc": "Đủ để làm đầy vài bể bơi mini"
            },
            {
                "id": "steps",
                "label": "Bước chân đã đi",
                "value": steps,
                "unit": "bước",
                "desc": "Tương đương hàng ngàn cây số"
            },
            {
                "id": "dreams",
                "label": "Giấc mơ đã trải qua",
                "value": dreams,
                "unit": "giấc mơ",
                "desc": "Dù phần lớn ta đều quên sạch khi thức dậy"
            }
        ]
    }