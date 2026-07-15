# CyberPanel & OpenLiteSpeed Optimizer

Script tự động tối ưu hóa phân vùng ghi tạm (swapping directory) cho OpenLiteSpeed (OLS) và cài đặt tác vụ dọn dẹp log, cache định kỳ tự động cho VPS chạy CyberPanel.

## Các tính năng chính

1. **Tách Swapping Directory ra khỏi `/tmp`:**
   * Di chuyển Swap Directory của OLS từ mặc định `/tmp/lshttpd/swap` sang thư mục riêng `/lswstmp/lshttpd/swap` trên phân vùng đĩa cứng.
   * Ngăn chặn việc làm đầy thư mục tạm `/tmp` (thường chạy trên RAM `tmpfs` hoặc phân vùng root có dung lượng nhỏ), giúp tránh lỗi crash cơ sở dữ liệu **MySQL/MariaDB** khi `/tmp` bị đầy.
   * Tự động nhận diện group sở hữu (`nobody` cho CentOS/AlmaLinux hoặc `nogroup` cho Ubuntu/Debian).

2. **Log & Cache Cleaner định kỳ (`/root/logscleaner.sh`):**
   * **Truncate log OLS:** Làm rỗng tất cả các tệp tin `*.log` trong `/usr/local/lsws/logs/` để giải phóng dung lượng nhưng không làm hỏng file descriptor của OpenLiteSpeed.
   * **Clean OLS cache:** Xóa toàn bộ tệp tin cache đã lưu (LSCache) để khôi phục dung lượng ổ đĩa và inodes.
   * **Truncate CyberPanel debug log:** Làm rỗng `/home/cyberpanel/error-logs.txt`.
   * **Dọn dẹp Journalctl:** Giới hạn dung lượng log hệ thống (`systemd-journal`) ở mức tối đa 500MB.
   * **Tự động quét rác:** Quét liệt kê các tệp tin `.sql`, `.gz` thừa thãi và thư mục rác `.trash`, website `staging` của người dùng để admin dễ quản trị dung lượng.

3. **Thiết lập Cron Job tự động:**
   * Tự động đăng ký một Daily Cron Job tại `/etc/cron.d/cyberpanel_logcleaner` để tự động chạy dọn dẹp vào **3:00 sáng mỗi ngày**.

---

## Hướng dẫn cài đặt bằng 1 lệnh duy nhất (1-Click Install)

Chạy lệnh dưới đây với quyền `root` trên VPS CyberPanel của bạn:

```bash
curl -sSL https://raw.githubusercontent.com/hienhoceo-dpsmedia/cyberpanel-optimizer/main/install.sh | bash
```

---

## Kiểm tra sau khi cài đặt

1. **Kiểm tra file cấu hình OLS đã được cập nhật chưa:**
   ```bash
   grep swappingDir /usr/local/lsws/conf/httpd_config.conf
   # hoặc nếu phiên bản cũ:
   grep swappingDir /usr/local/lsws/conf/httpd_config.xml
   ```
   *Kết quả mong muốn:* `<swappingDir>/lswstmp/lshttpd/swap</swappingDir>` hoặc `swappingDir /lswstmp/lshttpd/swap`.

2. **Chạy thử dọn dẹp thủ công:**
   ```bash
   /bin/bash /root/logscleaner.sh
   ```

3. **Kiểm tra Cron Job tự động:**
   ```bash
   cat /etc/cron.d/cyberpanel_logcleaner
   ```
