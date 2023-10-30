import React, { useState, useRef} from 'react';
import axios from 'axios';
import './ImageUploader.css';
import cloudPicture from '../assets/cloud_picture.png'; 
import PredictionResult from './PredictionResult';



const ImageUploader = () => {
    const [files, setFiles] = useState([]);
    const [prediction, setPrediction] = useState(null);
    const [isLoading, setIsLoading] = useState(false);
    const fileInputRef = useRef(null);

    const uploadFiles = async (uploadedFiles) => {
        const formData = new FormData();
        uploadedFiles.forEach(file => {
            formData.append('file', file);
        });
    };

    const handleDragOver = (e) => {
        e.preventDefault();
    };

    const handleDrop = (e) => {
        e.preventDefault();
        const uploadedFiles = Array.from(e.dataTransfer.files).filter(
            (file) => file.type === "image/png"
        );
        setFiles((prevFiles) => [...prevFiles, ...uploadedFiles]);
        uploadFiles(uploadedFiles);
    };

    const handleFileInput = (e) => {
        const uploadedFiles = Array.from(e.target.files).filter(
            (file) => file.type === "image/png"
        );
        setFiles((prevFiles) => [...prevFiles, ...uploadedFiles]);
        uploadFiles(uploadedFiles);
    };

    const handleAnalyzeClick = async () => {
        if (files.length > 0) {
            setIsLoading(true); // Déclenchez l'indicateur de chargement
            const formData = new FormData();
            files.forEach(file => {
                formData.append('file', file);
            });

            try {
                const response = await axios.post(process.env.REACT_APP_API_URL, formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                });

                if (response.status === 200) {
                    console.log(response.data)
                    // Mettre à jour l'état avec les résultats de la prédiction
                    setPrediction(response.data);
                } else {
                    console.error('Error occurred:', response.statusText);
                }
            } catch (error) {
                console.error('An error occurred while sending the data:', error);
            } finally {
                setIsLoading(false); // Réinitialiser l'indicateur de chargement
            }
        } else {
            console.log('No files to analyze.');
        }
    };

    const removeFile = (indexToRemove) => {
        setFiles((prevFiles) => prevFiles.filter((file, index) => index !== indexToRemove));
    };

    return (
        <div className="content-wrapper">
            <div className="uploader-wrapper">
            <div className="uploader-container">
                <div 
                    className="dropzone" 
                    onDragOver={handleDragOver} 
                    onDrop={handleDrop}
                >
                    <img src={cloudPicture} alt="Cloud" style={{ maxWidth: '15%', height: 'auto' }} />

                    <div className='drag-text'>
                        <p>Drag and Drop here 📁</p>
                    </div>
                    <div className='drag-or'>
                        <p>or</p>
                    </div>

                    <div className="drag-button">
                        <button onClick={() => fileInputRef.current.click()}>Browse Files</button>
                        <input 
                            ref={fileInputRef}
                            type="file" 
                            accept=".png, .jpg, .jpeg" 
                            onChange={handleFileInput} 
                            style={{ display: 'none' }}
                        />
                    </div>
                </div>
            </div>
            <div className="uploaded-images-container">
                    {files.map((file, index) => (
                        <div key={index} className="uploaded-image-wrapper">
                            <img 
                                src={URL.createObjectURL(file)} 
                                alt={`upload preview ${index}`}
                                className="uploaded-image"
                            />
                            <button 
                                className="remove-image-button" 
                                onClick={() => removeFile(index)}
                            >
                                ❌ {/* Ici, vous pouvez remplacer par une icône ou une image si vous préférez. */}
                            </button>
                        </div>
                    ))}
                </div>
            </div>
            <button onClick={handleAnalyzeClick} className="analyze-button">Analyse the picture</button>
                        {/* Afficher le composant de résultat si les données de prédiction sont disponibles */}
                        {prediction && !isLoading && (
                <PredictionResult
                    class_name={prediction.class_name}
                    confidence_score={prediction.confidence_score}
                />
            )}
        </div>
    );
};

export default ImageUploader;

