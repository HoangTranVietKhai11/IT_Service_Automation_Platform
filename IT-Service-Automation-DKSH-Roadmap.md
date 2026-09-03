# IT Service Request & Automation Platform
## Project Roadmap for DKSH AI & Automation Intern

> **Mục tiêu:** Xây dựng một project thực hành Microsoft Power Platform để làm quen với các kỹ năng xuất hiện trong JD **AI & Automation Intern – Central Service – TP.HCM** của DKSH, đồng thời tạo một project có thể đưa vào CV/portfolio sau khi hoàn thành thực tế.

---

## 1. Project Overview

### Tên project

**IT Service Request & Automation Platform**

### Bối cảnh

Mô phỏng một hệ thống IT nội bộ của doanh nghiệp.

Nhân viên có thể:

1. Gửi yêu cầu hỗ trợ IT.
2. Theo dõi trạng thái yêu cầu.
3. Yêu cầu có mức độ ưu tiên khác nhau.
4. Các yêu cầu cần phê duyệt sẽ đi qua workflow tự động.
5. Power Automate tự động phân loại/định tuyến, thông báo và theo dõi SLA.
6. Power BI cung cấp dashboard cho IT Manager.
7. Copilot Studio cung cấp chatbot hỗ trợ các câu hỏi IT thường gặp.
8. AI PoC hỗ trợ phân loại ticket.
9. UAT và documentation được xây dựng như một project doanh nghiệp thực tế.

---

# 2. Mục tiêu học tập

Sau khi hoàn thành project, cần có khả năng giải thích và thực hành được:

- Microsoft Power Apps
- Microsoft Power Automate
- Microsoft Power BI
- Microsoft Copilot Studio
- SharePoint Lists
- Power Query
- Excel
- SQL ở mức cơ bản
- Data collection
- Data retrieval
- Data cleansing
- Basic data analysis
- Workflow automation
- Approval workflow
- Notification automation
- SLA monitoring
- Solution testing
- UAT
- Technical documentation
- Process flow
- User guide
- Proof of Concept (PoC)
- AI-assisted automation
- Process improvement

---

# 3. Mapping với JD

| JD Requirement | Project Implementation |
|---|---|
| Power Apps | Employee IT Request Portal |
| Power Automate | Approval, assignment, notification, SLA workflow |
| Power BI | IT Service Dashboard |
| Copilot Studio | IT Support Assistant |
| Data collection | Collect IT requests |
| Data retrieval | Retrieve request/user information |
| Data cleansing | Normalize request and employee data |
| Basic analysis | Power BI / Excel analysis |
| Solution testing | Functional test cases |
| UAT | UAT test plan and execution |
| Documentation | Project documentation |
| Process flows | Business/system process flows |
| Training materials | User Guide / IT Guide |
| Stakeholder requirements | Business Requirements Document |
| AI / Copilot PoC | AI-assisted ticket classification |
| Process improvement | SLA automation and workflow optimization |

---

# 4. Kiến trúc hệ thống

```text
                         ┌─────────────────────┐
                         │      Employee       │
                         │     Power Apps      │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    Data Storage     │
                         │   SharePoint List   │
                         └──────────┬──────────┘
                                    │
                                    ▼
                    ┌─────────────────────────────┐
                    │       Power Automate        │
                    │                             │
                    │ - Approval                  │
                    │ - Assignment                │
                    │ - Notification              │
                    │ - SLA Monitoring            │
                    │ - Status Update             │
                    └──────────────┬──────────────┘
                                   │
                     ┌─────────────┴─────────────┐
                     │                           │
                     ▼                           ▼
          ┌─────────────────────┐     ┌─────────────────────┐
          │      Power BI       │     │  Copilot Studio     │
          │                     │     │                     │
          │ KPI Dashboard       │     │ IT FAQ              │
          │ Request Analytics   │     │ Troubleshooting     │
          │ SLA Dashboard       │     │ Ticket Escalation   │
          └─────────────────────┘     └─────────────────────┘
```

---

# 5. Technology Stack

## Core

- Microsoft Power Apps
- Microsoft Power Automate
- Microsoft Power BI
- Microsoft Copilot Studio
- SharePoint Online

## Supporting

- Microsoft Excel
- Power Query
- SQL / PostgreSQL (optional extension)
- GitHub
- Markdown

## AI

