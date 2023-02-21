import React from 'react';

import TextField from '@mui/material/TextField';
import Box from '@mui/system/Box';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';

import { Base64 } from 'js-base64';

import BackEndConnection from './BackEndConnection';
import TextTokens from './TextTokens';

const backend = BackEndConnection.INSTANCE();

export default class Url extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            url: null,
            value: 'https://www.bbc.com/'
        };

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

    render() {
        return (
            <Box>
                <Box style={{ display: 'flex', flexDirection: 'column', justifyContent: 'center', marginTop: 50 }}>
                    <Typography mb={1} fontSize={18} variant="body1">Enter a Url</Typography>
                    <TextField value={this.state.value} variant="outlined" onChange={(e) => this.getTextfieldValue(e)} />

                </Box >
                <Box style={{ justifyContent: 'right', display: 'flex', marginTop: 20 }}>
                    <Button variant="contained" size='large' onClick={() => this.submitUrl()}>Submit</Button>
                </Box>
                {this.state.data &&
                    <TextTokens data={this.state.data} />}
            </Box>
        );
    }
};