import React from 'react';

import Box from '@mui/system/Box';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';

import GenericTokenForText from './GenericTokenForText';
import AttachFile from './AttachFile';
import EnterUrl from './EnterUrl';
import { shared } from './helper';

import './style.css';

export default class InitProcess extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            data: null,
            textData: null,
            displayAtach: false,
            displayEnterUrl: false,
            displayButtons: true,
            turnOffDisplay: false
        };
        this.callInitUrlProcess = this.callInitUrlProcess.bind(this);
        shared.callInitUrlProcess = this.callInitUrlProcess;
    }

    gotToUrl() {
        this.setState({ displayEnterUrl: true, displayButtons: false });
    }

    callInitUrlProcess(e) {
        if (e.action === 'data-is-ready') {
            this.setState({ textData: e.data, data: null, turnOffDisplay: true });
        } else if (e.action === 'url-data-is-read') {
            this.setState({ data: e.data, textData: null, turnOffDisplay: true, dataName: e.name });
        } else if (e.action === "file-name-is-ready") {
            this.setState({ dataName: e.data });
        }
    }

    selectFile() {
        this.setState({ displayAtach: true, displayButtons: false })
    }

    render() {
        return (
            <Box>
                {this.state.displayButtons === true &&
                    <Box style={{ display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center' }}>
                        <Box className="StartInstruction">
                            <Typography mb={2} fontSize={18} variant="body1" fontWeight="500">Select a file or enter a url to start processing the text</Typography>
                        </Box>
                        <Box className="MainTwoButtons">
                            <Button style={{ marginRight: 20 }} variant="contained" className='SunbmitBtn' size='large' onClick={() => this.selectFile()}>Upload</Button>

                            <Button variant="contained" className='SunbmitBtn' size='large' onClick={() => this.gotToUrl()}>Enter Url</Button>
                        </Box>
                    </Box>}
                {this.state.displayAtach === true && this.state.turnOffDisplay === false && <AttachFile />}
                {this.state.displayEnterUrl === true && this.state.turnOffDisplay === false && <EnterUrl />}
                {this.state.data !== null && this.state.textData === null &&
                    <GenericTokenForText data={this.state.data} service='url' dataName={this.state.dataName} />}

                {this.state.textData !== null && this.state.data === null &&
                    <GenericTokenForText data={this.state.textData} service='text' dataName={this.state.dataName} />}
            </Box>
        );
    }
};