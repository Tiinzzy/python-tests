import React from 'react';

import Box from '@mui/system/Box';
import Divider from '@mui/material/Divider';
import Button from '@mui/material/Button';

import './style.css';

export default class TextTokensUrl extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            data: props.data,
            tokens: [],
            cleanTokens: []
        };

    }

    getText() {
        this.setState({ text: this.state.data.text, tokens: [] });
    }

    getTokens() {
        let tokens = [];
        for (let i in this.state.data.tokens) {
            tokens.push(i + ' --> ' + this.state.data.tokens[i]);
        }
        this.setState({ tokens: tokens, text: null, cleanTokens: [] });
    }

    getCleanTokens() {
        let cleanTokens = [];
        for (let i in this.state.data.nonStopWord) {
            cleanTokens.push(i + ' --> ' + this.state.data.nonStopWord[i]);
        }
        this.setState({ cleanTokens: cleanTokens, text: null, tokens: [] });
    }

    render() {
        return (
            <Box className="MainTextTokenBox">
                <Divider style={{ marginBottom: 20 }} color="#4c4c4c" />
                <Button variant="contained" className='GetTokensBtn' size='medium' onClick={() => this.getText()}>Text</Button>
                <Button variant="contained" className='GetTokensBtn' size='medium' onClick={() => this.getTokens()} >Tokens</Button>
                <Button variant="contained" className='GetTokensBtn' size='medium' onClick={() => this.getCleanTokens()} >CLean Tokens</Button>

                {this.state.text !== null && <Box className="DataDisplayBox">{this.state.text}</Box>}

                {this.state.tokens.length > 0 &&
                    <Box className="DataDisplayBox">
                        {this.state.tokens.map((e, i) => (
                            <div key={i}>{e}</div>
                        ))}
                    </Box>}

                {this.state.cleanTokens.length > 0 &&
                    <Box className="DataDisplayBox">
                        {this.state.cleanTokens.map((e, i) => (
                            <div key={i}>{e}</div>
                        ))}
                    </Box>}
            </Box>
        );
    }
};