- Copilot Studio
- AI-assisted ticket classification PoC
- AI tools for research/documentation, nếu có sử dụng thực tế

---

# 6. Phase 0 — Chuẩn bị Environment

## Checklist

- [ ] Có Microsoft account phù hợp để sử dụng Power Platform
- [ ] Đăng nhập Power Apps
- [ ] Đăng nhập Power Automate
- [ ] Đăng nhập Power BI
- [ ] Kiểm tra Copilot Studio
- [ ] Tạo environment/project workspace nếu cần
- [ ] Tạo SharePoint site
- [ ] Tạo GitHub repository

## Repository

Tên đề xuất:

```text
IT-Service-Automation
```

Cấu trúc:

```text
IT-Service-Automation/
│
├── README.md
│
├── docs/
│   ├── Business_Requirements.md
│   ├── Process_Flow.md
│   ├── System_Architecture.md
│   ├── Data_Dictionary.md
│   ├── UAT_Test_Plan.md
│   ├── User_Guide.md
│   └── Troubleshooting.md
│
├── data/
│   ├── sample_employees.xlsx
│   └── sample_it_requests.xlsx
│
└── screenshots/
    ├── powerapps/
    ├── powerautomate/
    ├── powerbi/
    └── copilot/
```

---

# 7. Phase 1 — Thiết kế Business Requirement

## Business Problem

Doanh nghiệp đang xử lý yêu cầu IT thủ công qua email/chat.

Các vấn đề:

- Khó theo dõi ticket.
- Không có trạng thái tập trung.
- Khó biết ticket thuộc team nào.
- Dễ quên xử lý ticket.
- Không có SLA rõ ràng.
- Khó thống kê workload.
- Không có dashboard.
- Các câu hỏi IT đơn giản phải xử lý thủ công.

## Proposed Solution

Xây dựng hệ thống:

```text
Employee
   ↓
Submit IT Request
   ↓
Automated Workflow
   ↓
Approval / Routing
   ↓
IT Support
   ↓
Resolution
   ↓
Dashboard / Analytics
```

---

# 8. Phase 2 — Data Model

## SharePoint List: IT_Requests

Tạo list:

```text
IT_Requests
```

Các column:

| Column | Type | Description |
|---|---|---|
| RequestID | ID | Ticket ID |
| EmployeeName | Text | Người gửi |
| Email | Text | Email |
| Department | Choice | Phòng ban |
| RequestType | Choice | Loại yêu cầu |
| Priority | Choice | Mức ưu tiên |
| Description | Multiple lines | Nội dung |
| Status | Choice | Trạng thái |
| AssignedTo | Person | Người xử lý |
| CreatedDate | Date | Ngày tạo |
| SLADeadline | Date | Deadline |
| ResolvedDate | Date | Ngày hoàn thành |
| Resolution | Multiple lines | Cách xử lý |
| Category | Choice/Text | Phân loại |
| AIClassification | Text | Kết quả AI |
| AIConfidence | Number | Confidence nếu có |
| CreatedBy | Person | Người tạo |

## Request Type

```text
Hardware
Software
Network
Account
Microsoft 365
Access Request
Other
```

## Priority

```text
Low
Medium
High
Critical
```

## Status

```text
New
Pending Approval
Approved
Rejected
In Progress
Resolved
Closed
```

---

# 9. Phase 3 — Power Apps

## Mục tiêu

Xây dựng Canvas App cho nhân viên.

## Screen 1 — Home

Hiển thị:

```text
IT Service Portal

[Create Request]

[My Requests]

[IT FAQ]
```

---

## Screen 2 — Create Request

Form:

```text
Employee Name
Department
Email
Request Type
Priority
Description
Attachment

[Submit]
```

## Validation

Phải kiểm tra:

- [ ] Employee Name không rỗng
- [ ] Email hợp lệ
- [ ] Department đã chọn
- [ ] Request Type đã chọn
- [ ] Priority đã chọn
- [ ] Description không rỗng

---

## Screen 3 — My Requests

Hiển thị:

```text
Request ID
Request Type
Priority
Status
Created Date
Assigned To
```

Cho phép filter:

```text
All
New
In Progress
Resolved
Closed
```

---

## Screen 4 — Request Detail

Hiển thị:

```text
Request ID
Description
Priority
Status
Assigned To
Created Date
SLA Deadline
Resolution
```

---

