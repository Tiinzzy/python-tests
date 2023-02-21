import React from 'react';

import TextField from '@mui/material/TextField';
import Box from '@mui/system/Box';
import Divider from '@mui/material/Divider';
import Button from '@mui/material/Button';

import './style.css';

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
        this.setState({ tokens: tokens });
        console.log(tokens);
    }

    getCleanTokens() {
        this.setState({ cleanTokens: this.state.data.nonStopWord });
        console.log(this.state.cleanTokens);
    }

    render() {
        return (
            <Box className="MainTextTokenBox">
                <Divider style={{ marginBottom: 20 }} color="#4c4c4c" />
                <Button variant="contained" className='GetTokensBtn' size='large' onClick={() => this.getText()}>Text</Button>
                <Button variant="contained" className='GetTokensBtn' size='large' onClick={() => this.getTokens()} >Tokens</Button>
                <Button variant="contained" className='GetTokensBtn' size='large' onClick={() => this.getCleanTokens()} >CLean Tokens</Button>

                {this.state.text !== null && <Box className="DataDisplayBox">{this.state.text}</Box>}
                {/* {this.state.tokens && <Box> {this.state.tokens.forEach((e, i) => {
                    <Box key={i}> {e}</Box>
                })}</Box>} */}
            </Box>
        );
    }
};