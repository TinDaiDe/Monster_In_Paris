# Monster_In_Paris
(Cre: công nghệ hắc ám)
> **Quy ước chung:** phần **Python** các bạn tự viết. Phần web (HTML, CSS, FastAPI) anh lo, hoặc nhờ AI viết.

## Đọc theo thứ tự này

1. Folder **`theory/`**: đọc nhanh khoảng 20 phút để hiểu mình đang làm gì (server, client, request, response, HTML/CSS/JS).
2. File **`project/readme.md`**: danh sách và đề bài các project.
3. File README này: biết chỗ nào được sửa, chạy thử thế nào.

---

## Cấu trúc thư mục

```
Monster_In_Paris/
├── MainServer.py              Điểm khởi động của web server
├── routers/                   🔴 "Biển chỉ đường": nối địa chỉ web với code Python
│   ├── __init__.py
│   ├── home.py                   trang chủ
│   └── LifeInSeconds.py          nối trang LifeInSeconds với code trong project/
├── project/                   🟢 NƠI CÁC BẠN LÀM VIỆC
│   ├── readme.md                 danh sách và đề bài
│   └── LifeInSecond/
│       └── LifeInSeconds.py      file có chỗ trống (TODO) để các bạn điền
├── templates/                 🟡 Giao diện HTML
│   ├── index.html
│   └── LifeInSeconds.html
├── static/images/             🟡 Ảnh, logo
├── theory/                    📖 Lý thuyết, chỉ đọc
├── .venv/                     🔴 Môi trường ảo, đừng mở ra sửa
└── README.md                  File này
```

(`__pycache__/` là thư mục Python tự tạo, cứ bỏ qua.)

---

## Ai được sửa gì

| Ký hiệu | Nghĩa | Gồm những gì |
|---|---|---|
| 🟢 **Các bạn tự sửa** | Đây là phần bài làm của các bạn | `project/<tên project>/*.py` |
| 🟡 **Chỉ sửa khi anh yêu cầu** | Anh hoặc AI lo. Bạn nào muốn đổi giao diện thì nhắn anh trước | `templates/`, `static/` |
| 🔴 **Không đụng vào** | Sửa nhầm là cả web có thể sập, ảnh hưởng tới mọi người | `MainServer.py`, `routers/`, `.venv/` |

Muốn **thêm project mới** hoặc **thêm một trang mới**: nhắn anh. Anh sẽ tạo phần nối vào web (router, trang HTML), các bạn chỉ cần viết phần Python.

---

## Cách làm một project

Ví dụ với `project/LifeInSecond/LifeInSeconds.py`:

1. Mở file, tìm các chỗ có comment **`TODO`**. Đây là chỗ anh đã xóa code để các bạn tự viết.
2. Chỉ viết vào các chỗ `TODO`. Đọc comment hướng dẫn ngay phía trên, nó nói hàm cần nhận gì và trả về gì.
3. **Giữ nguyên tên hàm, tên tham số, thứ tự tham số.** Phần `routers/` gọi các hàm theo đúng tên, đổi tên là web không chạy.
4. Hàm **không dùng `input()` và `print()`**. Hàm nhận tham số và `return` kết quả (lý do ở `theory/04-python-trong-web.md`).
5. Dùng thư viện có sẵn của Python là đủ. Cần thư viện ngoài thì hỏi anh trước.
6. Test bằng terminal trước (nếu cuối file có phần chạy thử `if __name__ == "__main__":` thì chạy `python project/LifeInSecond/LifeInSeconds.py`), rồi mới bật web để xem kết quả thật.

### Chuyện file bị "đỏ" trong VS Code

Một số file/thư mục đang hiện màu đỏ. **Đó là bình thường, không phải bạn làm hỏng.** Anh đã xóa bớt code và để lại comment, nên VS Code báo lỗi vì đang thiếu. Viết xong các chỗ `TODO` thì hết đỏ.

Nếu bạn đã viết xong mà vẫn đỏ, mở tab **Problems** (`Ctrl + Shift + M`) để đọc lỗi nói gì và ở dòng nào.

---

## Chạy web để test

Chạy các lệnh dưới đây trong terminal, **tại thư mục gốc `Monster_In_Paris`** (thư mục có file `MainServer.py`).

**Bước 1. Bật môi trường ảo (`.venv`)**

- Windows: `.venv\Scripts\activate`
- macOS / Linux: `source .venv/bin/activate`

Khi thành công, đầu dòng terminal sẽ có chữ `(.venv)`.

**Bước 2. Cài thư viện (chỉ cần làm một lần - về sau anh sẽ làm file requirement cho các bạn)**

```
pip install fastapi uvicorn jinja2
```

**Bước 3. Bật server**

```
uvicorn MainServer:app --reload
```

- `MainServer` là tên file `MainServer.py`.
- `app` là tên biến FastAPI trong file đó.
- `--reload` giúp server tự nạp lại mỗi khi bạn lưu file, không cần tắt bật.

**Bước 4. Mở trình duyệt**

- Trang web: `http://127.0.0.1:8000`
- Trang thử API của FastAPI (FastAPI tự tạo): `http://127.0.0.1:8000/docs`

**Tắt server:** nhấn `Ctrl + C` trong terminal.

> Mẹo: nếu web báo lỗi, **nhìn vào cửa sổ terminal đang chạy `uvicorn`**. Lỗi Python sẽ được in ra ở đó, kèm tên file và số dòng.

---

## Lỗi hay gặp

| Thấy gì | Thường là do | Cách xử lý |
|---|---|---|
| `uvicorn` không được nhận ra | Chưa bật `.venv` hoặc chưa cài thư viện | Làm lại bước 1 và 2 |
| `ModuleNotFoundError: No module named 'fastapi'` | Như trên | Làm lại bước 1 và 2 |
| `Error loading ASGI app` | Sai tên file hoặc tên biến trong lệnh chạy | Báo anh |
| `Address already in use` | Đang có server khác chạy ở cổng 8000 | Tắt server cũ, hoặc chạy thêm `--port 8001` |
| Trang báo `Internal Server Error` (mã 500) | Code Python của bạn bị lỗi | Xem lỗi trong terminal đang chạy `uvicorn` |
| Báo `404 Not Found` | Gõ sai đường dẫn | Kiểm tra lại URL |
| Lưu file rồi mà trang không đổi | Trình duyệt giữ bản cũ | Nhấn `Ctrl + F5` |
| `IndentationError` / `SyntaxError` | Thụt lề sai, thiếu dấu `:` hoặc dấu ngoặc | Xem dòng được báo lỗi |
| PowerShell chặn lệnh `activate` | Windows chặn chạy script | Chạy lệnh `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned`, rồi bật lại `.venv` |

---

## Khi cần hỏi anh

Hãy gửi kèm:

1. Bạn đang làm project nào, file nào.
2. **Toàn bộ nội dung lỗi** trong terminal (copy chữ, đừng chụp mỗi một dòng cuối).
3. Bạn đã thử những gì.

---

## Không đẩy lên Git

Nếu dùng Git, đừng đẩy các thứ sau lên (thêm vào file `.gitignore`):

```
.venv/
__pycache__/
```

---

## Tóm tắt trong 5 dòng

1. Chỉ viết code vào các chỗ `TODO` trong `project/`. (và vài chổ khác =) để cho các bạn hiểu debug là giề :V )
2. Giữ nguyên tên hàm và tên tham số.
3. Hàm dùng `return`, không dùng `input()`/`print()`.
4. Không đụng `MainServer.py`, `routers/`, `.venv/`.
5. Chạy: bật `.venv`, rồi `uvicorn MainServer:app --reload`.