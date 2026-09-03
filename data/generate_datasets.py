import os
import pandas as pd
from datetime import datetime, timedelta
import random

os.makedirs('data', exist_ok=True)
os.makedirs('screenshots/powerapps', exist_ok=True)
os.makedirs('screenshots/powerautomate', exist_ok=True)
os.makedirs('screenshots/powerbi', exist_ok=True)
os.makedirs('screenshots/copilot', exist_ok=True)
os.makedirs('docs', exist_ok=True)

# 1. Sample Employees
employees_data = [
    {"EmployeeID": "EMP001", "FullName": "Nguyễn Văn An", "Email": "an.nguyen@company.com", "Department": "Finance", "JobTitle": "Financial Analyst", "ManagerEmail": "manager.finance@company.com"},
    {"EmployeeID": "EMP002", "FullName": "Trần Thị Bích", "Email": "bich.tran@company.com", "Department": "HR", "JobTitle": "HR Specialist", "ManagerEmail": "manager.hr@company.com"},
    {"EmployeeID": "EMP003", "FullName": "Lê Hoàng Cường", "Email": "cuong.le@company.com", "Department": "Supply Chain", "JobTitle": "Supply Chain Executive", "ManagerEmail": "manager.sc@company.com"},
    {"EmployeeID": "EMP004", "FullName": "Phạm Minh Đức", "Email": "duc.pham@company.com", "Department": "Commercial", "JobTitle": "Key Account Manager", "ManagerEmail": "manager.comm@company.com"},
    {"EmployeeID": "EMP005", "FullName": "Hoàng Thị Giang", "Email": "giang.hoang@company.com", "Department": "Legal & Compliance", "JobTitle": "Compliance Officer", "ManagerEmail": "manager.legal@company.com"},
    {"EmployeeID": "EMP006", "FullName": "Vũ Hải Nam", "Email": "nam.vu@company.com", "Department": "Marketing", "JobTitle": "Marketing Specialist", "ManagerEmail": "manager.mkt@company.com"},
    {"EmployeeID": "EMP007", "FullName": "Đặng Thu Thảo", "Email": "thao.dang@company.com", "Department": "IT", "JobTitle": "Service Desk Engineer", "ManagerEmail": "manager.it@company.com"},
    {"EmployeeID": "EMP008", "FullName": "Bùi Quốc Thịnh", "Email": "thinh.bui@company.com", "Department": "IT", "JobTitle": "Network Engineer", "ManagerEmail": "manager.it@company.com"},
    {"EmployeeID": "EMP009", "FullName": "Ngô Mai Phương", "Email": "phuong.ngo@company.com", "Department": "IT", "JobTitle": "Application Support Specialist", "ManagerEmail": "manager.it@company.com"},
    {"EmployeeID": "EMP010", "FullName": "Trương Tấn Dũng", "Email": "dung.truong@company.com", "Department": "IT", "JobTitle": "IT Service Desk Manager", "ManagerEmail": "director.it@company.com"}
]

df_employees = pd.DataFrame(employees_data)
df_employees.to_excel('data/sample_employees.xlsx', index=False)

# 2. Sample Clean IT Requests (60 records for SharePoint import / Power BI)
request_types = ["Hardware", "Software", "Network", "Account", "Microsoft 365", "Access Request", "Other"]
priorities = ["Low", "Medium", "High", "Critical"]
statuses = ["New", "Pending Approval", "Approved", "In Progress", "Resolved", "Closed"]
it_agents = ["thao.dang@company.com", "thinh.bui@company.com", "phuong.ngo@company.com"]

