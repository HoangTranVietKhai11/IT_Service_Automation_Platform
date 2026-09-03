# IT Support Knowledge Base (Cơ sở tri thức FAQ cho Copilot Studio)
## Organization: IT Service Desk & Central Service

Tài liệu này chứa toàn bộ các kịch bản hướng dẫn xử lý sự cố phổ biến, được sử dụng làm nguồn dữ liệu **Knowledge Base (Generative Answers)** cho **Microsoft Copilot Studio**.

---

## 1. Reset Mật khẩu & Mở khóa tài khoản (Password Reset & Account Unlock)

### Vấn đề: Quên mật khẩu hoặc tài khoản Microsoft 365 bị khóa (Account Locked)
* **Nguyên nhân**: Nhập sai mật khẩu quá 5 lần hoặc mật khẩu hết hạn sau 90 ngày.
* **Hướng dẫn tự xử lý (Self-service)**:
  1. Truy cập cổng tự phục vụ: `https://passwordreset.microsoftonline.com`
  2. Nhập email công ty và mã xác thực captcha.
  3. Chọn phương thức xác thực bảo mật 2 lớp (MFA): Mã gửi qua SMS hoặc ứng dụng **Microsoft Authenticator**.
  4. Tạo mật khẩu mới (Tối thiểu 10 ký tự, bao gồm chữ hoa, chữ thường, số và ký tự đặc biệt).
* **Nếu không thành công**: Hãy tạo ticket loại `Account` với mức ưu tiên `High` để IT Desk mở khóa trực tiếp.

---

## 2. Kết nối Mạng & Wi-Fi văn phòng (Wi-Fi Troubleshooting)

### Vấn đề: Laptop không thể kết nối hoặc bị ngắt kết nối Wi-Fi công ty (`DKSH_Corporate_WiFi`)
* **Hướng dẫn tự xử lý**:
  1. **Bước 1**: Kiểm tra chế độ máy bay (Airplane Mode) đã tắt và Wi-Fi đã bật.
  2. **Bước 2**: Quên mạng Wi-Fi:
     * Vào `Settings` > `Network & Internet` > `Wi-Fi` > `Manage known networks`.
     * Chọn mạng công ty > Bấm **Forget**.
  3. **Bước 3**: Kết nối lại và nhập tài khoản email công ty kèm mật khẩu hiện tại.
  4. **Bước 4**: Khởi động lại máy tính (Restart) để làm mới card mạng.
* **Nếu vẫn không được**: Tạo ticket loại `Network` để kỹ sư mạng kiểm tra địa chỉ MAC.

---

## 3. Cài đặt & Cấu hình VPN làm việc từ xa (VPN Remote Access)

### Vấn đề: Không thể kết nối VPN để truy cập tài liệu nội bộ khi làm việc ở nhà
* **Yêu cầu bắt buộc**: Đã được phê duyệt quyền truy cập VPN từ Line Manager.
* **Hướng dẫn cài đặt & kết nối**:
  1. Mở ứng dụng **FortiClient / GlobalProtect VPN** đã được cài sẵn trên laptop.
  2. Nhập địa chỉ Gateway: `vpn.company.com` (Port 443).
  3. Nhập Email và Mật khẩu tài khoản công ty.
  4. Xác nhận thông báo trên ứng dụng **Microsoft Authenticator** trên điện thoại.
* **Lưu ý**: Nếu chưa có phần mềm VPN, hãy gửi yêu cầu loại `Access Request` > `VPN Access`.

---

## 4. Sự cố Outlook & Microsoft Teams (M365 Troubleshooting)

### Vấn đề: Outlook bị đơ (Not Responding) hoặc không nhận/gửi được email
* **Hướng dẫn tự xử lý**:
  1. Mở hộp thoại Run (`Windows + R`) > gõ `outlook.exe /safe` > bấm **Enter** để mở Outlook ở chế độ Safe Mode.
  2. Kiểm tra dung lượng hòm thư: Nếu dung lượng vượt quá 95% (47.5 GB / 50 GB), hãy xóa bớt thư trong mục `Deleted Items` hoặc lưu trữ thư cũ vào Archive.
  3. Xóa cache Teams:
     * Tắt hoàn toàn Microsoft Teams.
     * Mở `Windows + R` > dán `%appdata%\Microsoft\Teams` > xóa toàn bộ file trong thư mục này > Mở lại Teams.

---

## 5. Yêu cầu Cấp mới / Thu hồi Thiết bị & Phần mềm (Hardware & Software Requests)

### 5.1. Cấp mới Laptop / Màn hình / Phụ kiện (Hardware)
* **Quy định**: Yêu cầu phải có phê duyệt của Trưởng bộ phận (Line Manager) nếu chi phí phát sinh.
* **Thời gian đáp ứng (SLA)**: 24 - 48 giờ làm việc kể từ khi được duyệt.

### 5.2. Cài đặt phần mềm có bản quyền (Adobe Photoshop, Power BI Pro, Visual Studio...)
* Gửi yêu cầu qua cổng **IT Service Portal** > Chọn loại `Software` > Điền rõ lý do phục vụ công việc và người phê duyệt kinh phí.
