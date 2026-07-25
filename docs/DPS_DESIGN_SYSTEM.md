# 🎨 DPS.MEDIA UI & Admin Panel Design System

Tài liệu chuẩn hóa **System Design / Design System** dành cho giao diện quản trị (Admin Panel, Control Panel, Dashboard) thuộc hệ sinh thái **DPS.MEDIA**. 

Tài liệu này đóng vai trò làm quy chuẩn (spec & guidelines) giúp tái sử dụng màu sắc, typography, responsive scaling và tư duy thiết kế cho các dự án web/panel khác.

---

## 🎯 1. Triết lý Thiết kế (Design Philosophy)

1. **Vận hành thực tế (Operational-First)**:
   - Tập trung 100% vào công năng quản trị và trải nghiệm thao tác của kỹ thuật viên/người dùng.
   - Loại bỏ triệt để các banner quảng cáo, thông báo nhắc nhở tiếp thị (marketing nudges), và các menu không sử dụng đến.
2. **Nhận diện thương hiệu DPS (Branded Consistency)**:
   - Sử dụng cặp màu chủ đạo **DPS Navy** & **DPS Green** đồng bộ trên toàn bộ nền tảng.
   - Thay thế toàn bộ logo, văn bản và đồ họa gốc của nhà sản xuất bằng bộ nhận diện DPS.MEDIA.
3. **Thích ứng màn hình độ phân giải cao (High-DPI Scaling)**:
   - Tự động tỉ lệ (scale) kích thước chữ, nút bấm, khung nhập liệu và sidebar dựa trên độ phân giải màn hình (FHD, 2K, 4K) để tránh tình trạng chữ bị quá nhỏ trên màn hình retina/màn hình lớn.

---

## 🎨 2. Hệ thống Màu sắc (Color Tokens & Palette)

```css
html:root {
    /* Brand Accent Tokens */
    --dps-navy: #151577;         /* Navy chính: Header bảng, Primary Buttons, Active Tabs, Chevrons */
    --dps-navy-hover: #0f0f59;   /* Hover Navy */
    --dps-green: #32b561;        /* Green thương hiệu: Success status, Install Buttons, Active indicators */
    --dps-green-soft: #e8f6ed;   /* Green nhạt: Nền hover nhẹ, nền icon, tab hover */

    /* Neutral & Surface Tokens */
    --bg-primary: #f7f9fb;       /* Nền trang chính */
    --bg-secondary: #ffffff;     /* Nền card/panel */
    --bg-hover: #f0f6f2;         /* Nền khi hover item */
    --border-color: #e1e8e3;     /* Đường viền phân cách */
    --text-primary: #202938;     /* Chữ chính */
    --text-secondary: #6b7783;   /* Chữ phụ / subtitle */
}
```

### Quy tắc áp dụng màu sắc:
| Thành phần | Tông màu áp dụng | Mã màu HEX / Token |
| :--- | :--- | :--- |
| **Table Header (`thead`, `th`)** | DPS Navy | `#151577` (Chữ trắng) |
| **Nút bấm chính (`.btn-primary`, `.btn-info`)** | DPS Navy | Nền `#151577`, Hover `#0f0f59` |
| **Nút thành công / Thao tác (`.btn-success`, `.install-btn`)** | DPS Green | Nền `#32b561`, Hover `#289950` |
| **Tab / Menu Active** | DPS Navy | Nền `#151577`, Chữ trắng |
| **Icon chỉ hướng / Chevrons (`.fa-chevron-*`)** | DPS Navy | `#151577` |
| **Chấm trạng thái Active / Badges** | DPS Green | `#32b561` |

---

## 📐 3. Quy chuẩn Font & Co giãn Màn hình (High-DPI Scaling System)

Hệ thống sử dụng các ngưỡng `@media (min-width)` để tỉ lệ giao diện tự động:

### 📱 1. Standard Displays (< 1600px)
- **Base Font**: `14px`
- **Sidebar Width**: Default (~220px - 240px)
- **Form Control Height**: Default (~38px)

### 🖥️ 2. Desktop Full HD (1600px - 1919px)
- **Base Font**: `15px`
- **Form Control Height**: `42px` (Padding: `8px 14px`)
- **Button Padding**: `8px 18px`

### 🖥️ 3. 2K / Quad HD Displays (1920px - 2199px)
- **Base Font**: `16.5px`
- **Form Control Height**: `46px` (Padding: `10px 16px`)
- **Sidebar Width**: `260px`
- **Button Padding**: `10px 22px`

