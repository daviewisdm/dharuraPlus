// src/pages/ChatPage.tsx
import React, { useState } from 'react';

// Define the shape of the data coming from main.py
interface AdkResponse {
    status: string;
    reply: string;
}

const ChatPage: React.FC = () => {
    const [input, setInput] = useState("");
    const [response, setResponse] = useState("");
    const [loading, setLoading] = useState(false);

    const askPython = async () => {
        setLoading(true);
        try {
            // We pass the input as a query parameter to your FastAPI route
            const res = await fetch(`http://localhost:8000/api/chat?user_message=${encodeURIComponent(input)}`);
            const data: AdkResponse = await res.json();

            setResponse(data.reply);
        } catch (error) {
            console.error("Failed to reach Python backend:", error);
            setResponse("Error: Backend is not running.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div style={{ padding: '20px' }}>
            <h2>ADK Agent Page</h2>
            <input
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Ask the ADK something..."
            />
            <button onClick={askPython} disabled={loading}>
                {loading ? "Thinking..." : "Send"}
            </button>

            <div style={{ marginTop: '20px', border: '1px solid #ccc', padding: '10px' }}>
                <strong>Agent Response:</strong>
                <p>{response}</p>
            </div>
        </div>
    );
};

export default ChatPage;