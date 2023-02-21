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
        this.setState({ text: this.state.data.text, tokens: '' });
    }

    getTokens() {
        this.setState({ text: '' });
        let tokens = [];
        for (let i in this.state.data.tokens) {
            tokens.push(i + ' --> ' + this.state.data.tokens[i]);
            let tokenBox = document.getElementById('display-tokens');
            tokenBox.scrollTop = tokenBox.scrollHeight;
        }
        this.setState({ tokens: tokens })
    }

    render() {
        return (
            <Box style={{ marginTop: 20 }}>
                <Divider style={{ marginBottom: 20 }} color="#696969" />
                <Button variant="contained" size='large' onClick={() => this.getTokens()} style={{ marginRight: 15 }}>Tokens</Button>
                <Button variant="contained" size='large' onClick={() => this.getText()}>Text</Button>
                {this.state.text !== null &&
                    <Box style={{ marginTop: 20, overflowY: 'scroll', height: 600, width: 600 }}>{this.state.text}</Box>}
                {this.state.tokens && this.state.tokens.map((e, i) => {
                    <div key={i} id="display-tokens" style={{ overflowY: 'scroll', height: 600, width: 600 }}>{e}</div>
                })}
            </Box>
        );
    }
};