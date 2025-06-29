## This is a Smart FAQ Assistant for Dedan Kimathi University of Technology.

The assistant allows users to ask questions about the department of Computer Science and IT, University information in  general, its programs, admissions, campus life, and more. It provides accurate, fast, and contextually relevant answers through a web-based interface and WhatsApp integration.

The system is powered by a Retrieval-Augmented Generation (RAG) pipeline. RAG combines a document retrieval process with a language model to provide precise answers. Instead of relying purely on a pre-trained language model, RAG first searches a local document database (vector store) for relevant information and then uses the language model to generate a complete and accurate response based on the retrieved context. This ensures that the answers are both up-to-date and directly related to the university's specific resources.

The assistant supports both text and voice queries, making it accessible through Streamlit web interface and WhatsApp messaging.

### How to Run

1. Clone the project:

```bash
git clone https://github.com/jimmymuthoni/Dekut-Smart-Assistant.git
cd Dekut-Smart-Assistant
```

2. Create and activate a Python virtual environment:

```bash
python3.10 -m venv env
source env/bin/activate
```

3. Install all dependencies:

```bash
pip install -r requirements.txt
```

4. Set up your environment variables in a `.env` file.

5. Run the backend:

```bash
cd backend
uvicorn main:app --reload
```

6. Run the Streamlit frontend:

```bash
cd ../streamlit_ui
streamlit run frontend.py
```

7. For WhatsApp integration, set your Twilio webhook to:

```
https://<your-ngrok-url>/whatsapp
```

Make sure to expose your backend using:

```bash
ngrok http 8000
```
