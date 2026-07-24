# CyberPanel Optimizer & DPS.MEDIA Custom Branding

Bộ công cụ tối ưu hóa và áp dụng giao diện thương hiệu **DPS.MEDIA** tự động cho **CyberPanel**, sửa triệt để lỗi Server Error (500) khi lưu Custom CSS và dọn dẹp dung lượng hệ thống.

---

## 🚀 Lệnh cài đặt nhanh (1-Liner)

### 🎨 1. Tự động sửa lỗi 500 & Áp dụng Giao diện DPS.MEDIA Custom CSS
Chạy câu lệnh sau bằng quyền `root` trên bất kỳ VPS/Server CyberPanel nào:

```bash
curl -sSL https://raw.githubusercontent.com/hienhoceo-dpsmedia/cyberpanel-optimizer/main/apply_design.sh | bash
```

**Chức năng chính:**
- 🛠️ **Sửa lỗi Server Error (500):** Tự động bọc bộ xử lý ngoại lệ `try...except` và bổ sung timeout/header cho API GitHub trong `baseTemplate/views.py`.
- 🎨 **Áp dụng Custom Branding DPS.MEDIA:** Tự động nạp logo, ẩn các banner quảng cáo/AI scanner rác và cập nhật CSS giao diện vào cơ sở dữ liệu CyberPanel.
- 🔄 **Tự động restart service:** Khởi động lại dịch vụ `lscpd` ngay sau khi cập nhật.

---

### 🧹 2. Dọn dẹp Log & Tối ưu dung lượng CyberPanel
Dọn dẹp bớt log dư thừa của CyberPanel và LiteSpeed:

```bash
curl -sSL https://raw.githubusercontent.com/hienhoceo-dpsmedia/cyberpanel-optimizer/main/install.sh | bash
```

---

## 📁 Cấu trúc Repository

- `apply_design.sh`: Script 1-liner gọi bộ cập nhật giao diện & sửa lỗi 500.
- `apply_design.py`: Script Python tự động patch `views.py` và cập nhật Django Model `CyberPanelCosmetic`.
- `dps_design.css`: Bộ CSS tùy biến giao diện thương hiệu DPS.MEDIA.
- `install.sh`: Script dọn dẹp file log hệ thống.

---

## 🛡️ An toàn & Sao lưu
- Script `apply_design.py` tự động tạo bản sao lưu `/usr/local/CyberCP/baseTemplate/views.py.bak` trước khi thực hiện thay đổi.
- Nếu muốn khôi phục lại trạng thái file views cũ:
  ```bash
  cp /usr/local/CyberCP/baseTemplate/views.py.bak /usr/local/CyberCP/baseTemplate/views.py && systemctl restart lscpd
  ```

---
© DPS.MEDIA JSC. All rights reserved.
