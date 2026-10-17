# 2. Request và Response

Hai bên nói chuyện với nhau bằng một "ngôn ngữ chung" tên là **HTTP**. Mỗi lượt nói chuyện gồm **một request và một response**.

## Request (client gửi lên)

Gồm các phần chính:

| Phần | Ý nghĩa | Ví dụ |
|---|---|---|
| **Method** | Muốn làm gì | `GET`, `POST` |
| **URL** | Gọi tới đâu | `/api/so-sanh?chieu_cao_m=1.5` |
| **Body** (không bắt buộc) | Dữ liệu gửi kèm | thông tin nhập trong form |

Hai method cần biết:
- **GET:** lấy thông tin về (xem trang, tra kết quả).
- **POST:** gửi dữ liệu lên để server xử lý hoặc lưu (nộp form).

## Response (server trả về)

| Phần | Ý nghĩa | Ví dụ |
|---|---|---|
| **Status code** | Kết quả chung | `200` |
| **Body** | Nội dung trả về | trang HTML, hoặc dữ liệu JSON |

## Status code hay gặp

| Mã | Nghĩa | Gặp khi nào |
|---|---|---|
| `200` | Thành công | mọi thứ ổn |
| `404` | Không tìm thấy | gõ sai đường dẫn |
| `422` | Dữ liệu gửi lên sai kiểu | (FastAPI) gửi chữ vào chỗ cần số |
| `500` | Lỗi phía server | **code Python của bạn bị lỗi** |

Khi bạn thấy `500`, hãy nhìn vào cửa sổ terminal đang chạy server: lỗi Python sẽ được in ra ở đó.

## JSON: định dạng dữ liệu để trao đổi

JSON trông gần giống `dict` của Python:

```json
{"ket_qua": 6.0, "vat_the": "meo"}
```

Server Python trả về một `dict`, FastAPI tự đổi thành JSON, và JavaScript ở trình duyệt đọc được.

## Một lượt nói chuyện hoàn chỉnh

```
Request:   GET /api/so-sanh?chieu_cao_m=1.5&vat_the=meo
Response:  200 OK
           {"ket_qua": 6.0}
```

## Mẹo: xem tận mắt

Mở bất kỳ trang web nào, nhấn **F12**, chọn tab **Network**, rồi tải lại trang. Bạn sẽ thấy danh sách request mà trình duyệt vừa gửi, kèm status code của từng cái.

## Tự kiểm tra

1. `GET` và `POST` khác nhau thế nào?
2. Thấy mã `500` thì nên tìm lỗi ở đâu?
3. JSON giống kiểu dữ liệu nào của Python?