### 🖥️ 4. Ultra Wide / 2K+ High-DPI (2200px - 2999px) - *Scale ~1.5x*
```css
@media screen and (min-width: 2200px) {
    body, #main-content { font-size: 19.5px !important; }
    .form-control, input, select, label, button, td, th { font-size: 19px !important; }
    .form-control { height: 52px !important; padding: 12px 20px !important; border-radius: 6px !important; }
    .btn { padding: 12px 28px !important; font-size: 18.5px !important; border-radius: 6px !important; }
    #sidebar { width: 300px !important; }
    #sidebar a { font-size: 18px !important; padding: 14px 22px !important; }
    .switch, input[type="checkbox"] { transform: scale(1.25); transform-origin: center right; }
}
```

### 🖥️ 5. 4K Ultra HD Displays (3000px+) - *Scale ~1.75x*
```css
@media screen and (min-width: 3000px) {
    body, #main-content { font-size: 23px !important; }
    .form-control, input, select, label, button, td, th { font-size: 22px !important; }
    .form-control { height: 60px !important; padding: 14px 24px !important; }
    .btn { padding: 14px 32px !important; font-size: 21px !important; }
    #sidebar { width: 360px !important; }
}
```

---

## 🖼️ 4. Tài nguyên Thương hiệu & Kỹ thuật Thay thế (Assets & CSS Hacks)

### 📌 Tài nguyên Ảnh (Asset URLs)
* **Logo Vector SVG**: `https://dps.media/wp-content/uploads/2023/08/dpsmedia.svg`
* **Illustration Background (Login Side)**: `https://dps.media/wp-content/uploads/2025/11/chrome_6AkkKmSNBI.png`

### 🛠️ Kỹ thuật Thay thế Logo & Text bằng Pure CSS
Khi tùy biến giao diện của bên thứ 3 mà không sửa file HTML nguồn:
1. **Ẩn Logo gốc**: Đặt `opacity: 0 !important;` hoặc `display: none !important;` cho thẻ `<img>` cũ.
2. **Chèn Logo DPS**: Gán `background-image: url('https://dps.media/wp-content/uploads/2023/08/dpsmedia.svg')` vào container với `background-size: contain; background-repeat: no-repeat;`.
3. **Thay thế Text**:
   ```css
   /* Ẩn chữ cũ bằng font-size: 0 */
   .brand-title { font-size: 0 !important; position: relative; }
   
   /* Thêm chữ mới qua ::after */
   .brand-title::after {
       content: "DPS.MEDIA";
       font-size: 38px;
       font-weight: 600;
       color: #32b561;
       display: block;
   }
   ```

---

## 🧹 5. Danh sách Loại bỏ (Clean-up Standard)

Mọi giao diện quản trị quy chuẩn DPS cần ẩn các nhóm Selector rác sau:
1. **Banner tiếp thị / QC**: Notification banners, upsell banners, AI scanner prompts.
2. **Dashboard Clutter**: Greetings, hero cards không dùng đến, shortcut thừa.
3. **Sidebar Links ngoài phạm vi**: Các đường dẫn trỏ ra ngoài hệ thống không thuộc quản lý của VPS/Panel.
4. **Website Screenshot Thumbnails**: Ẩn ảnh xem trước website (`.website-screenshot`) trên danh sách tên miền để tránh rối mắt và tải chậm.

---

## 📂 6. Quy chuẩn Tùy biến Trang Chi tiết (Page-Specific Specs)

### 🌐 Danh sách Website (List Websites)
- **Hình đại diện (`.website-screenshot`)**: Đặt `display: none !important;` để ẩn ảnh preview.
- **Lưới thông số (`.info-table`, `.info-cell`)**: 
  - Thu gọn padding ô thông số (`STATE`, `IP ADDRESS`, `PHP VERSION`, `DISK USAGE`, `PACKAGE`, `OWNER`) từ `20px` xuống `10px 16px`.
  - Nhãn nhạt 11px uppercase bold, giá trị đậm `13.5px` màu chữ chính `--text-primary`.
  - Thẻ bao ngoài `padding: 16px 20px` tạo cảm giác gọn gàng (compact & minimal).

### 📁 Quản lý File (File Manager Redesign)
- **Thanh điều hướng trên (`#navBar`)**: Nền trắng sáng, viền dưới nhẹ `--border-color`, icon thương hiệu DPS Green Soft, tên miền dạng badge xanh nhạt.
- **Thao tác nhanh (Nav links)**: Icon chủ đạo DPS Navy `#151577`, hiệu ứng hover nền `--dps-green-soft`.
- **Cây thư mục (`#treeView`) & Toolbar phụ**: Khung card bo góc `10px`, ô chứa đường dẫn hiện tại (`#currentPath`) sử dụng font monospace xanh Navy đậm.
- **Bảng danh sách tập tin (`#filesTable`, `table`)**: Header bảng phủ màu **DPS Navy `#151577`** chữ trắng in hoa, dòng tập tin hover màu xanh dịu `--dps-green-soft`, icon thư mục Navy, icon tập tin Green `#32b561`.

---
*DPS.MEDIA Design System Spec - Version 1.1*

