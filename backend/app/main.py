# Main FastAPI application entry point
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.api import upload_router, qa
from app.api import health as health_router
from app.api import history_router, status_router
from app.db.database import init_db
from app.repositories.vector_store import VectorStore


app = FastAPI(title="Codebase Q&A with Proof")

@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Codebase Q&A System</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 1200px; margin: 40px auto; padding: 20px; background: #f5f5f5; }
            .container { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            h1 { color: #333; border-bottom: 3px solid #4CAF50; padding-bottom: 10px; }
            .section { margin: 30px 0; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }
            input[type="file"], input[type="text"] { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ddd; border-radius: 4px; }
            button { background: #4CAF50; color: white; padding: 12px 30px; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; }
            button:hover { background: #45a049; }
            #answer { background: #f9f9f9; padding: 20px; border-left: 4px solid #4CAF50; margin-top: 20px; white-space: pre-wrap; }
            .reference { background: #fff3cd; padding: 10px; margin: 10px 0; border-left: 4px solid #ffc107; }
            .ref-header { font-weight: bold; color: #856404; }
            #status { background: #d4edda; padding: 10px; border-radius: 4px; margin-bottom: 20px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🔍 Codebase Q&A System with Proof</h1>
            
            <div id="status"></div>
            
            <div class="section">
                <h2>📤 Upload File</h2>
                <input type="file" id="fileInput" accept=".py,.js,.cpp,.java,.txt,.md">
                <button onclick="uploadFile()">Upload & Index</button>
                <div id="uploadStatus"></div>
            </div>
            
            <div class="section">
                <h2>❓ Ask Question</h2>
                <input type="text" id="question" placeholder="What is this code about?">
                <button onclick="askQuestion()">Ask</button>
                <div id="answer"></div>
                <div id="references"></div>
            </div>
            
            <div class="section">
                <h2>📜 History</h2>
                <button onclick="showHistory()">Show Last 10 Q&A</button>
                <button onclick="clearHistory()">Clear History</button>
                <div id="history"></div>
            </div>
        </div>
        
        <script>
            async function checkStatus() {
                const res = await fetch('/status');
                const data = await res.json();
                document.getElementById('status').innerHTML = 
                    `✅ Backend: ${data.backend} | 📊 Indexed Items: ${data.vector_store_items} | 🤖 LLM: ${data.llm}`;
            }
            
            async function uploadFile() {
                const fileInput = document.getElementById('fileInput');
                const formData = new FormData();
                formData.append('file', fileInput.files[0]);
                
                const res = await fetch('/upload/upload', { method: 'POST', body: formData });
                const data = await res.json();
                document.getElementById('uploadStatus').innerHTML = 
                    `<p style="color: green;">✅ ${data.message}</p>`;
                checkStatus();
            }
            
            async function askQuestion() {
                const question = document.getElementById('question').value;
                const res = await fetch('/qa/ask', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({question})
                });
                const data = await res.json();
                
                document.getElementById('answer').innerHTML = 
                    `<strong>Answer:</strong><br>${data.answer}`;
                
                let refsHtml = '<h3>📚 References (Proof):</h3>';
                if (data.references && data.references.length > 0) {
                    data.references.forEach((ref, i) => {
                        if (typeof ref === 'object') {
                            refsHtml += `
                                <div class="reference">
                                    <div class="ref-header">📄 ${ref.file_path} (Lines ${ref.start_line}-${ref.end_line})</div>
                                    <pre>${ref.content}</pre>
                                </div>`;
                        }
                    });
                }
                document.getElementById('references').innerHTML = refsHtml;
            }
            
            async function showHistory() {
                const res = await fetch('/qa/history');
                const data = await res.json();
                let html = '<h3>Recent Q&A:</h3>';
                data.history.forEach((item, i) => {
                    html += `<div class="reference">
                        <strong>Q:</strong> ${item.question}<br>
                        <strong>A:</strong> ${item.answer}
                    </div>`;
                });
                document.getElementById('history').innerHTML = html;
            }
            
            async function clearHistory() {
                await fetch('/qa/history', { method: 'DELETE' });
                document.getElementById('history').innerHTML = '<p>History cleared!</p>';
            }
            
            checkStatus();
        </script>
    </body>
    </html>
    """

@app.on_event("startup")
def startup():
    init_db()
    vector_store = VectorStore()
    vector_store.load()

app.include_router(upload_router.router, prefix="/upload", tags=["Upload"])
app.include_router(qa.router, prefix="/qa", tags=["QA"])
app.include_router(health_router.router, tags=["Health"])
app.include_router(history_router.router, prefix="/qa", tags=["History"])
app.include_router(status_router.router, tags=["Status"])