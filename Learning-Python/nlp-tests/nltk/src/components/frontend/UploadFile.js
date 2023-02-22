import React from 'react';

import Box from '@mui/system/Box';
import Button from '@mui/material/Button';

import { shared } from './helper';
import BackEndConnection from './BackEndConnection';

import { Base64 } from 'js-base64';

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
    }

    handleFileSelect(e) {
        const reader = new FileReader();
        reader.onload = this.handleFileLoad;
        reader.readAsText(e.target.files[0]);
    }

    async handleFileLoad(e) {
        let query = { text: e.target.result };
        await backend.send_text_file_to_backend(query, (data) => {
            console.log(data)
        });
        if (query.text.length > 0) {
            shared.callInitUrlProcess({ action: 'data-is-ready', data: query })
        }
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