# 10. Phase 4 — Power Automate

> 📖 **Tài liệu kỹ thuật và biểu thức chi tiết:** Xem tại [docs/Power_Automate_Flows.md](file:///d:/khai/AI_automation/docs/Power_Automate_Flows.md)

## Flow 1 — New Request (Triage, SLA & Approval)

Trigger:

```text
When an item is created (SharePoint List: IT_Requests)
```

Flow:

```text
New Request
     ↓
Validate data
     ↓
Set Status = New
     ↓
Check Priority & Calculate SLA Deadline
     ↓
Check Approval Condition (Critical/High/Access Request)
     ↓
Auto Route to IT Specialist
     ↓
Send notification (Employee & IT Team)
```

---

# 11. Approval Workflow

## Business Rule

Ví dụ:

```text
Critical / High
      ↓
Manager Approval
      ↓
Approved?
   /       \
 YES       NO
 ↓          ↓
IT Team    Reject
```

Normal request:

```text
Normal
   ↓
Auto route
   ↓
IT Support
```

## Checklist

- [ ] Approval request
- [ ] Approve path
- [ ] Reject path
- [ ] Employee notification
- [ ] IT notification
- [ ] Status update
- [ ] Error handling

---

# 12. Assignment Automation

Dựa trên Request Type:

```text
Network
   ↓
Network Support

Microsoft 365
   ↓
Microsoft 365 Support

Hardware
   ↓
Hardware Support

Account
   ↓
System / Identity Support

Software
   ↓
Application Support
```

Mục tiêu:

> Giảm thao tác routing ticket thủ công.

---

# 13. SLA Automation

## SLA giả lập

| Priority | SLA |
|---|---:|
| Critical | 4 hours |
| High | 8 hours |
| Medium | 24 hours |
| Low | 72 hours |

## Flow

```text
Request Created
      ↓
Calculate SLA Deadline
      ↓
Monitor Request
      ↓
Is Request Resolved?
     /       \
   YES        NO
    ↓          ↓
  Stop      SLA Exceeded?
                /      \
              YES       NO
               ↓         ↓
        Notify Manager  Continue
```

## SLA Notifications

Ví dụ:

```text
SLA remaining < 25%
       ↓
Notify assigned IT member

SLA exceeded
       ↓
Notify IT Manager
```

---

# 14. Phase 5 — Data Cleansing

## Dataset lỗi mẫu

Tạo dữ liệu cố tình có vấn đề:

```text
IT
it
IT Department
Information Technology
```

Chuẩn hóa thành:

```text
IT
```

Employee:

```text
Nguyen Van A
NGUYEN VAN A
Nguyễn Văn A
```

Mục tiêu:

```text
Nguyễn Văn A
```

## Data Cleaning Tasks

- [ ] Remove duplicate records
- [ ] Standardize department names
- [ ] Standardize request categories
- [ ] Normalize priority values
- [ ] Handle missing values
- [ ] Standardize email format
- [ ] Validate dates
- [ ] Validate status values

Có thể thực hành bằng:

- Excel
- Power Query
- Power BI

---

# 15. Phase 6 — Power BI

> 📊 **Đặc tả kỹ thuật & Bộ công thức DAX:** Xem tại [docs/Power_BI_Dashboard_Spec.md](file:///d:/khai/AI_automation/docs/Power_BI_Dashboard_Spec.md)  
> 🔢 **File mã nguồn DAX độc lập:** [data/powerbi_dax_measures.dax](file:///d:/khai/AI_automation/data/powerbi_dax_measures.dax)

## Dashboard

Tên:

```text
IT Service Management Dashboard
```

## KPI

```text
Total Requests
Open Requests
Resolved Requests
SLA Breaches
Average Resolution Time
```

## Charts

### Requests by Department

```text
Department
    ↓
Request Count
```

### Requests by Category

```text
Network
Software
Hardware
Account
Microsoft 365
Other
```

### Requests by Priority

```text
Critical
High
Medium
Low
```

### Requests by Status

```text
New
Pending Approval
Approved
In Progress
Resolved
Closed
```

### SLA

Theo dõi:

```text
SLA Met
SLA Breached
Average Resolution Time
```

---

# 16. Phase 7 — Copilot Studio

> 🤖 **Hướng dẫn cấu hình kịch bản Copilot Studio:** [docs/Copilot_Studio_Guide.md](file:///d:/khai/AI_automation/docs/Copilot_Studio_Guide.md)  
> 📚 **Tài liệu Cơ sở tri thức FAQ (Knowledge Base):** [docs/IT_Support_Knowledge_Base.md](file:///d:/khai/AI_automation/docs/IT_Support_Knowledge_Base.md)

## Tên chatbot

```text
IT Support Assistant
```

## Knowledge Base

Tạo tài liệu FAQ:

```text
How to reset password
How to request VPN access
How to request Microsoft 365 access
Wi-Fi troubleshooting
Email troubleshooting
Account lockout
Software installation request
IT ticket submission process
```

## Ví dụ

User:

```text
My laptop cannot connect to Wi-Fi.
```

Bot:

```text
Please try:

1. Check whether Wi-Fi is enabled.
2. Disconnect and reconnect to the network.
3. Restart the Wi-Fi adapter.
4. Restart the laptop.

If the issue persists, I can help you create an IT request.
```

---

# 17. Copilot → Automation

Nâng cấp chatbot:

```text
User
 ↓
Copilot Studio
 ↓
Problem cannot be solved
 ↓
Create IT Request
 ↓
Power Automate
 ↓
IT Support
```

Mục tiêu:

> Biến chatbot từ FAQ bot thành entry point cho automation workflow.

---

# 18. Phase 8 — AI Ticket Classification PoC

> 🧠 **Mã nguồn AI Model PoC:** [data/ai_ticket_classifier.py](file:///d:/khai/AI_automation/data/ai_ticket_classifier.py)

## Objective

Tự động phân loại ticket bằng mô hình Machine Learning & NLP.

Input:

```text
"I cannot connect to the company VPN from my laptop."
```

Expected:

```text
Category: Network
Subcategory: VPN
Priority: Medium
Suggested Team: Network Support
```

Ví dụ:

```text
"I need access to Microsoft 365."

Category: Account / Microsoft 365
Priority: Medium
Suggested Team: Microsoft 365 Support
```

## Automation

```text
New Ticket
    ↓
AI Classification
    ↓
Category
Priority
Team
    ↓
Power Automate
    ↓
Route Ticket
```

## Important

Không được ghi vào CV rằng đã xây dựng AI classification nếu project thực tế chưa triển khai được.

Nếu mới ở mức thử nghiệm:

```text
Proof of Concept
```

thì phải mô tả đúng là PoC.

---

# 19. Phase 9 — Testing

## Test Categories

### Functional Testing

Kiểm tra:

- [ ] Create request
- [ ] Edit request
- [ ] View request
- [ ] Filter request
- [ ] Approval
- [ ] Rejection
- [ ] Assignment
- [ ] Notification
- [ ] SLA
- [ ] Resolution
- [ ] Closing

### Negative Testing

Kiểm tra:

- [ ] Empty form
- [ ] Invalid email
- [ ] Missing priority
- [ ] Missing request type
- [ ] Invalid data
- [ ] Duplicate request
- [ ] Workflow failure

---

# 20. UAT Test Plan

Tạo file:

```text
docs/UAT_Test_Plan.md
```

Bảng:

| ID | Scenario | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| TC001 | Submit request | Request created |  |  |
| TC002 | High priority | Approval triggered |  |  |
| TC003 | Reject request | User notified |  |  |
| TC004 | Approve request | Assigned to IT |  |  |
| TC005 | SLA exceeded | Manager notified |  |  |
| TC006 | Resolve request | Status Resolved |  |  |
| TC007 | Close request | Status Closed |  |  |
| TC008 | Chatbot FAQ | Correct response |  |  |
| TC009 | Escalate chatbot | Ticket created |  |  |

---

# 21. Phase 10 — Documentation

## Business Requirements Document

Phải mô tả:

- Business problem
- Current process
- Proposed process
- Business requirements
- Functional requirements
- Non-functional requirements
- Assumptions
- Limitations

---

## Process Flow

Ví dụ:

```text
Employee
   ↓
Create Request
   ↓
Validation
   ↓
Priority Check
   ↓
Approval?
  / \
YES  NO
 |    |
 v    v
IT   Reject
 |
 v
Assignment
 |
 v
Processing
 |
 v
SLA Check
 |
 v
Resolution
 |
 v
Employee Confirmation
 |
 v
Closed
```

---

# 22. User Guide

Tạo:

```text
docs/User_Guide.md
```

Nội dung:

1. Login
2. Create request
3. Check request
4. Update request
5. Chat with IT Assistant
6. Escalate issue
7. Check resolution
8. Close request

---

# 23. Training Material

Tạo slide hoặc document ngắn:

```text
IT Service Portal Training
```

Bao gồm:

- What is the system?
- Who can use it?
- How to create a ticket
- Priority definitions
- SLA explanation
- How to use IT Assistant
- How to track requests

---

# 24. Error Handling

Power Automate phải có xử lý lỗi cơ bản.

Các trường hợp:

```text
SharePoint unavailable
       ↓
Workflow failure
       ↓
Log error
       ↓
Notify administrator
```

Kiểm tra:

- [ ] Flow failure notification
- [ ] Retry behavior
- [ ] Error logging
- [ ] Invalid data handling

---

# 25. Process Improvement

Sau khi hệ thống chạy ổn định, đánh giá:

### Before

```text
Employee
   ↓
Email / Chat
   ↓
IT manually reads
   ↓
Manual assignment
   ↓
Manual notification
   ↓
Manual tracking
```

### After

```text
Employee
   ↓
Power Apps
   ↓
Power Automate
   ↓
Automatic routing
   ↓
Automatic notification
   ↓
SLA monitoring
   ↓
Power BI
```

## Improvement Metrics

Có thể đo:

```text
Manual steps reduced
Average handling time
Average resolution time
SLA compliance
Number of automated notifications
Number of tickets automatically routed
```

Không được tự tạo số liệu thành tích nếu chưa đo thực tế.

---

# 26. Definition of Done

Project chỉ được xem là hoàn thành khi:

## Power Apps

- [ ] Employee can create request
- [ ] Employee can view request
- [ ] Employee can filter request
- [ ] Form validation works

## Power Automate

- [ ] Request trigger works
- [ ] Approval works
- [ ] Routing works
- [ ] Notification works
- [ ] SLA calculation works
- [ ] SLA notification works
- [ ] Error handling exists

## Power BI

- [ ] KPI dashboard
- [ ] Request analytics
- [ ] Priority analysis
- [ ] Department analysis
- [ ] SLA analysis

## Copilot Studio

- [ ] FAQ knowledge base
- [ ] Basic troubleshooting
- [ ] Escalation
- [ ] Ticket creation integration nếu triển khai được

## Data

- [ ] Data collection
- [ ] Data retrieval
- [ ] Data cleansing
- [ ] Basic analysis

## Testing

- [ ] Functional testing
- [ ] Negative testing
- [ ] UAT
- [ ] Test results documented

## Documentation

- [ ] README
- [ ] Business Requirements
- [ ] Process Flow
- [ ] Architecture
- [ ] Data Dictionary
- [ ] UAT
- [ ] User Guide
- [ ] Troubleshooting
- [ ] Training Material

---

# 27. CV Integration

Chỉ thêm vào CV những phần đã thực sự hoàn thành.

## Project Title

**IT Service Request & Automation Platform | Microsoft Power Platform**

## CV bullet mẫu

Sau khi hoàn thành thật:

```text
• Built an IT service request portal using Microsoft Power Apps for submitting and tracking internal IT requests.

• Automated request approval, assignment, notification, and SLA monitoring workflows using Power Automate.

• Developed a Power BI dashboard to analyze request volume, priority, status, resolution time, and SLA performance.

• Created a Copilot Studio IT support assistant for common troubleshooting and request escalation.

• Designed UAT test cases and project documentation covering business requirements, process flows, user guides, and testing results.
```

Nếu đã thực sự làm AI PoC:

```text
• Developed a proof-of-concept AI workflow to classify IT tickets and suggest request categories and support teams.
```

---

# 28. Những thứ KHÔNG được ghi vào CV

Không được ghi:

```text
Power Apps
Power Automate
Power BI
Copilot Studio
AI Agents
```

với tư cách "experienced" nếu chưa thực sự sử dụng.

Có thể ghi:

```text
Basic
Familiar
Hands-on practice
Project experience
```

nhưng chỉ khi mô tả đó đúng với mức độ thực tế.

Không được tự tạo:

```text
Reduced processing time by 70%
Improved efficiency by 50%
Handled 1,000 tickets
```

nếu chưa có dữ liệu đo lường.

---

# 29. Interview Preparation

Sau project, phải tự trả lời được:

### Power Apps

- What is Power Apps?
- Why did you use Canvas App?
- How does Power Apps connect to SharePoint?
- How did you validate the form?

### Power Automate

- What is a trigger?
- How does your approval flow work?
- How did you calculate SLA?
- How did you handle errors?
- How did you route tickets?

### Power BI

- What KPIs did you choose?
- How did you clean the data?
- What is Power Query?
- Why is dashboard useful for IT management?

### Copilot Studio

- What problem does your chatbot solve?
- How does it retrieve knowledge?
- How does escalation work?
- How can it trigger automation?

### AI

- What is your AI PoC?
- What data does it use?
- What happens if classification is incorrect?
- How would you improve it?

### Business

- What problem does the project solve?
- What process was automated?
- What was the original manual process?
- What improvements can be measured?

---

# 30. 7-Day Execution Plan

## Day 1 — Environment + Data

- [ ] Power Platform environment
- [ ] SharePoint site
- [ ] IT_Requests list
- [ ] Sample data
- [ ] GitHub repository

## Day 2 — Power Apps

- [ ] Home screen
- [ ] Create Request
- [ ] My Requests
- [ ] Request Detail
- [ ] Validation

## Day 3 — Power Automate

- [ ] New Request Flow
- [ ] Approval
- [ ] Assignment
- [ ] Notification

## Day 4 — SLA + Data

- [ ] SLA calculation
- [ ] SLA monitoring
- [ ] SLA notification
- [ ] Data cleansing
- [ ] Power Query

## Day 5 — Power BI

- [ ] KPI cards
- [ ] Request charts
- [ ] Priority analysis
- [ ] Department analysis
- [ ] SLA dashboard

## Day 6 — Copilot Studio + AI PoC

- [ ] IT FAQ bot
- [ ] Troubleshooting
- [ ] Escalation
- [ ] AI ticket classification PoC

## Day 7 — Testing + Documentation

- [ ] Functional testing
- [ ] Negative testing
- [ ] UAT
- [ ] README
- [ ] Process Flow
- [ ] User Guide
- [ ] Screenshots
- [ ] CV update

---

# 31. Final Portfolio Checklist

```text
[ ] Working Power Apps application
[ ] Working Power Automate workflows
[ ] Power BI dashboard
[ ] Copilot Studio chatbot
[ ] AI PoC
[ ] SharePoint data source
[ ] Clean sample dataset
[ ] UAT test cases
[ ] Business requirements
[ ] Process flow
[ ] System architecture
[ ] User guide
[ ] Training material
[ ] GitHub README
[ ] Screenshots
[ ] Demo video (optional)
```

---

# 32. Project Success Criteria

Project đạt mục tiêu nếu có thể demo theo flow:

```text
1. Employee opens Power Apps
        ↓
2. Creates IT request
        ↓
3. Request stored in SharePoint
        ↓
4. Power Automate starts
        ↓
5. Priority checked
        ↓
6. Approval triggered if required
        ↓
7. Ticket automatically assigned
        ↓
8. Employee receives notification
        ↓
9. SLA is monitored
        ↓
10. IT resolves ticket
        ↓
11. Power BI updates analytics
        ↓
12. Employee can ask Copilot for IT help
        ↓
13. Unresolved issue can be escalated
```

---

# 33. Final Objective

Mục tiêu cuối cùng không phải chỉ là "biết Power Platform".

Mục tiêu là có thể chứng minh:

> **I can understand a business process, collect and manage data, build an automated workflow, test the solution, document it, visualize the results, and explore AI-assisted automation.**

Đây là năng lực cần hướng tới khi chuẩn bị cho vị trí **AI & Automation Intern**.

---

## Source / JD Reference

Project này được thiết kế để bám theo JD:

**AI & Automation Intern – Central Service – TP.HCM**

Các yêu cầu chính trong JD gồm Microsoft Power Apps, Power Automate, Power BI, Copilot Studio, data collection/retrieval/cleansing/basic analysis, solution testing, UAT, documentation, process flows, training materials, AI/Copilot PoC, automation monitoring và process improvement.

> **Lưu ý:** Đây là project học tập/portfolio. Các kỹ năng chỉ nên đưa vào CV ở mức độ đúng với những gì đã thực sự triển khai.
