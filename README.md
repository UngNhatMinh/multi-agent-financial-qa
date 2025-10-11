# multi-agent-financial-qa
Hệ thống hỏi–đáp tài chính đa tác tử sử dụng LLM
# Hướng Dẫn Setup Môi Trường Phát Triển

Dưới đây là các bước cần thiết để thiết lập môi trường cục bộ (local environment) cho dự án Multi-Agent Financial QA System.

## 1. Clone Repository

Sử dụng Git để tải mã nguồn về máy:

```bash
git clone <URL_của_repository_của_bạn>
cd <tên_folder_dự_án>
# Tạo môi trường ảo (ví dụ: sử dụng venv)
python -m venv venv
# Kích hoạt môi trường ảo
# Trên Windows (Command Prompt):
# venv\Scripts\activate.bat
# Trên Windows (PowerShell):
# venv\Scripts\Activate.ps1
# Cài đặt các thư viện
pip install -r requirements.txt
OPENAI_API_KEY="sk-..."
python src/retriever.py
# HOẶC: python main.py

## 2. Ghi Lại Lỗi Phát Sinh và Debugging

Đây là nhiệm vụ **QA (Quality Assurance) và Hỗ trợ Debugging** của bạn.

### Cách Thực Hiện:

1.  **Thử nghiệm:** Thường xuyên thực hiện lại các bước trong `SETUP.md` và chạy thử các script chính (`retriever.py`, `main.py`, v.v.) trên nhiều môi trường khác nhau (nếu có thể, ví dụ: Windows và Linux/macOS) để tìm lỗi.
2.  **Lập Bảng Ghi Lại Lỗi:** Sử dụng một Google Sheet hoặc Markdown file chuyên biệt (ví dụ: `ERRORS_LOG.md`) để ghi lại các lỗi gặp phải, ví dụ:

| Thời gian | Thành viên | Mô tả Lỗi | Nguyên nhân (nếu biết) | Hướng Khắc Phục/Debug | Trạng thái |
| :---: | :---: | :--- | :--- | :--- | :---: |
| 11/10 | Nam | `ModuleNotFoundError: No module named 'langchain'` | Quên kích hoạt môi trường ảo hoặc thiếu `pip install -r requirements.txt`. | Thêm bước kiểm tra môi trường ảo vào `SETUP.md`. | Đã Xong |
| 12/10 | A | Lỗi 401 khi gọi API LLM | Khóa API hết hạn/sai định dạng. | Kiểm tra lại file `.env` và format của khóa. | Đang Xử lý |

3.  **Hỗ trợ Debug:** Khi thành viên khác báo lỗi, bạn sẽ là người đầu tiên tìm hiểu nguyên nhân (ví dụ: do cấu hình môi trường, thiếu thư viện, lỗi logic cơ bản) và đưa ra giải pháp, hoặc ít nhất là cô lập được vấn đề để các thành viên code chuyên trách có thể giải quyết nhanh chóng.

---

## 3. Bảng Theo Dõi Tiến Độ Nhóm (Google Sheet)

Đây là công cụ **Quản lý Tiến độ** quan trọng. Hãy lập một Google Sheet với các cột sau và chia sẻ nó với cả nhóm.

| Thành viên | Công việc (Mô-đun/Task) | Trạng thái | Ngày Bắt đầu | Ngày Dự kiến Hoàn thành | Ghi chú/Vấn đề |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **Nam** | QA + Tài liệu (SETUP.md, ERRORS_LOG) | Đang thực hiện | 11/10 | 25/10 | Ưu tiên hoàn thành `SETUP.md` và theo dõi lỗi ban đầu. |
| **A** | Phát triển Agent *Retriever* (Truy xuất Tài liệu) | Đã bắt đầu | 11/10 | 18/10 | Cần chốt nguồn dữ liệu tài chính (vd: báo cáo thường niên, tin tức). |
| **B** | Phát triển Agent *Reasoning* (Phân tích Logic) | Sắp bắt đầu | 15/10 | 22/10 | Đang chờ Agent Retriever hoàn thành để tích hợp. |
| **C** | Tích hợp Multi-Agent và Giao diện (Streamlit/UI) | Chờ | 20/10 | 30/10 | Cần thiết kế luồng giao tiếp giữa các Agents. |

---

## 4. Định Hướng Kỹ thuật cho Đề tài

Đề tài **"Xây dựng hệ thống hỏi-đáp tài chính đa tác tử (Multi-Agent Financial QA System) sử dụng LLMs"** là một đề tài hiện đại và phức tạp.

### Khái niệm cốt lõi:

* **LLMs (Large Language Models):** Là bộ não của hệ thống, xử lý ngôn ngữ tự nhiên, tạo phản hồi, và đôi khi đóng vai trò là bộ điều phối cho các agents.
* **Multi-Agent System:** Thay vì một mô hình lớn làm tất cả, hệ thống được chia thành nhiều "tác tử" (Agents) chuyên biệt, mỗi agent chịu trách nhiệm cho một phần của quá trình xử lý câu hỏi tài chính.

### Các Agent Tiềm năng và Vai trò:

1.  **Financial Query Router/Classifier Agent:**
    * **Nhiệm vụ:** Phân tích câu hỏi của người dùng (ví dụ: "Doanh thu quý 3 của FPT là bao nhiêu?").
    * **Hành động:** Quyết định xem câu hỏi cần truy vấn dữ liệu (RAG), cần tính toán, hay chỉ cần câu trả lời từ kiến thức chung của LLM.
2.  **Financial Retriever Agent (Sử dụng RAG - Retrieval-Augmented Generation):**
    * **Nhiệm vụ:** Tìm kiếm và truy xuất thông tin tài chính liên quan từ cơ sở dữ liệu (Database/Vector Store) đã được lập chỉ mục (ví dụ: báo cáo tài chính, tin tức thị trường).
    * **Đầu ra:** Các đoạn văn bản/báo cáo *nguyên mẫu* chứa câu trả lời.
3.  **Financial Reasoning/Analyst Agent:**
    * **Nhiệm vụ:** Xử lý các tài liệu thô từ Retriever Agent, thực hiện tính toán (nếu cần), và tổng hợp câu trả lời cuối cùng.
    * **Đầu ra:** Câu trả lời **chính xác** và **đầy đủ** theo ngữ cảnh tài chính.

### Công nghệ Khuyến nghị:

* **Framework Agents:** **LangChain** hoặc **LlamaIndex** (cung cấp các công cụ sẵn có để xây dựng và điều phối Multi-Agent).
* **Vector Database:** **ChromaDB**, **Pinecone**, hoặc **FAISS** (để lưu trữ và truy vấn hiệu quả các văn bản tài chính).
* **LLMs:** GPT-4/GPT-3.5 (OpenAI), Gemini (Google), hoặc các mô hình mã nguồn mở như Llama/Mistral đã được tinh chỉnh (Fine-tuned) cho lĩnh vực tài chính.

Nhiệm vụ của bạn là then chốt để đảm bảo tiến độ và chất lượng. Hãy bắt đầu ngay với việc tạo file `SETUP.md` và theo dõi môi trường của cả nhóm! 💪
