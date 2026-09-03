"""
Data Cleansing & Transformation Pipeline (Phase 5)
Project: IT Service Request & Automation Platform (DKSH Project)

Mục tiêu:
- Đọc file dữ liệu lỗi thực tế: dirty_it_requests.xlsx
- Xử lý các lỗi dữ liệu phổ biến trong doanh nghiệp:
  1. Loại bỏ bản ghi trùng lặp (Duplicate records)
  2. Chuẩn hóa tên phòng ban (Department: 'IT', 'it', 'Information Technology' -> 'IT')
  3. Chuẩn hóa định dạng Email (Chữ thường, xóa khoảng trắng thừa)
  4. Chuẩn hóa mức độ ưu tiên (Priority: 'high', 'HIGH', 'H' -> 'High')
  5. Xử lý giá trị trống / Null (Missing values imputation)
  6. Chuẩn hóa định dạng ngày tháng (Date/Time validation)
- Xuất file dữ liệu sạch: cleaned_it_requests.xlsx
"""

import sys
import os
import re
import pandas as pd
import numpy as np

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DIRTY_DATA_PATH = os.path.join(CURRENT_DIR, "dirty_it_requests.xlsx")
CLEANED_DATA_PATH = os.path.join(CURRENT_DIR, "cleaned_it_requests.xlsx")

# Từ điển chuẩn hóa phòng ban (Department Mapping)
DEPARTMENT_MAPPING = {
    "it": "IT",
    "information technology": "IT",
    "cntt": "IT",
    "fin": "Finance",
    "finance dept": "Finance",
    "kế toán": "Finance",
    "tai chinh": "Finance",
    "hr": "HR",
    "human resources": "HR",
    "nhân sự": "HR",
    "mkt": "Marketing",
    "marketing dept": "Marketing",
    "supply chain": "Supply Chain",
    "chuỗi cung ứng": "Supply Chain",
    "logistics": "Supply Chain",
    "commercial": "Commercial",
    "sales": "Commercial",
    "kinh doanh": "Commercial",
    "legal": "Legal & Compliance",
    "compliance": "Legal & Compliance",
    "pháp chế": "Legal & Compliance"
}

# Từ điển chuẩn hóa Mức ưu tiên (Priority Mapping)
PRIORITY_MAPPING = {
    "c": "Critical",
    "crit": "Critical",
    "critical": "Critical",
    "khẩn cấp": "Critical",
    "h": "High",
    "high": "High",
    "cao": "High",
    "m": "Medium",
    "med": "Medium",
    "medium": "Medium",
    "trung bình": "Medium",
    "l": "Low",
    "low": "Low",
    "thấp": "Low"
}

def clean_dataset():
    print("=" * 75)
    print(">>> DATA CLEANSING & TRANSFORMATION PIPELINE (PHASE 5) <<<")
    print("=" * 75)

    if not os.path.exists(DIRTY_DATA_PATH):
        print(f"[-] Khong tim thay file {DIRTY_DATA_PATH}")
        return

    df = pd.read_excel(DIRTY_DATA_PATH)
    initial_rows = len(df)
    print(f"[*] Tong so ban ghi ban dau: {initial_rows} dong")

    # 1. Loại bỏ bản ghi trùng lặp
    df = df.drop_duplicates(subset=['RequestID'], keep='first')
    df = df.drop_duplicates(subset=['Email', 'Description', 'CreatedDate'], keep='first')
    dedup_rows = initial_rows - len(df)
    print(f"    -> Da loai bo {dedup_rows} ban ghi trung lap")

    # 2. Chuẩn hóa Email
    df['Email'] = df['Email'].astype(str).str.strip().str.lower()
    df['Email'] = df['Email'].apply(lambda x: re.sub(r'\s+', '', x))

    # 3. Chuẩn hóa Department
    def standardize_dept(dept):
        if pd.isna(dept):
            return "Other"
        clean_d = str(dept).strip().lower()
        return DEPARTMENT_MAPPING.get(clean_d, str(dept).strip().title())

    df['Department'] = df['Department'].apply(standardize_dept)

    # 4. Chuẩn hóa Priority
    def standardize_prio(prio):
        if pd.isna(prio):
            return "Medium"
        clean_p = str(prio).strip().lower()
        return PRIORITY_MAPPING.get(clean_p, "Medium")

    df['Priority'] = df['Priority'].apply(standardize_prio)

    # 5. Xử lý giá trị trống (Missing values imputation)
    df['Status'] = df['Status'].fillna("New").str.strip()
    df['EmployeeName'] = df['EmployeeName'].fillna("Unknown Employee").str.strip()
    df['Description'] = df['Description'].fillna("No description provided").str.strip()

    # 6. Kiểm tra và định dạng lại ngày tháng
    df['CreatedDate'] = pd.to_datetime(df['CreatedDate'], errors='coerce')
    if 'SLADeadline' in df.columns:
        df['SLADeadline'] = pd.to_datetime(df['SLADeadline'], errors='coerce')
    if 'ResolvedDate' in df.columns:
        df['ResolvedDate'] = pd.to_datetime(df['ResolvedDate'], errors='coerce')

    # Xuất file dữ liệu sạch
    df.to_excel(CLEANED_DATA_PATH, index=False)
    print(f"\n[+] Da lam sach va xuat file thanh cong: {CLEANED_DATA_PATH}")
    print(f"    -> So luong ban ghi sach (Cleaned rows): {len(df)} dong")
    print("=" * 75)

if __name__ == "__main__":
    clean_dataset()
