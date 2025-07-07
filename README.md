## Smart FAQ Assistant for Dedan Kimathi University of Technology.

This is a Smart FAQ Assistant for Dedan Kimathi University of Technology.

The assistant allows users to ask questions about the Department of Computer Science and IT, general university information, its programs, admissions, campus life, and more. It provides accurate, fast, and contextually relevant answers through a web-based interface and WhatsApp integration.

The system is powered by a Retrieval-Augmented Generation (RAG) pipeline. RAG combines a document retrieval process with a language model to provide precise answers. Instead of relying purely on a pre-trained language model, RAG first searches a local document database (vector store) for relevant information and then uses the language model to generate a complete and accurate response based on the retrieved context. This ensures that the answers are both up-to-date and directly related to the university's specific resources.

The assistant supports both text and voice queries, making it accessible through the Streamlit web interface and WhatsApp messaging.

---

## How to Run

### 1. Clone the project

```bash
git clone https://github.com/jimmymuthoni/Dekut-Smart-Assistant.git
cd Dekut-Smart-Assistant
```

### 2. Create and activate a Python virtual environment

```bash
python3.10 -m venv env
source env/bin/activate
```

### 3. Install all dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your environment variables

Create a `.env` file in the root directory with the following content:

```bash
TWILIO_SID=""
TWILIO_TOKEN=""
TWILIO_WHATSAPP_NUMBER=whatsapp:
HUGGING_FACE_TOKEN=""
```

### 5. Install PyTorch for LLM support

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

### 6. Run the backend server

```bash
cd backend
uvicorn main:app --reload
```

### 7. Run the Streamlit frontend

```bash
cd ../streamlit_ui
streamlit run frontend.py
```

### 8. Set Twilio Webhook

Point your Twilio WhatsApp webhook to:

```bash
https://<your-ngrok-url>/whatsapp
```

### 9. Install Whisper for voice processing

```bash
uv pip install git+https://github.com/openai/whisper.git
```

### 10. Expose the backend server

```bash
ngrok http 8000
```

---

## Screenshots

### 1. Home Page

*(Attach Screenshot 1 here)*

### 2. Asking a Question via Streamlit Interface

*(Attach Screenshot 2 here)*

### 3. WhatsApp Integration Example

*(Attach Screenshot 3 here)*
