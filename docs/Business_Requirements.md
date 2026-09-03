# Business Requirements Document (BRD)
## Project: IT Service Request & Automation Platform

---

### 1. Executive Summary
Doanh nghiệp đang đối mặt với tình trạng quá tải và thiếu minh bạch trong việc tiếp nhận và xử lý các yêu cầu hỗ trợ công nghệ thông tin (IT Helpdesk). Việc tiếp nhận phân tán qua email, tin nhắn Teams/Zalo và trao đổi miệng dẫn đến tình trạng trễ hạn, thất lạc yêu cầu, không có cam kết chất lượng dịch vụ (SLA) và thiếu dữ liệu định lượng cho cấp quản lý để tối ưu nguồn lực.

Dự án **IT Service Request & Automation Platform** xây dựng giải pháp số hóa toàn diện trên nền tảng **Microsoft Power Platform** kết hợp AI nhằm chuẩn hóa quy trình, tự động hóa phân luồng xử lý và cung cấp báo cáo phân tích thời gian thực.

---

### 2. Business Problem & Opportunity

| Vấn đề hiện tại | Hậu quả kinh doanh | Cơ hội cải tiến với Power Platform |
|---|---|---|
| Yêu cầu gửi qua email/chat phân tán | Thất lạc ticket (15-20%), phản hồi chậm | Cổng gửi yêu cầu tập trung qua **Power Apps** |
| Phân loại & phân công thủ công | Tốn 30-45 phút mỗi ticket để chuyển tiếp | Tự động định tuyến theo phân loại qua **Power Automate** |
| Yêu cầu đặc quyền thiếu phê duyệt chuẩn | Rủi ro an ninh thông tin, vi phạm audit | Quy trình phê duyệt số hóa nhiều cấp (Approval flow) |
| Không theo dõi được SLA | Không biết ticket nào sắp quá hạn | Hệ thống tính toán SLA tự động và cảnh báo vi phạm |
| Thiếu báo cáo tổng hợp | IT Manager không nắm được tải công việc | Dashboard trực quan thời gian thực trên **Power BI** |
| Câu hỏi IT cơ bản lặp lại nhiều | IT Helpdesk mất 40% thời gian cho FAQ | Chatbot hỗ trợ tự động 24/7 với **Copilot Studio** |

---

### 3. Project Objectives (Mục tiêu dự án)
1. **100% Yêu cầu được số hóa:** Mọi yêu cầu hỗ trợ IT được tạo, lưu trữ và theo dõi tập trung trên SharePoint/Dataverse.
2. **Giảm 70% thời gian tiếp nhận & phân công:** Power Automate tự động gán ticket đến kỹ sư phụ trách phù hợp trong vòng dưới 1 phút.
3. **Tuân thủ SLA > 90%:** Theo dõi tự động hạn chót xử lý dựa trên mức độ ưu tiên (Critical: 4h, High: 8h, Medium: 24h, Low: 72h).
4. **Tự động hóa phê duyệt quản lý:** Các yêu cầu mức High/Critical hoặc quyền truy cập nhạy cảm được gửi phê duyệt tự động tới Line Manager.
5. **Nâng cao khả năng tự phục vụ (Self-service):** Chatbot AI giải đáp các sự cố IT phổ biến (Reset mật khẩu, VPN, Wi-Fi).

---

### 4. Stakeholders (Các bên liên quan)

| Stakeholder | Vai trò | Trách nhiệm chính |
|---|---|---|
| **Employee (End-user)** | Người dùng nội bộ | Gửi yêu cầu, theo dõi tiến độ, xác nhận hoàn thành |
| **Line Manager** | Người phê duyệt | Phê duyệt/từ chối các yêu cầu có mức độ ưu tiên cao hoặc cấp quyền |
| **IT Support Engineer** | Người xử lý kỹ thuật | Tiếp nhận ticket được gán, cập nhật tiến độ, ghi nhận giải pháp |
| **IT Service Desk Manager** | Quản lý IT | Giám sát KPI, SLA, phân bổ nhân sự qua Power BI |
| **Automation Engineer (Intern)** | Nhà phát triển giải pháp | Thiết kế, xây dựng, kiểm thử và tài liệu hóa hệ thống |

