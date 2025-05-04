import React, { useState } from 'react';
import { countryFlags } from './flag-map'
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
            let locations = [];

            const infoDiv = document.createElement('div');
            document.body.appendChild(infoDiv);

            while (true) {
                const { done, value } = await reader.read();
                if (done) break;

                const chunk = decoder.decode(value, { stream: true });
                console.log('map:', countryFlags, countryFlags.get(chunk.trim()));
                console.log('Received chunk:', chunk);
                locations.push(chunk);

                // Heading
                const heading = document.createElement('h2');
                const paragraph = document.createElement('p');
                heading.style.textAlign = 'center'; // Center the heading element
                paragraph.style.textAlign = 'center'; // Center the paragraph element
                if (locations.length === 1) {
                    heading.textContent = 'Country';
                    const flag = countryFlags.get(chunk.trim());
                    paragraph.textContent = flag ? `${chunk.trim()} ${flag}` : chunk.trim();
                } else if (locations.length === 2) {
                    heading.textContent = 'State';
                    paragraph.textContent = chunk.trim();
                } else {
                    heading.textContent = 'New Chunk Received';
                    paragraph.textContent = chunk.trim();
                }

                // Paragraph

                infoDiv.appendChild(heading);
                infoDiv.appendChild(paragraph);
            }

            infoDiv.remove();

            if (!response.ok) {
                throw new Error('Failed to analyze image');
            }

            setResult(locations);
            setPage('result');
        } catch (error) {
            console.error(error);
            alert('An error occurred while analyzing the image.');
            setPage('upload'); // Go back to the upload page on error
        }
    };

    if (page === 'loading') {
        return (
            <div style={{ textAlign: 'center' }}>
                <img src="images/globe.gif" alt="Loading..." />
                <p></p>Searching the globe, please wait...
            </div>
        );
    }

    if (page === 'result') {
        const flag = countryFlags.get(result[0]);
        return (
            <div className="result-page" style={{ textAlign: 'center' }}>
            <h1>Analysis Result</h1>
            <div>
                {result[0] && (
                <div>
                    <h2>Country</h2>
                    <p>{flag ? `${result[0]} ${flag}` : result[0]}</p>
                </div>
                )}
                {result[1] && (
                <div>
                    <h2>State</h2>
                    <p>{result[1]}</p>
                </div>
                )}
                {result[1] && (
                <div>
                    <h2>Final Location</h2>
                    <p>{result.join(', ')}</p>
                </div>
                )}
            </div>
            <button 
                className="upload-again-btn" 
                onClick={() => setPage('upload')} 
                style={{ marginTop: '20px' }}
            >
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