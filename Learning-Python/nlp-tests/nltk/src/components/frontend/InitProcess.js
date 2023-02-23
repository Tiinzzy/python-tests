import React from 'react';

import TextField from '@mui/material/TextField';
import Box from '@mui/system/Box';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';

import { Base64 } from 'js-base64';

import BackEndConnection from './BackEndConnection';
import GenericTokenForText from './GenericTokenForText';
import UploadFile from './UploadFile';
import { shared } from './helper';

import './style.css';

const backend = BackEndConnection.INSTANCE();

export default class InitProcess extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            url: null,
            value: 'https://www.cnn.com/',
            data: null,
            textData: null
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
            that.setState({ data: data, textData: null });
        })
    }

    callInitUrlProcess(e) {
        if (e.action === 'data-is-ready') {
            this.setState({ textData: e.data, data: null });
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

                {/* {this.state.data !== null && this.state.textData === null &&
                    <TextTokensForUrl data={this.state.data} />} */}


                {this.state.data !== null && this.state.textData === null &&
                    <GenericTokenForText data={this.state.data} service='url' />}


                {this.state.textData !== null && this.state.data === null &&
                    <GenericTokenForText data={this.state.textData} service='text' />}



            </Box>
        );
    }
};