---

### 5. Functional Requirements (Yêu cầu chức năng)

#### FR-01: Cổng người dùng (Employee Portal - Power Apps)
- **FR-01.1:** Cho phép người dùng tạo ticket mới với đầy đủ thông tin: Họ tên, Email, Phòng ban, Loại yêu cầu, Mức độ ưu tiên, Mô tả chi tiết, File đính kèm.
- **FR-01.2:** Form validation bắt buộc các trường quan trọng, ngăn chặn dữ liệu rác.
- **FR-01.3:** Màn hình "My Requests" cho phép lọc danh sách theo trạng thái (New, In Progress, Resolved, Closed) và tìm kiếm theo mã ticket.
- **FR-01.4:** Màn hình chi tiết ticket hiển thị đầy đủ thời gian tạo, deadline SLA, người đang xử lý và giải pháp xử lý.

#### FR-02: Tự động hóa quy trình (Power Automate)
- **FR-02.1:** **Trigger:** Kích hoạt ngay khi có ticket mới tạo trong SharePoint List.
- **FR-02.2:** **Tính toán SLA:** Tự động cộng giờ làm việc vào thời điểm tạo để sinh `SLADeadline`.
- **FR-02.3:** **Phê duyệt tự động:** Gửi thông báo phê duyệt tới Quản lý nếu ticket là `Critical` hoặc `High`. Cập nhật trạng thái `Approved`/`Rejected`.
- **FR-02.4:** **Tự động định tuyến (Auto-Assignment):**
  - `Network` $\rightarrow$ Network Engineer
  - `Hardware` $\rightarrow$ Hardware Support
  - `Software` / `Microsoft 365` $\rightarrow$ Application Support Specialist
  - `Account` / `Access Request` $\rightarrow$ Identity & Security Team
- **FR-02.5:** **Thông báo email đa kênh:** Gửi email xác nhận kèm mã ticket cho người gửi và email thông báo công việc cho kỹ sư IT được gán.
- **FR-02.6:** **Giám sát SLA:** Gửi email cảnh báo khi ticket còn dưới 25% thời gian SLA hoặc khi đã quá hạn vi phạm (SLA Breached).

#### FR-03: Báo cáo phân tích (Power BI Dashboard)
- **FR-03.1:** Hiển thị thẻ KPI tổng quan: Tổng số ticket, Đang xử lý, Đã hoàn thành, Tỷ lệ vi phạm SLA, Thời gian giải quyết trung bình (MTTR).
- **FR-03.2:** Biểu đồ phân bố ticket theo Phòng ban, Phân loại lỗi, Cấp độ ưu tiên.
- **FR-03.3:** Báo cáo hiệu suất theo từng kỹ sư hỗ trợ và xu hướng theo thời gian.

#### FR-04: Trợ lý AI IT (Copilot Studio & AI Classification)
- **FR-04.1:** Chatbot trả lời tự động các bài viết hướng dẫn xử lý sự cố thường gặp (Troubleshooting Guide).
- **FR-04.2:** Cho phép leo thang (Escalate) tạo ticket trực tiếp từ hội thoại chat nếu người dùng chưa tự giải quyết được.
- **FR-04.3 (PoC):** Trích xuất nội dung mô tả của người dùng bằng AI để gợi ý Category và Priority tự động.

---

### 6. Non-Functional Requirements (Yêu cầu phi chức năng)
- **Bảo mật:** Dữ liệu phân quyền theo vai trò (Người dùng chỉ thấy ticket của mình; IT Support thấy toàn bộ ticket).
- **Tính khả dụng:** Hệ thống hoạt động 99.5% trong giờ làm việc của doanh nghiệp.
- **Thời gian phản hồi:** Power Apps tải dữ liệu dưới 3 giây; Flow xử lý dưới 30 giây.
- **Khả năng mở rộng:** Kiến trúc hỗ trợ mở rộng tích hợp Dataverse, Azure OpenAI và Microsoft Teams trong tương lai.
