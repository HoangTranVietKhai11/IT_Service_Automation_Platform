"""
AI Ticket Classification Proof-of-Concept (PoC)
Project: IT Service Request & Automation Platform (DKSH Project)

Mục tiêu:
- Phân loại tự động loại yêu cầu IT (RequestType: Hardware, Software, Network, Account, Microsoft 365, Access Request, Other)
- Dự đoán mức độ ưu tiên (Priority: Critical, High, Medium, Low)
- Đưa ra độ tin cậy của AI (Confidence Score: 0.0 - 1.0)
- Đề xuất hướng xử lý sơ bộ (Suggested Routing & SLA)
"""

import sys
import os
import re
import unicodedata

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(CURRENT_DIR, "sample_it_requests.xlsx")

def remove_vietnamese_accents(text: str) -> str:
    """Loại bỏ dấu tiếng Việt để đối sánh linh hoạt"""
    if not isinstance(text, str):
        return ""
    text = unicodedata.normalize('NFD', text)
    text = re.sub(r'[\u0300-\u036f]', '', text)
    text = text.replace('đ', 'd').replace('Đ', 'D')
    return text

def clean_text(text: str) -> str:
    """Chuẩn hóa văn bản tiếng Việt"""
    if not isinstance(text, str):
        return ""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text

# Bộ từ khóa nhận diện chuyên sâu (Semantic Rules)
CATEGORY_RULES = {
    "Hardware": ["man hinh", "may tinh", "laptop", "chuot", "ban phim", "may in", "hong", "ket giay", "khong len nguon", "phan cung", "ram", "o cung", "tai nghe", "vo man hinh", "pin"],
    "Network": ["wifi", "wi fi", "mang", "internet", "vpn", "mat mang", "chap chon", "ket noi mang", "lan", "router", "switch", "sap mang"],
    "Microsoft 365": ["outlook", "teams", "onedrive", "sharepoint", "email", "hom thu", "office 365", "m365", "dung luong hom thu"],
    "Account": ["mat khau", "password", "quen mat khau", "khoa tai khoan", "tai khoan", "account", "unlock", "dang nhap", "sso", "reset mat khau"],
    "Access Request": ["quyen truy cap", "xin quyen", "shared drive", "folder", "cap quyen", "phan quyen", "truy cap thu muc", "permission", "access"],
    "Software": ["cai dat", "phan mem", "power bi", "photoshop", "excel", "loi phan mem", "khong mo duoc", "crash", "ung dung", "license", "sap", "erp"]
}

PRIORITY_RULES = {
    "Critical": ["khan cap", "ngung hoat dong", "toan bo", "sap", "toan cong ty", "anh huong nghiem trong", "ngay lap tuc", "he thong chinh", "sap he thong"],
    "High": ["khong lam viec duoc", "gap", "sep", "bao cao gap", "ket", "het han", "mat quyen", "vo man hinh", "khoa tai khoan"],
    "Medium": ["cham", "can ho tro", "hoi", "huong dan", "thinh thoang", "xin quyen", "shared drive"],
    "Low": ["khi nao ranh", "cai them", "tham khao", "nho", "thac mac", "cai dat"]
}

