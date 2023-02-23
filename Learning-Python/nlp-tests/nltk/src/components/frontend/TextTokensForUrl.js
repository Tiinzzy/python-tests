import React from 'react';

import Box from '@mui/system/Box';
import Divider from '@mui/material/Divider';
import Button from '@mui/material/Button';

import CommonWordsUrl from './CommonWordsUrl';
import { shared } from './helper';

import './style.css';

export default class TextTokensForUrl extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            data: props.data,
            tokens: [],
            cleanTokens: []
        };
        this.callTextTokensForUrl = this.callTextTokensForUrl.bind(this);
        shared.callTextTokensForUrl = this.callTextTokensForUrl;
    }

    getText() {
        this.setState({ text: this.state.data.text, tokens: [], commonWords: '', cleanTokens: [] });
    }

    getTokens() {
        let tokens = [];
        for (let i in this.state.data.tokens) {
            tokens[i] = [i, this.state.data.tokens[i]];
        }
        this.setState({ tokens: tokens, text: null, cleanTokens: [], commonWords: '' });
    }

    getCleanTokens() {
        let cleanTokens = [];
        for (let i in this.state.data.nonStopWord) {
            cleanTokens[i] = [i, this.state.data.nonStopWord[i]];
        }
        this.setState({ cleanTokens: cleanTokens, text: null, tokens: [], commonWords: '' });
    }

    callTextTokensForUrl(e) {
        if (e.action === 'get-common-words-for-url') {
            let common_words = [];
            let info = e.data.common_words;
            for (let i in info) {
                common_words[i] = [info[i][0], info[i][1]];
            }
            this.setState({ commonWords: common_words, text: null, cleanTokens: [], tokens: [] })
        }
    }

    render() {
        return (
            <Box className="MainTextTokenBox">
                <Divider style={{ marginBottom: 20 }} color="#4c4c4c" />
                <Box display='flex'>
                    <Button variant="contained" className='GetTokensBtn' size='medium' onClick={() => this.getText()}>Text</Button>
                    <Button variant="contained" className='GetTokensBtn' size='medium' onClick={() => this.getTokens()} >Tokens</Button>
                    <Button variant="contained" className='GetTokensBtn' size='medium' onClick={() => this.getCleanTokens()} >CLean Tokens</Button>
                    <CommonWordsUrl />
                </Box>

                {this.state.text !== null && <Box className="DataDisplayBox">{this.state.text}</Box>}

                {this.state.tokens.length > 0 &&
                    <Box className="DataDisplayBox">
                        <table width="100%">
                            <tbody >
                                <tr>
                                    <th>index</th>
                                    <th>Tokenized Word</th>
                                </tr>
                                {this.state.tokens.map((e, i) => (
                                    <tr key={i} >
                                        <td>
                                            {e[0]}
                                        </td>
                                        <td>
                                            {e[1]}
                                        </td>
                                    </tr>))}
                            </tbody>
                        </table>
                    </Box>}
                {this.state.cleanTokens.length > 0 &&
                    <Box className="DataDisplayBox">
                        <table width="100%">
                            <tbody >
                                <tr>
                                    <th>index</th>
                                    <th>Clean Tokenized Word</th>
                                </tr>
                                {this.state.cleanTokens.map((e, i) => (
                                    <tr key={i} >
                                        <td>
                                            {e[0]}
                                        </td>
                                        <td>
                                            {e[1]}
                                        </td>
                                    </tr>))}
                            </tbody>
                        </table>
                    </Box>}
                {this.state.commonWords &&
                    <Box className="DataDisplayBox">
                        <table width="100%">
                            <tbody >
                                <tr>
                                    <th>Word</th>
                                    <th>Count</th>
                                </tr>
                                {this.state.commonWords.map((e, i) => (
                                    <tr key={i} >
                                        <td>
                                            {e[0]}
                                        </td>
                                        <td>
                                            {e[1]}
                                        </td>
                                    </tr>))}
                            </tbody>
                        </table>
                    </Box>}


            </Box>
        );
    }
};