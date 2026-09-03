# Data Dictionary
## Project: IT Service Request & Automation Platform

Tài liệu định nghĩa cấu trúc dữ liệu của hệ thống, chuẩn hóa schema cho **SharePoint List (`IT_Requests`)**, các bảng phụ trợ và trường dữ liệu tính toán trong **Power BI**.

---

### 1. Bảng chính: `IT_Requests` (SharePoint List / Dataverse Table)

| Tên trường (Column) | Kiểu dữ liệu (Data Type) | Bắt buộc (Required) | Giá trị mặc định / Lựa chọn | Mô tả chi tiết |
|---|---|---|---|---|
| **ID** / **RequestID** | Single line of text / Auto Number | Có | Tự sinh (e.g. `REQ-0001`) | Mã định danh duy nhất của ticket |
| **Title** | Single line of text | Có | Không | Tiêu đề ngắn gọn về sự cố |
| **EmployeeName** | Single line of text | Có | `User().FullName` | Họ và tên nhân viên gửi yêu cầu |
| **Email** | Single line of text | Có | `User().Email` | Địa chỉ email của nhân viên |
| **Department** | Choice (Dropdown) | Có | `Finance`, `HR`, `Supply Chain`, `Commercial`, `Legal & Compliance`, `Marketing`, `IT` | Phòng ban của nhân viên |
| **RequestType** | Choice (Dropdown) | Có | `Hardware`, `Software`, `Network`, `Account`, `Microsoft 365`, `Access Request`, `Other` | Phân loại loại yêu cầu IT |
| **Priority** | Choice (Dropdown) | Có | `Low`, `Medium`, `High`, `Critical` | Mức độ khẩn cấp & tác động |
| **Description** | Multiple lines of text (Plain) | Có | Không | Mô tả chi tiết vấn đề hoặc nhu cầu |
| **Status** | Choice (Dropdown) | Có | Mặc định: `New`<br>Lựa chọn: `New`, `Pending Approval`, `Approved`, `Rejected`, `In Progress`, `Resolved`, `Closed` | Trạng thái vòng đời của ticket |
| **AssignedTo** | Person or Group / Text Email | Không | Không | Kỹ sư IT Desk chịu trách nhiệm xử lý |
| **CreatedDate** | Date and Time | Có | `Created` (Thời điểm tạo) | Ngày và giờ tạo yêu cầu |
| **SLADeadline** | Date and Time | Không | Tính bởi Power Automate | Hạn chót hoàn thành theo cam kết SLA |
| **ResolvedDate** | Date and Time | Không | Không | Thời điểm kỹ sư hoàn thành xử lý |
| **Resolution** | Multiple lines of text | Không | Không | Ghi chú phương án xử lý / nguyên nhân lỗi |
| **Category** | Single line of text | Không | Trùng với `RequestType` hoặc chi tiết hơn | Phân nhóm nghiệp vụ |
| **AIClassification** | Single line of text | Không | Dự đoán bởi AI PoC | Kết quả phân loại tự động của AI |
| **AIConfidence** | Number (Decimal) | Không | Giá trị từ 0.00 đến 1.00 | Độ tin cậy của mô hình AI |
| **ManagerApproval** | Choice | Không | `Pending`, `Approved`, `Rejected`, `N/A` | Kết quả phê duyệt của Line Manager |
| **ManagerComments** | Multiple lines of text | Không | Không | Lý do phê duyệt / từ chối từ Manager |

---

### 2. Quy chuẩn SLA Matrix (Service Level Agreement)

| Priority | Thời gian phản hồi tối đa (First Response) | Thời gian giải quyết tối đa (Resolution SLA) | Người phê duyệt |
|---|---|---|---|
| **Critical** | 15 phút | **4 giờ** | Line Manager + IT Manager |
| **High** | 30 phút | **8 giờ** | Line Manager |
| **Medium** | 2 giờ | **24 giờ** | Tự động phân luồng |
| **Low** | 4 giờ | **72 giờ** | Tự động phân luồng |

---

### 3. Ma trận định tuyến tự động (Assignment Matrix)

| Request Type | Đội ngũ phụ trách (Support Group) | Kỹ sư chỉ định mặc định (Email) |
|---|---|---|
| **Hardware** | Hardware & Workplace Support | `thao.dang@company.com` |
| **Network** | Network & Infrastructure Support | `thinh.bui@company.com` |
| **Software** | Application Support Team | `phuong.ngo@company.com` |
| **Microsoft 365** | Cloud & Collaboration Team | `phuong.ngo@company.com` |
| **Account** | Identity & Access Management (IAM) | `thao.dang@company.com` |
| **Access Request** | Security & Compliance Desk | `dung.truong@company.com` |
| **Other** | IT General Helpdesk | `thao.dang@company.com` |

---

### 4. Bảng nhân viên: `Employees` (Dữ liệu tham chiếu)

| Column Name | Data Type | Description |
|---|---|---|
| `EmployeeID` | Text (Primary Key) | Mã nhân viên (e.g. `EMP001`) |
| `FullName` | Text | Họ và tên đầy đủ |
| `Email` | Text | Email công ty |
| `Department` | Text | Phòng ban trực thuộc |
| `JobTitle` | Text | Chức danh công việc |
| `ManagerEmail` | Text | Email quản lý trực tiếp để gửi Approval |
