# N4 — Episodes Module (Frontend-only)

Phiên bản này đã được tinh gọn để chỉ bao gồm phần frontend (HTML/CSS/JS) cho nhiệm vụ N4 (tập phim).
Backend (Flask, model, seed data) đã được tách ra khỏi thư mục này để nhóm khác đảm nhiệm tích hợp sau.

## Mục đích
- Cung cấp giao diện tĩnh cho chức năng **danh sách tập** và **trang xem tập** (N4).
- Dễ mở nhanh để demo UI mà không cần chạy backend.

## Nội dung giữ lại (frontend)
- `frontend_n4/index.html` — trang chủ demo (liệt kê phim)
- `frontend_n4/movie_detail.html` — trang chi tiết phim + danh sách tập
- `frontend_n4/watch.html` — trang xem tập (player + sidebar danh sách tập)
- `frontend_n4/static/css/style.css` — CSS giao diện
- `frontend_n4/static/js/script.js` — JS nhỏ phục vụ UI

> Các file frontend ở trên có thể mở trực tiếp hoặc phục vụ bằng web server tĩnh.

## Chạy trang frontend (cách dễ nhất)
1. Mở PowerShell, chuyển đến thư mục `frontend_n4`:

```powershell
cd 'C:\Users\ADMIN\Documents\code_PY\n4_episodes_module\frontend_n4'
```

2a) Chạy bằng Python HTTP server (khuyến nghị):

```powershell
python -m http.server 8000
```
Mở trình duyệt vào: http://localhost:8000

2b) Nếu dùng VS Code: mở folder `frontend_n4` và sử dụng extension **Live Server** → Go Live.

2c) Hoặc mở trực tiếp file `index.html` bằng trình duyệt (kéo thả). Lưu ý: 1 số trình duyệt chặn một số API khi mở bằng file://.

## Lý do tách backend
- Nhiệm vụ bạn được giao chỉ là frontend (N4). Để tránh xung đột và giúp nhóm khác tích hợp dễ dàng, tôi đã tạm tách/xóa các file backend khỏi thư mục `ui_webphim_ttnt`.
- Nếu cần phục hồi backend để chạy full demo, có thể khôi phục từ Git hoặc tôi có thể giúp tái tạo `app.py`/`models.py` theo yêu cầu.

## File còn tồn tại/ghi chú
- File database `ui_webphim_ttnt/movie_app.db` hiện vẫn nằm trong thư mục gốc. Nếu bạn muốn tôi xóa/move file này, tôi có thể thực hiện (cần đảm bảo không bị khóa bởi process khác).

## Hướng dẫn tích hợp trở lại (tóm tắt)
- Khi nhóm backend (N2/N5) hoàn thiện API, chỉ cần:
  - Thay các đường link tĩnh (`movie_detail.html`, `watch.html`) bằng template Jinja tương ứng hoặc gọi dữ liệu qua fetch/AJAX.
  - Map endpoint backend → các nút/links hiện có (ví dụ: `/watch/<movie_id>/<ep>`).

## Liên hệ / Ghi chú
- Đây là bản giao N4 (chỉ frontend). Nếu muốn tôi tinh chỉnh CSS để giống chính xác giao diện tham chiếu `https://soniabragaonline.com/`, cho biết mức độ chi tiết (color/font/layout).

---
Generated/updated by the frontend maintainer for task N4.