sample_issues = {
    "Hardware": [
        ("Màn hình laptop Dell bị sọc ngang nhấp nháy", "Low", "Hardware"),
        ("Bàn phím ngoài không nhận tín hiệu USB", "Low", "Hardware"),
        ("Pin laptop chai nhanh, sạc không vào điện", "Medium", "Hardware"),
        ("Cần cấp thêm 1 màn hình phụ 24 inch làm việc", "Medium", "Hardware"),
        ("Máy in tầng 3 kẹt giấy liên tục và báo lỗi mực", "High", "Hardware")
    ],
    "Software": [
        ("Lỗi crash khi mở ứng dụng SAP ERP", "High", "Software"),
        ("Yêu cầu cài đặt phần mềm Adobe Acrobat Pro", "Medium", "Software"),
        ("Excel bị đơ và treo khi xử lý Power Query lớn", "Low", "Software"),
        ("Cập nhật phiên bản Power BI Desktop mới nhất", "Low", "Software"),
        ("Phần mềm kế toán MISA báo lỗi kết nối máy chủ", "High", "Software")
    ],
    "Network": [
        ("Không thể kết nối vào mạng VPN công ty từ nhà", "Medium", "Network"),
        ("Mạng Wi-Fi tầng 5 chập chờn, mất kết nối liên tục", "High", "Network"),
        ("Tốc độ mạng nội bộ văn phòng rất chậm", "Medium", "Network"),
        ("Mất kết nối Internet toàn bộ phòng Commercial", "Critical", "Network"),
        ("IP tĩnh máy in văn phòng bị xung đột địa chỉ", "Medium", "Network")
    ],
    "Account": [
        ("Quên mật khẩu đăng nhập Windows và bị khóa tài khoản", "Medium", "Account"),
        ("Cần mở khóa tài khoản Active Directory do nhập sai pass", "High", "Account"),
        ("Tạo tài khoản người dùng mới cho nhân viên thử việc", "Medium", "Account"),
        ("Yêu cầu kích hoạt xác thực 2 bước MFA trên điện thoại mới", "Low", "Account"),
        ("Thu hồi tài khoản và quyền truy cập của nhân viên nghỉ việc", "High", "Account")
    ],
    "Microsoft 365": [
        ("Outlook không gửi nhận được email bên ngoài", "High", "Microsoft 365"),
        ("Không đồng bộ được file OneDrive với máy tính", "Medium", "Microsoft 365"),
        ("Tài khoản Teams bị mất mic khi tham gia họp", "Low", "Microsoft 365"),
        ("Cần cấp bản quyền Microsoft 365 E5 cho phòng Phân tích", "Medium", "Microsoft 365"),
        ("Lỗi bảo mật khi mở file đính kèm trong Outlook", "High", "Microsoft 365")
    ],
    "Access Request": [
        ("Yêu cầu cấp quyền truy cập folder Shared Drive phòng Finance", "Medium", "Access Request"),
        ("Cấp quyền truy cập hệ thống CRM cho Sales Manager mới", "High", "Access Request"),
        ("Yêu cầu quyền xem Dashboard doanh thu trên Power BI", "Low", "Access Request"),
        ("Yêu cầu cấp quyền Admin tạm thời để cài driver máy in", "Medium", "Access Request"),
        ("Truy cập cơ sở dữ liệu Data Warehouse để trích xuất báo cáo", "High", "Access Request")
    ],
    "Other": [
        ("Hỗ trợ setup máy chiếu phòng họp lớn cho hội thảo", "Medium", "Other"),
        ("Tư vấn cấu hình máy tính mua mới cho phòng Media", "Low", "Other"),
        ("Yêu cầu vệ sinh định kỳ laptop văn phòng", "Low", "Other")
    ]
}

sla_hours_map = {
    "Critical": 4,
    "High": 8,
    "Medium": 24,
    "Low": 72
}

base_date = datetime(2026, 8, 1, 8, 0, 0)
clean_requests = []

random.seed(42)

