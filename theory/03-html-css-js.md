# 3. HTML, CSS, JavaScript

Một trang web được ghép từ ba thứ, mỗi thứ lo một việc:

| Thành phần | Lo việc gì | Ví dụ ẩn dụ |
|---|---|---|
| **HTML** | Có **cái gì** trên trang (tiêu đề, ô nhập, nút) | Bộ xương |
| **CSS** | Trông **thế nào** (màu, cỡ chữ, vị trí) | Quần áo |
| **JavaScript** | **Làm gì** khi người dùng thao tác | Cơ bắp |

## Điều quan trọng nhất

> **HTML, CSS và JavaScript chạy ở trình duyệt của người chơi. Python chạy trên server.**

JavaScript **không gọi trực tiếp** được hàm Python. Nó phải gửi một **request** lên server, rồi nhận **response** về.

## Một trang nhỏ hoàn chỉnh

```html
<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <title>Bạn cao bao nhiêu</title>
  <style>
    body { font-family: sans-serif; text-align: center; margin-top: 50px; }
    button { padding: 8px 16px; font-size: 16px; }
    #ketqua { color: teal; font-size: 24px; }
  </style>
</head>
<body>
  <h1>Bạn cao bao nhiêu?</h1>
  <input id="chieucao" type="number" step="0.01" placeholder="Chiều cao (m)">
  <button id="nut">So sánh</button>
  <p id="ketqua"></p>

  <script>
    document.getElementById("nut").addEventListener("click", async () => {
      const m = document.getElementById("chieucao").value;
      const res = await fetch(`/api/so-sanh?chieu_cao_m=${m}&vat_the=meo`);
      const data = await res.json();
      document.getElementById("ketqua").textContent =
        `Bạn bằng ${data.ket_qua} con mèo`;
    });
  </script>
</body>
</html>
```

Đọc từng khối:
- Phần trong `<style>` là **CSS** (đổi màu, cỡ chữ).
- Các thẻ trong `<body>` là **HTML** (tiêu đề, ô nhập, nút, đoạn chữ).
- Phần trong `<script>` là **JavaScript**: khi bấm nút, gửi request bằng `fetch`, nhận JSON, rồi ghi kết quả lên trang.

Bạn **không cần tự viết** những thứ này (có thể nhờ AI), nhưng nên đọc hiểu được nó đang làm gì.

## Tự kiểm tra

1. Thứ nào quyết định màu của chữ: HTML, CSS hay JavaScript?
2. Code JavaScript chạy ở đâu: trình duyệt hay server?
3. `fetch(...)` trong ví dụ để làm gì?