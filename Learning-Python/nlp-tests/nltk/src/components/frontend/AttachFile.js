import React from 'react';

import Box from '@mui/system/Box';
import Typography from '@mui/material/Typography';
import DownloadForOfflineIcon from '@mui/icons-material/DownloadForOffline';

import UploadFile from './UploadFile';

import './style.css';

export default class AttachFile extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
        };
    }



    render() {
        return (
            <Box className="GetFileBox">
                <Box style={{ fontSize: 60}}><DownloadForOfflineIcon fontSize='inherit' className='UploadIcon'/></Box>
                <Typography mb={2} fontSize={18} variant="body1" fontWeight="500">Select a text file to attach</Typography>
                <UploadFile />
            </Box>
        );
    }
};