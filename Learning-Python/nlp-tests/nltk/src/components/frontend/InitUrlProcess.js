import React from 'react';

import TextField from '@mui/material/TextField';
import Box from '@mui/system/Box';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';

import { Base64 } from 'js-base64';

import BackEndConnection from './BackEndConnection';
import TextTokens from './TextTokens';
import UploadFile from './UploadFile';
import { shared } from './helper';

import './style.css';

const backend = BackEndConnection.INSTANCE();

export default class InitUrlProcess extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            url: null,
            value: 'https://www.cnn.com/'
        };
        this.callInitUrlProcess = this.callInitUrlProcess.bind(this);
        shared.callInitUrlProcess = this.callInitUrlProcess;
    }

    getTextfieldValue(e) {
        this.setState({ url: e.target.value })
    }

    submitUrl() {
        let url = Base64.encode(this.state.value);
        let that = this;
        backend.send_url_to_backend(url, (data) => {
            that.setState({ data: data });
        })
    }

    callInitUrlProcess(e) {
        if (e.action === 'data-is-ready') {
            this.setState({ data: e.data });
        }
    }

    render() {
        return (
            <Box>
                <Box className="GetUrlBox">
                    <Typography mb={1} fontSize={18} variant="body1">Enter URL</Typography>
                    <TextField value={this.state.value} variant="outlined" onChange={(e) => this.getTextfieldValue(e)} />
                </Box >
                <Box className="SUbmitBtnBox">
                    <UploadFile />

                    <Button variant="contained" className='SunbmitBtn' size='large' onClick={() => this.submitUrl()}>Submit</Button>
                </Box>
                {this.state.data &&
                    <TextTokens data={this.state.data} />}
            </Box>
        );
    }
};