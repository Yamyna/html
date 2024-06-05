const express = require('express');
const multer = require('multer');
const path = require('path');
const app = express();

// Set up storage engine using multer
const storage = multer.diskStorage({
    destination: './uploads/',
    filename: function(req, file, cb) {
        cb(null, file.fieldname + '-' + Date.now() + path.extname(file.originalname));
    }
});

// Init upload
const upload = multer({
    storage: storage
}).single('file');

// Upload endpoint
app.post('/upload', (req, res) => {
    upload(req, res, (err) => {
        if (err) {
            res.status(500).json({ message: 'File upload failed', error: err.message });
        } else {
            if (req.file == undefined) {
                res.status(400).json({ message: 'No file selected' });
            } else {
                res.status(200).json({ message: 'File uploaded successfully', file: req.file });
            }
        }
    });
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
