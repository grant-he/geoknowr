import React, { useState } from 'react';
import './App.css'

function App() {
    const [page, setPage] = useState('upload'); // 'upload', 'loading', 'result'
    const [result, setResult] = useState(null);

    const handleSubmit = async (event) => {
        event.preventDefault();
        const formData = new FormData(event.target);

        setPage('loading'); // Transition to the loading page

        try {
            const formDataWithField = new FormData();
            formDataWithField.append('image', formData.get('image'));

            console.log('Sending request to /api/push/know with form data:');
            const response = await fetch('http://localhost:8000/api/push/know', {
                method: 'POST',
                body: formDataWithField,
            });
            console.log('Response status:', response.status);

            if (!response.body) {
                throw new Error('ReadableStream not supported in this browser.');
            }

            const reader = response.body.getReader();
            const decoder = new TextDecoder('utf-8');
            let resultText = '';

            const loadingDiv = document.createElement('div');
            loadingDiv.textContent = 'Processing: ';
            document.body.appendChild(loadingDiv);

            while (true) {
                const { done, value } = await reader.read();
                if (done) break;

                const chunk = decoder.decode(value, { stream: true });
                console.log('Received chunk:', chunk);
                resultText += chunk;
                loadingDiv.textContent = `Processing: ${resultText}`;
            }

            loadingDiv.remove();

            if (!response.ok) {
                throw new Error('Failed to analyze image');
            }

            setResult(resultText);
            setPage('result');
        } catch (error) {
            console.error(error);
            alert('An error occurred while analyzing the image.');
            setPage('upload'); // Go back to the upload page on error
        }
    };

    if (page === 'loading') {
        return <div>Loading...</div>;
    }

    if (page === 'result') {
        return (
            <div className="result-page">
            <h1>Analysis Result</h1>
            <pre className="result-data" style={{ whiteSpace: 'pre-wrap', wordWrap: 'break-word' }}>
                {JSON.stringify(result, null, 2)}
            </pre>
            <button className="upload-again-btn" onClick={() => setPage('upload')}>
                Upload Another Image
            </button>
            </div>
        );
    }

    return (
        <div>
            <h1>Upload an Image</h1>
            <form 
                onSubmit={handleSubmit} 
                encType="multipart/form-data"
            >
                <div>
                    <label htmlFor="imageUpload">
                        Choose an image:
                    </label>
                </div>
                <div>
                    <input 
                        type="file" 
                        id="imageUpload" 
                        name="image" 
                        accept="image/*" 
                        required 
                    />
                </div>
                <div>
                    <button type="submit">
                        Upload
                    </button>
                </div>
            </form>
        </div>
    );
}

export default App;