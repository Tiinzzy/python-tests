import React from 'react';

import TextField from '@mui/material/TextField';
import Box from '@mui/system/Box';
import Divider from '@mui/material/Divider';
import Button from '@mui/material/Button';


export default class TextTokens extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            data: props.data,
            tokens: []
        };

    }

    getText() {
        this.setState({ text: this.state.data.text });
    }

    getTokens() {
        let tokens = [];
        for (let i in this.state.data.tokens) {
            tokens.push(i + ' --> ' + this.state.data.tokens[i]);
        }
        this.setState({ tokens: tokens })
        console.log(tokens)
    }

    getCleanTokens() {
        this.setState({ cleanTokens: this.state.data.nonStopWord });
    }

    render() {
        return (
            <Box style={{ marginTop: 20 }}>
                <Divider style={{ marginBottom: 20 }} color="#696969" />
                <Button variant="contained" size='large' onClick={() => this.getText()} style={{ marginRight: 15 }}>Text</Button>
                <Button variant="contained" size='large' onClick={() => this.getTokens()} style={{ marginRight: 15 }}>Tokens</Button>
                <Button variant="contained" size='large' onClick={() => this.getCleanTokens()} style={{ marginRight: 15 }}>CLean Tokens</Button>

                {this.state.text !== null &&
                    <Box style={{ marginTop: 20, overflowY: 'scroll', height: 600, width: 600 }}>{this.state.text}</Box>}
                {this.state.tokens && <Box> {this.state.tokens.forEach((e, i) => {
                    <Box key={i}> {e}</Box>
                })}</Box>}
            </Box>
        );
    }
};