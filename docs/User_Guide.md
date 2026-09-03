# User Guide
## IT Service Request & Automation Platform

Tài liệu hướng dẫn sử dụng dành cho **Nhân viên (End-User)** và **Kỹ sư IT Desk (IT Support Engineer)**.

---

### 1. Hướng dẫn dành cho Nhân viên (Employee Guide)

#### Bước 1: Truy cập Cổng dịch vụ IT
- Mở ứng dụng **IT Service Portal** từ màn hình Power Apps hoặc đường link được gửi qua email.
- Tại màn hình chính (Home), bạn có 3 lựa chọn:
  1. **Create Request:** Tạo yêu cầu hỗ trợ mới.
  2. **My Requests:** Xem và theo dõi tiến độ các yêu cầu của bạn.
  3. **IT FAQ / Assistant:** Tra cứu hướng dẫn tự khắc phục nhanh.

#### Bước 2: Tạo yêu cầu hỗ trợ mới
1. Bấm vào nút **Create Request**.
2. Thông tin cá nhân (Họ tên, Email) sẽ được tự động điền theo tài khoản đăng nhập của bạn.
3. Chọn **Department** (Phòng ban của bạn).
4. Chọn **Request Type** phù hợp với vấn đề bạn gặp phải (Ví dụ: `Hardware` nếu hỏng chuột/bàn phím; `Network` nếu mất mạng hoặc lỗi VPN).
5. Chọn mức độ ưu tiên **Priority**:
   - `Critical`: Sự cố diện rộng làm gián đoạn hoàn toàn công việc (SLA: 4 giờ).
   - `High`: Sự cố nghiêm trọng ảnh hưởng trực tiếp đến cá nhân (SLA: 8 giờ).
   - `Medium`: Yêu cầu công việc tiêu chuẩn (SLA: 24 giờ).
   - `Low`: Thắc mắc, yêu cầu tư vấn hoặc bảo trì định kỳ (SLA: 72 giờ).
6. Nhập mô tả chi tiết vào ô **Description** và đính kèm hình ảnh chụp màn hình lỗi nếu có.
7. Bấm nút **Submit Request**. Hệ thống sẽ gửi email xác nhận kèm mã số Ticket (Ví dụ: `REQ-0025`).

#### Bước 3: Theo dõi trạng thái yêu cầu
- Mở mục **My Requests** để xem danh sách các ticket đã tạo.
- Sử dụng thanh bộ lọc trạng thái: `All`, `New`, `In Progress`, `Resolved`, `Closed`.
- Bấm vào một ticket để xem thông tin chi tiết: Kỹ sư nào đang xử lý, deadline cam kết và giải pháp khi hoàn tất.

---

### 2. Hướng dẫn dành cho Kỹ sư IT (IT Support Engineer Guide)

#### Bước 1: Nhận thông báo ticket mới
- Khi có ticket thuộc nhóm chuyên môn của bạn được gán tự động, bạn sẽ nhận được thông báo qua Email/Teams.

#### Bước 2: Cập nhật tiến độ & Xử lý
- Mở chi tiết ticket trên Portal hoặc SharePoint List.
- Sau khi kiểm tra và khắc phục xong:
  1. Chuyển trạng thái sang **Resolved**.
  2. Nhập đầy đủ nguyên nhân và phương án khắc phục vào ô **Resolution**.
  3. Bấm **Save**. Hệ thống sẽ tự động ghi nhận thời gian `ResolvedDate` và gửi email thông báo cho người dùng.
