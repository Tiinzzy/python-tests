import React from 'react';

import TextField from '@mui/material/TextField';
import Box from '@mui/system/Box';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';

import BackEndConnection from './BackEndConnection';
import { shared } from './helper';

import { Base64 } from 'js-base64';

import './style.css';


const backend = BackEndConnection.INSTANCE();

export default class EnterUrl extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            url: null,
            value: 'https://www.cnn.com/'
        };
    }

    getTextfieldValue(e) {
        this.setState({ value: e.target.value });
    }

    submitUrl() {
        let url = Base64.encode(this.state.value);
        let that = this;
        backend.send_url_to_backend(url, (data) => {
            that.setState({ data: data });
            shared.callInitUrlProcess({ action: 'url-data-is-read', data: data, name: this.state.value })
        })
    }

    render() {
        return (
            <>
                <Box className="GetUrlBox">
                    <Typography mb={1} fontSize={18} variant="body1">Enter URL</Typography>
                    <TextField value={this.state.value} variant="outlined" onChange={(e) => this.getTextfieldValue(e)} />
                    <Box className="SUbmitBtnBox">
                        <Button variant="contained" className='SunbmitBtn' size='large' onClick={() => this.submitUrl()}>Submit</Button>
                    </Box>                    
                </Box >
            </>
        );
    }
};