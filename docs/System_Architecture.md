# System Architecture
## Project: IT Service Request & Automation Platform

---

### 1. Kiến trúc phân tầng (Layered Architecture)

```text
┌─────────────────────────────────────────────────────────────────────────┐
│                        1. PRESENTATION LAYER                            │
│  ┌─────────────────────────────────┐   ┌─────────────────────────────┐  │
│  │   Employee Self-Service Portal   │   │     Copilot AI Assistant    │  │
│  │     (Power Apps Canvas App)     │   │      (Copilot Studio)       │  │
│  └────────────────┬────────────────┘   └──────────────┬──────────────┘  │
└───────────────────┼───────────────────────────────────┼─────────────────┘
                    │                                   │
┌───────────────────┼───────────────────────────────────┼─────────────────┐
│                   ▼                                   ▼                 │
│                          2. DATA STORAGE LAYER                          │
│  ┌───────────────────────────────────────────────────────────────────┐  │
│  │                   SharePoint Online Lists                         │  │
│  │   - IT_Requests (Main transactional table)                        │  │
│  │   - Employees (Directory reference table)                         │  │
│  │   - Service_Catalog (Category & SLA parameters)                   │  │
│  └────────────────┬──────────────────────────────────────────────────┘  │
└───────────────────┼─────────────────────────────────────────────────────┘
                    │
┌───────────────────┼─────────────────────────────────────────────────────┐
│                   ▼                                                     │
│                    3. AUTOMATION & BUSINESS LOGIC LAYER                 │
│  ┌───────────────────────────────────────────────────────────────────┐  │
│  │                      Microsoft Power Automate                     │  │
│  │   - Flow 1: New Ticket Intake, Validation & SLA Calculation       │  │
│  │   - Flow 2: Multi-Tier Approval Workflow (Adaptive Cards / Email) │  │
│  │   - Flow 3: Smart Routing & Notification Automation               │  │
│  │   - Flow 4: SLA Monitor & Escalation Engine                       │  │
│  │   - Flow 5: AI PoC Classification Hook (AI Builder / LLM)         │  │
│  └────────────────┬──────────────────────────────────────────────────┘  │
└───────────────────┼─────────────────────────────────────────────────────┘
                    │
┌───────────────────┼─────────────────────────────────────────────────────┐
│                   ▼                                                     │
│                     4. ANALYTICS & REPORTING LAYER                      │
│  ┌───────────────────────────────────────────────────────────────────┐  │
│  │                        Power BI Dashboard                         │  │
│  │   - Real-time KPI Overview (Volume, MTTR, SLA Breach %)           │  │
│  │   - Workload Distribution by Support Engineer & Department        │  │
│  │   - Root Cause & Request Categorization Analysis                  │  │
│  └───────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────┘
```

---

### 2. Các thành phần công nghệ chi tiết

#### 2.1. Microsoft Power Apps (Canvas App)
- **Framework:** Canvas App (Tối ưu cho cả Desktop & Mobile/Tablet).
- **Data Source:** SharePoint Online List (`IT_Requests`).
- **Giao diện:** 4 Màn hình chuẩn UX/UI theo thiết kế hiện đại (Modern Theme).
- **Logic / Formula:** Ngôn ngữ **Power Fx** xử lý validation form, lọc dữ liệu phía client và Submit Form.

#### 2.2. SharePoint Online (Data Storage)
- Lưu trữ dữ liệu dạng bảng với cơ chế phân quyền RBAC (Role-Based Access Control).
- Quản lý phiên bản (Version History) và đính kèm tệp tin tài liệu hỗ trợ.

#### 2.3. Microsoft Power Automate (Workflow Engine)
- Tiếp nhận các sự kiện thay đổi dữ liệu từ SharePoint (Event-driven architecture).
- Thực thi logic rẽ nhánh, gửi Approval Request qua email và Microsoft Teams.
- Đồng bộ hóa trạng thái hai chiều giữa người dùng, kỹ sư và cấp quản lý.

#### 2.4. Microsoft Copilot Studio
- Chatbot AI tích hợp Knowledge Base (FAQ & Hướng dẫn kỹ thuật).
- Kết nối trực tiếp vào Power Automate để mở ticket tự động khi hội thoại thất bại trong việc giải quyết sự cố.

#### 2.5. Microsoft Power BI
- Kết nối dữ liệu trực tiếp với SharePoint List qua kết nối Web/SharePoint connector.
- Chuyển đổi và làm sạch dữ liệu bằng **Power Query (M Code)**.
- Mô hình hóa dữ liệu và tính toán chỉ số nghiệp vụ nâng cao bằng **DAX (Data Analysis Expressions)**.
