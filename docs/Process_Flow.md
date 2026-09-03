# Process Flow
## Project: IT Service Request & Automation Platform

Tài liệu này mô tả toàn diện luồng nghiệp vụ từ khi nhân viên gặp sự cố, tìm kiếm giải pháp tự phục vụ, gửi yêu cầu, qua các bước phê duyệt và phân luồng tự động, đến khi xử lý hoàn tất và ghi nhận vào hệ thống phân tích.

---

### 1. Luồng tổng thể (End-to-End Business Flow)

```mermaid
sequenceDiagram
    autonumber
    actor Emp as Nhân viên (Employee)
    participant Bot as Copilot Studio
    participant App as Power Apps Portal
    participant SP as SharePoint List
    participant Flow as Power Automate
    actor Mgr as Line Manager
    actor IT as IT Support Engineer
    participant PBI as Power BI Dashboard

    alt Người dùng cần hỗ trợ nhanh (Self-service)
        Emp->>Bot: Đặt câu hỏi sự cố IT thường gặp
        Bot-->>Emp: Hướng dẫn giải quyết tức thì (FAQ)
    end

    alt Không tự xử lý được hoặc có yêu cầu dịch vụ
        Emp->>App: Nhập form yêu cầu (Loại lỗi, Ưu tiên, Mô tả)
        App->>SP: Tạo bản ghi Ticket mới (Status: New)
        SP-->>Flow: Trigger: "When an item is created"
        
        Flow->>Flow: Tính toán SLADeadline dựa theo Priority
        
        opt Mức độ High hoặc Critical
            Flow->>Flow: Cập nhật Status = "Pending Approval"
            Flow->>Mgr: Gửi yêu cầu phê duyệt qua Email/Teams
            alt Phê duyệt từ chối
                Mgr-->>Flow: Reject
                Flow->>SP: Cập nhật Status = "Rejected"
                Flow->>Emp: Gửi email thông báo từ chối
            else Phê duyệt đồng ý
                Mgr-->>Flow: Approve
                Flow->>SP: Cập nhật Status = "Approved"
            end
        end

        Flow->>Flow: Xác định Kỹ sư phụ trách theo Ma trận RequestType
        Flow->>SP: Gán AssignedTo, Cập nhật Status = "In Progress"
        Flow->>Emp: Gửi email xác nhận tiếp nhận kèm mã Ticket & Deadline
        Flow->>IT: Gửi email thông báo phân công công việc
        
        par Giám sát SLA ngầm (SLA Monitoring)
            Flow->>Flow: Chờ theo thời hạn SLA
            opt Quá hạn chưa Resolved
                Flow->>Mgr: Gửi email cảnh báo SLA Breached
            end
        and Xử lý kỹ thuật
            IT->>App: Kiểm tra chi tiết và tiến hành khắc phục
            IT->>SP: Nhập Resolution và đổi Status = "Resolved"
            Flow->>Emp: Gửi email thông báo hoàn thành
            Emp->>App: Xác nhận và chuyển Status = "Closed"
        end

        SP->>PBI: Tự động cập nhật dữ liệu vào Dashboard báo cáo
    end
```

---

### 2. Chi tiết các luồng xử lý con (Sub-processes)

#### 2.1. Luồng tính toán SLA (SLA Calculation Rule)
- **Công thức:** `SLADeadline = CreatedDate + SLA_Hours(Priority)`
- **Quy tắc:**
  - `Critical` $\rightarrow$ `addHours(triggerBody()?['Created'], 4)`
  - `High` $\rightarrow$ `addHours(triggerBody()?['Created'], 8)`
  - `Medium` $\rightarrow$ `addHours(triggerBody()?['Created'], 24)`
  - `Low` $\rightarrow$ `addHours(triggerBody()?['Created'], 72)`

#### 2.2. Luồng Phê duyệt (Approval Decision Matrix)
- Nếu `Priority in ('High', 'Critical')` hoặc `RequestType = 'Access Request'`:
  - Trạng thái chuyển sang `Pending Approval`.
  - Gửi thẻ Approval đến `ManagerEmail` với 2 nút **Approve** và **Reject**.
  - Nếu **Reject**: Ghi nhận nhận xét của Quản lý vào `ManagerComments`, gửi thông báo kết thúc cho nhân viên.
  - Nếu **Approve**: Tiếp tục quy trình phân công cho IT Support.

#### 2.3. Luồng Tự động định tuyến (Routing Logic)
Sử dụng khối điều kiện **Switch** trong Power Automate dựa trên giá trị `RequestType`:
- **Case "Hardware"**: Gán cho bộ phận Phần cứng & Thiết bị.
- **Case "Network"**: Gán cho bộ phận Mạng & Hạ tầng.
- **Case "Software" | "Microsoft 365"**: Gán cho bộ phận Ứng dụng & Nền tảng Cloud.
- **Case "Account" | "Access Request"**: Gán cho bộ phận Quản trị Định danh & Phân quyền.
- **Default ("Other")**: Gán cho Trưởng nhóm IT Service Desk để phân loại thủ công.
