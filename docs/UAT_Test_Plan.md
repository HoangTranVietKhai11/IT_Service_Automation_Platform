# UAT Test Plan & Execution Matrix
## Project: IT Service Request & Automation Platform

---

### 1. Mục tiêu kiểm thử (Test Objectives)
Xác minh toàn bộ các chức năng của giải pháp **IT Service Request & Automation Platform** hoạt động đúng với yêu cầu nghiệp vụ (Business Requirements), xử lý ngoại lệ tốt và sẵn sàng cho việc đưa vào sử dụng thực tế (Go-Live).

---

### 2. Phạm vi kiểm thử (Scope of Testing)
- **Power Apps Portal:** Kiểm tra tạo ticket, validation dữ liệu, tìm kiếm, lọc danh sách và xem chi tiết.
- **Power Automate Flows:** Kiểm tra trigger tiếp nhận, tính SLA, luồng Approval, luồng gán kỹ sư và gửi email.
- **Power BI Dashboard:** Kiểm tra độ chính xác của các chỉ số KPI, tương tác qua lại giữa các visual (Cross-filtering) và làm sạch dữ liệu.
- **Copilot Studio:** Kiểm tra độ chính xác của câu trả lời FAQ và khả năng leo thang tạo ticket.

---

### 3. Kịch bản kiểm thử chi tiết (UAT Test Cases)

| Test ID | Hạng mục kiểm thử | Kịch bản / Thao tác thực hiện | Kết quả mong đợi (Expected Result) | Kết quả thực tế (Actual Result) | Trạng thái (Pass/Fail) |
|---|---|---|---|---|---|
| **TC-01** | Power Apps Validation | Bấm nút Submit khi để trống trường `Employee Name` hoặc `Description` | Hệ thống báo lỗi validation màu đỏ, không cho gửi ticket | Đã chặn gửi và báo lỗi cụ thể | **PASS** |
| **TC-02** | Create Normal Ticket | Gửi ticket `Medium` phân loại `Network` | Bản ghi được tạo trong SharePoint với trạng thái `New`, mã sinh tự động | Bản ghi tạo thành công `REQ-0001` | **PASS** |
| **TC-03** | Auto-Assignment | Kiểm tra ticket `Network` sau khi tạo | Power Automate tự động cập nhật `AssignedTo = thinh.bui@company.com`, status thành `In Progress` | Flow chạy gán đúng kỹ sư | **PASS** |
| **TC-04** | High Priority Approval | Gửi ticket có `Priority = High` | Flow chuyển trạng thái sang `Pending Approval` và gửi email Approval tới Manager | Email Approval được gửi kèm 2 nút bấm | **PASS** |
| **TC-05** | Manager Reject | Manager bấm nút `Reject` và nhập lý do | Status đổi thành `Rejected`, nhân viên nhận được email thông báo kèm lý do từ chối | Trạng thái cập nhật đúng, gửi mail tức thì | **PASS** |
| **TC-06** | Manager Approve | Manager bấm nút `Approve` | Status đổi thành `Approved` rồi chuyển sang `In Progress`, tự gán kỹ sư IT | Luồng tiếp tục phân công chính xác | **PASS** |
| **TC-07** | SLA Deadline Calc | Gửi ticket `Critical` vào lúc 08:00 | Hệ thống tính `SLADeadline` chính xác là 12:00 cùng ngày (cộng 4 giờ) | `SLADeadline` chính xác theo công thức | **PASS** |
| **TC-08** | My Requests Filter | Chọn filter `In Progress` trong màn hình danh sách | Gallery chỉ hiển thị các ticket đang có trạng thái `In Progress` | Bộ lọc hoạt động tức thì | **PASS** |
| **TC-09** | Resolve Ticket | IT Engineer nhập `Resolution` và đổi status thành `Resolved` | `ResolvedDate` tự động ghi nhận thời gian hiện tại, gửi email hoàn thành cho nhân viên | Ghi nhận giải pháp và thời gian chính xác | **PASS** |
| **TC-10** | Power BI Cross-filter | Bấm chọn phòng ban `Finance` trên biểu đồ phòng ban | Toàn bộ các thẻ KPI và biểu đồ phân loại tự động lọc theo dữ liệu của phòng Finance | Dashboard tương tác mượt mà | **PASS** |
| **TC-11** | Copilot Chatbot FAQ | Người dùng hỏi "Làm sao để kết nối lại Wi-Fi văn phòng?" | Chatbot trả lời đầy đủ 4 bước khắc phục từ tài liệu hướng dẫn | Phản hồi đúng nội dung trong KB | **PASS** |
| **TC-12** | Copilot Escalation | Người dùng báo "Vẫn không được, hãy tạo ticket giúp tôi" | Chatbot gọi action kích hoạt Power Automate tạo ticket mới và trả về mã ticket | Tạo ticket thành công qua chatbot | **PASS** |

---

### 4. Báo cáo tổng kết UAT (Sign-off Summary)
- **Tổng số Test Cases:** 12
- **Số lượng Đạt (Passed):** 12 / 12 (100%)
- **Số lượng Lỗi nghiêm trọng (Blocker):** 0
- **Kết luận:** Hệ thống đáp ứng toàn diện các tiêu chí nghiệm thu và sẵn sàng cho môi trường hoạt động thực tế.
