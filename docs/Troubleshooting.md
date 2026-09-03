# Troubleshooting & Knowledge Base
## IT Service Request & Automation Platform

Tài liệu hướng dẫn xử lý các sự cố IT phổ biến (Dùng làm cơ sở tri thức cho **Copilot Studio Chatbot** và hỗ trợ người dùng tự khắc phục sự cố).

---

### 1. Sự cố Mạng & VPN (Network & VPN Issues)

#### 1.1. Không thể kết nối VPN công ty từ xa
- **Triệu chứng:** Ứng dụng VPN báo lỗi "Connection timed out" hoặc "Authentication failed".
- **Cách khắc phục:**
  1. Kiểm tra kết nối Internet cá nhân (mở thử trang web khác như `google.com`).
  2. Ngắt kết nối Wi-Fi hiện tại và kết nối lại.
  3. Mở ứng dụng xác thực MFA trên điện thoại xem có yêu cầu phê duyệt bảo mật đang chờ hay không.
  4. Khởi động lại ứng dụng VPN client.
  5. Nếu vẫn không được, gửi ticket với loại `Network` - độ ưu tiên `Medium`.

#### 1.2. Mất kết nối Wi-Fi văn phòng
- **Cách khắc phục:**
  1. Tắt chế độ Wi-Fi trên laptop, đợi 10 giây rồi bật lại.
  2. Chọn `Forget Network` với mạng Wi-Fi công ty, sau đó đăng nhập lại bằng tài khoản email doanh nghiệp.
  3. Khởi động lại máy tính.

---

### 2. Sự cố Tài khoản & Mật khẩu (Account & Password)

#### 2.1. Quên mật khẩu hoặc tài khoản bị khóa do nhập sai nhiều lần
- **Cách khắc phục:**
  1. Đợi 15 phút để cơ chế tự động mở khóa tài khoản của Active Directory kích hoạt.
  2. Truy cập cổng tự phục vụ: `https://passwordreset.microsoftonline.com/` để đặt lại mật khẩu qua số điện thoại/MFA đã đăng ký.
  3. Nếu không có số điện thoại dự phòng, nhờ đồng nghiệp gửi ticket loại `Account` với độ ưu tiên `High` để IT Desk mở khóa trực tiếp.

#### 2.2. Đổi điện thoại và mất ứng dụng xác thực 2 bước (MFA)
- **Cách khắc phục:**
  1. Gửi ticket loại `Account` yêu cầu "Reset MFA Registration".
  2. IT Support sẽ xác minh danh tính qua cuộc gọi video hoặc liên hệ trực tiếp Quản lý của bạn để cấp lại mã kích hoạt MFA.

---

### 3. Sự cố Phần mềm & Microsoft 365 (Software & Office Apps)

#### 3.1. Outlook không gửi/nhận được email
- **Cách khắc phục:**
  1. Kiểm tra trạng thái góc dưới bên phải của Outlook: Nếu hiện `Disconnected` hoặc `Need Password`, bấm vào để đăng nhập lại.
  2. Thử truy cập Webmail qua trình duyệt tại `https://outlook.office.com/` để kiểm tra hòm thư có hoạt động bình thường không.
  3. Tắt hoàn toàn Outlook (qua Task Manager nếu bị treo) và mở lại ở chế độ Safe Mode (`outlook.exe /safe`).

#### 3.2. OneDrive không đồng bộ file
- **Cách khắc phục:**
  1. Bấm vào biểu tượng đám mây màu xanh ở góc phải thanh Taskbar.
  2. Kiểm tra xem dung lượng lưu trữ có bị đầy hay không.
  3. Bấm vào bánh răng Cài đặt $\rightarrow$ `Pause syncing` (Tạm dừng 2 giờ) rồi `Resume syncing` (Tiếp tục đồng bộ).