class AITicketClassifier:
    def __init__(self):
        self.category_pipeline = None
        self.priority_pipeline = None
        self.trained = False

    def train(self, df: pd.DataFrame):
        """Huấn luyện mô hình phân loại dựa trên tập dữ liệu IT Requests"""
        print(f"[*] Dang huan luyen mo hinh voi {len(df)} ban ghi...")
        
        X = df['Description'].apply(clean_text)
        y_category = df['RequestType']
        y_priority = df['Priority']

        self.category_pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(ngram_range=(1, 2), min_df=1)),
            ('clf', MultinomialNB(alpha=0.3))
        ])
        self.category_pipeline.fit(X, y_category)

        self.priority_pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(ngram_range=(1, 2), min_df=1)),
            ('clf', MultinomialNB(alpha=0.3))
        ])
        self.priority_pipeline.fit(X, y_priority)

        self.trained = True
        
        pred_cat = self.category_pipeline.predict(X)
        pred_prio = self.priority_pipeline.predict(X)
        
        acc_cat = accuracy_score(y_category, pred_cat) * 100
        acc_prio = accuracy_score(y_priority, pred_prio) * 100
        
        print(f"[+] Huan luyen hoan tat thanh cong!")
        print(f"    - Do chinh xac phan loai su co (RequestType Accuracy): {acc_cat:.1f}%")
        print(f"    - Do chinh xac du doan muc do (Priority Accuracy):    {acc_prio:.1f}%")

    def predict(self, description: str) -> dict:
        """Dự đoán RequestType, Priority và Confidence cho một mô tả sự cố mới"""
        cleaned = clean_text(description)
        normalized = remove_vietnamese_accents(cleaned)
        
        # 1. Dự đoán qua ML Pipeline
        cat_probs = self.category_pipeline.predict_proba([cleaned])[0]
        cat_classes = self.category_pipeline.classes_
        top_cat_idx = np.argmax(cat_probs)
        predicted_cat = cat_classes[top_cat_idx]
        cat_confidence = float(cat_probs[top_cat_idx])

        prio_probs = self.priority_pipeline.predict_proba([cleaned])[0]
        prio_classes = self.priority_pipeline.classes_
        top_prio_idx = np.argmax(prio_probs)
        predicted_prio = prio_classes[top_prio_idx]
        prio_confidence = float(prio_probs[top_prio_idx])

        # 2. Rule-based Semantic Enhancement
        for cat, keywords in CATEGORY_RULES.items():
            for kw in keywords:
                if kw in normalized:
                    predicted_cat = cat
                    cat_confidence = max(cat_confidence, 0.94)
                    break

        for prio, keywords in PRIORITY_RULES.items():
            for kw in keywords:
                if kw in normalized:
                    predicted_prio = prio
                    prio_confidence = max(prio_confidence, 0.92)
                    break

        sla_map = {
            "Critical": "4 gio (SLA Khan cap - Can Quan ly phe duyet)",
            "High": "8 gio (SLA Cao)",
            "Medium": "24 gio (SLA Tieu chuan)",
            "Low": "72 gio (SLA Thap)"
        }

        routing_map = {
            "Hardware": "Hardware & Equipment Support (it-hardware@company.com)",
            "Network": "Network & Infrastructure Team (it-network@company.com)",
            "Software": "Application Support Team (it-software@company.com)",
            "Microsoft 365": "M365 & Cloud Platform Team (it-m365@company.com)",
            "Account": "Identity & Access Management Desk (it-iam@company.com)",
            "Access Request": "Security & Compliance Team (it-iam@company.com)",
            "Other": "IT General Service Desk (it-servicedesk@company.com)"
        }

        return {
            "InputDescription": description,
            "PredictedRequestType": predicted_cat,
            "RequestTypeConfidence": round(float(cat_confidence), 2),
            "PredictedPriority": predicted_prio,
            "PriorityConfidence": round(float(prio_confidence), 2),
            "ExpectedSLA": sla_map.get(predicted_prio, "24 gio"),
            "SuggestedRouting": routing_map.get(predicted_cat, "IT Service Desk")
        }

def run_demo():
    print("=" * 80)
    print(">>> AI TICKET CLASSIFICATION PoC - DKSH AUTOMATION PLATFORM <<<")
    print("=" * 80)

    if not os.path.exists(DATA_PATH):
        print(f"[-] Khong tim thay file {DATA_PATH}")
        return

    df = pd.read_excel(DATA_PATH)
    classifier = AITicketClassifier()
    classifier.train(df)

    test_cases = [
        "Laptop của tôi bị rơi vỡ màn hình không hiển thị được gì nữa",
        "Tôi không thể kết nối vào mạng Wi-Fi công ty sau khi đổi mật khẩu",
        "Quên mật khẩu tài khoản email và máy tính bị khóa sau 5 lần nhập sai",
        "Cần cài đặt phần mềm Adobe Photoshop và Power BI Pro phục vụ làm báo cáo",
        "Xin cấp quyền truy cập vào thư mục Shared Drive phòng Tài chính kế toán",
        "Hệ thống mạng toàn bộ chi nhánh bị sập ngắt kết nối khẩn cấp"
    ]

    print("\n[+] DANG CHAY KIEM THU MAU (AUTOMATED TEST CASES):")
    print("-" * 80)
    for i, test in enumerate(test_cases, 1):
        result = classifier.predict(test)
        print(f"Ticket #{i}: \"{test}\"")
        print(f"  -> Loai su co (RequestType):  {result['PredictedRequestType']} (Do tin cay AI: {result['RequestTypeConfidence']*100:.0f}%)")
        print(f"  -> Muc uu tien (Priority):    {result['PredictedPriority']} (SLA cam ket: {result['ExpectedSLA']})")
        print(f"  -> Doi ngu phu trach (Route): {result['SuggestedRouting']}")
        print("-" * 80)

    # Chế độ tương tác nhập liệu trực tiếp
    if "--interactive" in sys.argv or "-i" in sys.argv:
        print("\n[?] CHE DO NHAP LIEU TRUC TIEP (Go 'exit' de thoat):")
        while True:
            try:
                user_input = input("\nNhap mo ta su co: ").strip()
                if user_input.lower() in ['exit', 'quit', 'q']:
                    break
                if not user_input:
                    continue
                res = classifier.predict(user_input)
                print(f"  -> Loai su co:  {res['PredictedRequestType']} (Confidence: {res['RequestTypeConfidence']*100:.0f}%)")
                print(f"  -> Muc uu tien: {res['PredictedPriority']} (SLA: {res['ExpectedSLA']})")
                print(f"  -> Doi phu trach: {res['SuggestedRouting']}")
            except (KeyboardInterrupt, EOFError):
                break

if __name__ == "__main__":
    run_demo()
