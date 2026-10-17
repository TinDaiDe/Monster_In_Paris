# 1. Client và Server

## Ví dụ ở quán ăn

| Ở quán ăn | Trên web |
|---|---|
| Khách ngồi bàn | **Client** (trình duyệt của người chơi) |
| Bếp | **Server** (máy chạy code Python của bạn) |
| Khách gọi món | **Request** (yêu cầu) |
| Bếp đem món ra | **Response** (phản hồi) |

Khách không vào bếp, bếp không tự đem món ra khi chưa ai gọi. **Client luôn là bên hỏi trước, server là bên trả lời.**

## Client là gì?

Là bên **gửi yêu cầu**. Thường là trình duyệt (Chrome, Safari...) hoặc app trên điện thoại.

## Server là gì?

Là một **chương trình luôn chạy và chờ yêu cầu**, thường nằm trên một máy tính nào đó. Nó nhận yêu cầu, xử lý (có thể gọi hàm Python của bạn), rồi trả kết quả về.

Điều hay là server **không phải là một cỗ máy bí ẩn**. Máy tính của bạn khi chạy FastAPI cũng đang là server (địa chỉ thường là `localhost` hoặc `127.0.0.1`, nghĩa là "chính máy này").

## Địa chỉ trang web (URL)

```
https://vi-du.com/api/so-sanh?chieu_cao_m=1.5
└─┬──┘  └───┬───┘ └───┬────┘ └──────┬───────┘
 giao   tên miền  đường dẫn   dữ liệu gửi kèm
 thức   (máy nào) (chức năng nào)
```

- **Tên miền** cho biết gọi tới máy nào.
- **Đường dẫn** cho biết muốn dùng chức năng nào trên máy đó.
- Phần sau dấu `?` là dữ liệu gửi kèm.

## Trong dự án của chúng ta

- **Client:** trình duyệt của người chơi.
- **Server:** máy chạy FastAPI, bên trong có các hàm Python của các bạn.

## Tự kiểm tra

1. Bên nào luôn gửi yêu cầu trước, client hay server?
2. Máy tính của mình có thể vừa là client vừa là server không?
3. Trong `https://vi-du.com/api/so-sanh`, đâu là tên miền và đâu là đường dẫn?