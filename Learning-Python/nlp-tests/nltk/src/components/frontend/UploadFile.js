import React from 'react';

import Box from '@mui/system/Box';
import Button from '@mui/material/Button';

import './style.css';

export default class UploadFile extends React.Component {
    constructor(props) {
        super(props);
        this.state = {

        };

    }

    initReadFile(e) {
        document.getElementById("myFile").addEventListener('change', this.handleFileSelect(e), false);
        let filePath = document.getElementById("myFile").value;
        let fileName = filePath.replace('fakepath', '').replace('C:\\\\', '');
        this.setState({ fileName: fileName })
    }

    handleFileSelect(e) {
        const reader = new FileReader();
        reader.onload = this.handleFileLoad;
        reader.readAsText(e.target.files[0]);
    }

    handleFileLoad(e) {
        console.log('----------------------------')
        console.log(e.target.result);
    }

    render() {
        return (
            <Box style={{ marginRight: 15 }}>
                <Button size='large' className='SunbmitBtn' variant="contained" component="label">
                    Upload
                    <input hidden id="myFile" multiple type="file" accept="text/plain" onChange={(e) => this.initReadFile(e)} />
                </Button>
            </Box>
        );
    }
};