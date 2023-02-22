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

    render() {
        return (
            <Box style={{marginRight: 15}}>
                <Button size='large' className='SunbmitBtn' variant="contained" component="label">
                    Upload
                    <input hidden id="myFile" multiple type="file" accept="text/plain" />
                </Button>
            </Box>
        );
    }
};