for i in range(1, 61):
    req_type = random.choice(request_types)
    desc, prio, cat = random.choice(sample_issues[req_type])
    
    emp = random.choice(employees_data[:6]) # Regular employees
    
    created_time = base_date + timedelta(days=random.randint(0, 30), hours=random.randint(8, 17), minutes=random.randint(0, 59))
    sla_hours = sla_hours_map[prio]
    sla_deadline = created_time + timedelta(hours=sla_hours)
    
    # Status distribution
    r = random.random()
    if r < 0.15:
        status = "New"
        assigned_to = ""
        resolved_date = None
        resolution = ""
    elif r < 0.25:
        status = "Pending Approval" if prio in ["High", "Critical"] else "In Progress"
        assigned_to = random.choice(it_agents) if status == "In Progress" else ""
        resolved_date = None
        resolution = ""
    elif r < 0.50:
        status = "In Progress"
        assigned_to = random.choice(it_agents)
        resolved_date = None
        resolution = ""
    elif r < 0.85:
        status = "Resolved"
        assigned_to = random.choice(it_agents)
        # 80% resolve within SLA, 20% breach SLA
        if random.random() < 0.80:
            res_duration = timedelta(hours=random.uniform(0.5, sla_hours * 0.9))
        else:
            res_duration = timedelta(hours=random.uniform(sla_hours * 1.1, sla_hours * 2.5))
        resolved_date = created_time + res_duration
        resolution = f"Đã kiểm tra và xử lý thành công yêu cầu {req_type.lower()} cho người dùng."
    else:
        status = "Closed"
        assigned_to = random.choice(it_agents)
        res_duration = timedelta(hours=random.uniform(0.5, sla_hours * 0.9))
        resolved_date = created_time + res_duration
        resolution = f"Đã hoàn thành và xác nhận đóng ticket với người dùng."

    # SLA Status check
    sla_breached = False
    if resolved_date and resolved_date > sla_deadline:
        sla_breached = True
    elif not resolved_date and datetime(2026, 9, 2, 12, 0, 0) > sla_deadline:
        sla_breached = True

    clean_requests.append({
        "RequestID": f"REQ-{i:04d}",
        "EmployeeName": emp["FullName"],
        "Email": emp["Email"],
        "Department": emp["Department"],
        "RequestType": req_type,
        "Priority": prio,
        "Description": desc,
        "Status": status,
        "AssignedTo": assigned_to,
        "CreatedDate": created_time.strftime("%Y-%m-%d %H:%M:%S"),
        "SLADeadline": sla_deadline.strftime("%Y-%m-%d %H:%M:%S"),
        "ResolvedDate": resolved_date.strftime("%Y-%m-%d %H:%M:%S") if resolved_date else "",
        "Resolution": resolution,
        "Category": cat,
        "AIClassification": cat,
        "AIConfidence": round(random.uniform(0.85, 0.98), 2),
        "SLABreached": "Yes" if sla_breached else "No"
    })

df_clean = pd.DataFrame(clean_requests)
df_clean.to_excel('data/sample_it_requests.xlsx', index=False)

# 3. Dirty Dataset for Data Cleansing Practice (Phase 5)
dirty_requests = []
for req in clean_requests[:40]:
    d = req.copy()
    # Introduce inconsistent department
    dep = d["Department"]
    if dep == "Finance" and random.random() < 0.4:
        d["Department"] = random.choice(["finance", "FINANCE", "Fin", "Finance Dept."])
    elif dep == "Supply Chain" and random.random() < 0.4:
        d["Department"] = random.choice(["SCM", "supply chain", "SupplyChain", "SUPPLY CHAIN"])
    elif dep == "IT" and random.random() < 0.4:
        d["Department"] = random.choice(["it", "Information Technology", "IT Dept", "I.T"])
    
    # Introduce messy names / casing
    if random.random() < 0.3:
        d["EmployeeName"] = d["EmployeeName"].upper()
    elif random.random() < 0.2:
        d["EmployeeName"] = "  " + d["EmployeeName"] + "  " # Trailing/leading spaces
        
    # Introduce messy emails
    if random.random() < 0.2:
        d["Email"] = d["Email"].replace("@company.com", " @company.com ")

    # Missing values
    if random.random() < 0.15 and d["Status"] in ["Resolved", "Closed"]:
        d["Resolution"] = ""
        
    dirty_requests.append(d)

# Add duplicates
dirty_requests.append(dirty_requests[2].copy())
dirty_requests.append(dirty_requests[5].copy())

df_dirty = pd.DataFrame(dirty_requests)
df_dirty.to_excel('data/dirty_it_requests.xlsx', index=False)

print("Generated sample_employees.xlsx, sample_it_requests.xlsx, and dirty_it_requests.xlsx successfully!")
