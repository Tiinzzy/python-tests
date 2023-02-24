import React from 'react';

import Box from '@mui/system/Box';
import Button from '@mui/material/Button';

import BackEndConnection from './BackEndConnection';
import { shared } from './helper';

import './style.css';

const backend = BackEndConnection.INSTANCE();

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
        this.setState({ fileName: fileName });
        shared.callInitUrlProcess({ action: 'file-name-is-ready', data: fileName });
    }

    handleFileSelect(e) {
        const reader = new FileReader();
        reader.onload = this.handleFileLoad;
        reader.readAsText(e.target.files[0]);
    }

    handleFileLoad(e) {
        let query = { text: e.target.result };
        backend.send_text_file_to_backend(query, (data) => {
            let that = this;
            let result = { 'text': query, 'clean': data.no_stopwords, 'tokens': data.tokens };
            if (query.text.length > 0) {
                shared.callInitUrlProcess({ action: 'data-is-ready', data: result });
            }
        });
    }

    render() {
        return (
            <Box>
                <Button size='large' className='SunbmitBtn' variant="contained" component="label">
                    Select a file
                    <input hidden id="myFile" multiple type="file" accept="text/plain" onChange={(e) => this.initReadFile(e)} />
                </Button>
            </Box>
        );
    }
};