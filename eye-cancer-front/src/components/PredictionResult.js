// PredictionResult.js
import React from 'react';
import './PredictionResult.css';


const PredictionResult = ({ class_name, confidence_score }) => {
    const confidenceInPercentage = (confidence_score * 100).toFixed(2);

    let message;
    if (class_name === "1 Disease_Risk") {
        message = (
            <span>
                We regret to announce that we have detected eye cancer with a prediction of{' '}
                <span className="confidence-score">{confidenceInPercentage}%</span>
            </span>
        );
    } else {
        message = (
            <span>
                We did not detect any disease with a prediction score of{' '}
                <span className="confidence-score">{confidenceInPercentage}%</span>
            </span>
        );
    }

    return (
        <div className='container'>
            <p>{message}</p>
        </div>
    );
};

export default PredictionResult;
