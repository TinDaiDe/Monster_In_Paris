## Đời bạn tính bằng giây

**Ý tưởng:** nhập ngày sinh, máy cho biết bạn đã sống bao nhiêu giây, rồi quy ra những thứ đời thường.

**Đầu vào:** ngày sinh (dạng `năm-tháng-ngày`, ví dụ `2007-05-20`).

**Đầu ra:** một bảng gồm
- Tổng số giây đã sống
- Đã chớp mắt bao nhiêu lần
- Đã ngủ bao nhiêu ngày
- Đã ăn bao nhiêu bữa cơm
- Tim đã đập bao nhiêu lần
- ... (các bạn tự thêm)

**Các bước:**
1. Đọc ngày sinh, chuyển thành đối tượng `datetime`.
2. Lấy thời điểm hiện tại, trừ đi ngày sinh để ra khoảng thời gian.
3. Quy toàn bộ khoảng đó ra **giây**.
4. Từ số giây, tính các chỉ số bằng các hằng số ước lượng.

**Hằng số gợi ý (ước lượng vui, các bạn có thể đổi):**

| Hằng số | Giá trị |
|---|---|
| Chớp mắt | 15 lần/phút (chỉ tính lúc thức) |
| Thời gian thức | 16 giờ/ngày |
| Thời gian ngủ | 8 giờ/ngày |
| Bữa cơm | 3 bữa/ngày |
| Nhịp tim | 70 lần/phút |