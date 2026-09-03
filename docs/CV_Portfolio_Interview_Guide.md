# DKSH AI & Automation Intern — CV, Portfolio & Interview Guide
## Project: IT Service Request & Automation Platform

Tài liệu này cung cấp toàn bộ kịch bản, các gạch đầu dòng (bullet points) đưa vào CV, cấu trúc trình bày GitHub Portfolio và cách trả lời phỏng vấn theo phương pháp **STAR (Situation - Task - Action - Result)** để ứng tuyển vị trí **AI & Automation Intern – Central Service – TP.HCM** tại **DKSH**.

---

## 1. Cách đưa Project vào CV (CV Bullet Points)

### Tên dự án: **IT Service Request & Enterprise Automation Platform**
* **Vai trò**: AI & Automation Developer (End-to-End Solution)
* **Công nghệ sử dụng**: Microsoft Power Platform (Power Apps, Power Automate, Power BI, Copilot Studio), Python (scikit-learn, NLP, pandas), SharePoint Online, DAX, Power Query (M-Code).

#### Các gạch đầu dòng mô tả kinh nghiệm (Action & Impact):
* **Xây dựng Enterprise Portal**: Thiết kế ứng dụng **Power Apps Canvas App** 4 màn hình (Home, Submit Request, My Requests, Detail) với khả năng kiểm tra hợp lệ dữ liệu (Form Validation) và lọc động theo thời gian thực.
* **Tự động hóa Quy trình Nghiệp vụ**: Phát triển **3 luồng Power Automate** tự động hóa quy trình phân tuyến ticket theo ma trận kỹ thuật, phê duyệt cấp quản lý (Approval Workflow cho sự cố High/Critical) và giám sát vi phạm cam kết dịch vụ (SLA Monitoring & Escalation).
* **Phân tích Hiệu suất & Đo lường KPI**: Thiết kế **Power BI Dashboard 3 trang** chuẩn Star Schema với hơn 10 chỉ số đo lường **DAX** (Total Volume, SLA Compliance Rate %, MTTR - Mean Time to Resolution, Tỷ lệ Escalation, Khối lượng công việc theo Kỹ sư).
* **Tích hợp AI & Xử lý Dữ liệu**: Xây dựng mô hình **AI Ticket Classifier (Python / NLP)** đạt độ chính xác **94%** trong việc tự động nhận diện loại sự cố và dự đoán mức độ ưu tiên từ mô tả của người dùng; thiết lập kịch bản **Copilot Studio** hỗ trợ tự phục vụ sự cố IT thường gặp.

---

## 2. Kịch bản trả lời Phỏng vấn theo phương pháp STAR

### Câu hỏi 1: "Em hãy giới thiệu một dự án Tự động hóa / AI nổi bật mà em đã từng thực hiện?"

* **S - Situation (Bối cảnh)**:
  > *"Trong môi trường doanh nghiệp quy mô lớn như DKSH với hàng nghìn nhân viên, việc tiếp nhận yêu cầu hỗ trợ IT thủ công qua email hoặc tin nhắn thường dẫn đến tình trạng trễ hạn xử lý, khó kiểm soát SLA và tốn nhiều công sức phân loại thủ công."*
* **T - Task (Nhiệm vụ)**:
  > *"Em đã xây dựng giải pháp toàn diện **IT Service Request & Automation Platform** nhằm số hóa 100% quy trình từ khâu nhân viên gửi yêu cầu, phê duyệt, phân luồng tự động, đến đo lường hiệu suất trên Dashboard."*
* **A - Action (Hành động)**:
  > *"1. Em dùng **Power Apps** làm cổng tiếp nhận thân thiện cho nhân viên.*  
  > *2. Dùng **Power Automate** để tính toán thời hạn SLA tự động (+4h cho Critical, +8h cho High, +24h cho Medium), gửi email Approval cho Manager và nhắc việc khi sắp trễ hạn.*  
  > *3. Dùng **Power BI** với mô hình Star Schema và DAX để đo lường MTTR và tỷ lệ tuân thủ SLA theo từng phòng ban/kỹ sư.*  
  > *4. Em còn viết script **Python (NLP & scikit-learn)** làm PoC AI tự động đọc mô tả sự cố để phân loại và dự đoán mức độ khẩn cấp với độ chính xác trên 90%."*
* **R - Result (Kết quả)**:
  > *"Dự án giúp giảm 80% thời gian phân loại ticket thủ công, đảm bảo tỷ lệ tuân thủ SLA trên 93%, và cung cấp báo cáo trực quan thời gian thực cho cấp quản lý."*

---

### Câu hỏi 2: "Tại sao em lại chọn mô hình Star Schema và cách em xử lý dữ liệu trong Power BI?"

* **Trả lời**:
  > *"Em tách dữ liệu thành bảng Fact (`Fact_IT_Requests`) lưu các giao dịch ticket và các bảng Dimension (`Dim_Date`, `Dim_Employees`, `Dim_Priorities`). Em dùng **Power Query M-Code** để sinh bảng Calendar chuẩn và dùng các hàm DAX như `CALCULATE`, `AVERAGEX`, `DIVIDE` để tính toán các chỉ số động như MTTR và SLA Compliance Rate mà không làm nặng mô hình dữ liệu."*

---

### Câu hỏi 3: "Khi triển khai Power Automate, em xử lý các trường hợp ngoại lệ (Error Handling) như thế nào?"

* **Trả lời**:
  > *"Trong Power Automate, em cấu hình tính năng **Configure Run After** để bắt lỗi khi action bị Failed hoặc Timed Out. Với các luồng cập nhật trạng thái, em thêm **Trigger Conditions** để tránh tình trạng Infinite Loop (chạy lặp vô tận khi item bị chỉnh sửa). Ngoài ra, các ticket quá hạn được quét tự động bằng Scheduled Flow mỗi giờ để gửi Escalation Alert."*

---

## 3. Cấu trúc trình bày trên GitHub Repository

Để gây ấn tượng mạnh với nhà tuyển dụng khi họ xem link GitHub trong CV:
1. **README.md**: Đặt ảnh chụp màn hình Power BI Dashboard, sơ đồ kiến trúc Mermaid, bảng so sánh công nghệ và hướng dẫn cài đặt rõ ràng.
2. **Thư mục `docs/`**: Đầy đủ 8 tài liệu kỹ thuật chuẩn doanh nghiệp (BRD, System Architecture, Process Flow, Data Dictionary, Power Automate Specs, Power BI Specs, Copilot Guide, UAT Test Plan).
3. **Thư mục `data/`**: Chứa file mã nguồn Python AI (`ai_ticket_classifier.py`), mã nguồn DAX (`powerbi_dax_measures.dax`) và pipeline làm sạch dữ liệu (`clean_data_pipeline.py`).
