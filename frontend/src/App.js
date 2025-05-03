import React, { useState } from 'react';

function App() {
    const [page, setPage] = useState('upload'); // 'upload', 'loading', 'result'
    const [result, setResult] = useState(null);

    const handleSubmit = async (event) => {
        event.preventDefault();
        const formData = new FormData(event.target);

        setPage('loading'); // Transition to the loading page

        try {
            const response = await fetch('http://localhost:5000/analyze_image', {
                method: 'POST',
                body: formData,
            });

            if (!response.ok) {
                throw new Error('Failed to analyze image');
            }

            const data = await response.json();
            setResult(data); // Save the result
            setPage('result'); // Transition to the result page
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
            <div>
                <h1>Analysis Result</h1>
                <pre>{JSON.stringify(result, null, 2)}</pre>
                <button onClick={() => setPage('upload')}>Upload Another Image</button>
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