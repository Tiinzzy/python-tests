import React from 'react';

import Box from '@mui/system/Box';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';

import CommonWordsFrequency from './CommonWordsFrequency';
import DispersionPlot from './DispersionPlot';
import { shared } from './helper';

import './style.css';

export default class GenericTokenForText extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            dataName: props.dataName,
            service: props.service,
            data: props.data,
            tokens: [],
            cleanTokens: [],
            frequency: null,
            commonWords: null,
            openDialog: false
        };
        this.handleCloseDialog = this.handleCloseDialog.bind(this);
        this.callTokenForText = this.callTokenForText.bind(this);
        shared.callTokenForText = this.callTokenForText;
    }

    getText() {
        let text = (this.state.service === 'text' ? this.state.data.text.text : this.state.data.text);
        this.setState({ text, tokens: [], commonWords: null, cleanTokens: [], frequency: null });
    }

    getTokens() {
        let tokens = [];
        for (let i in this.state.data.tokens) {
            tokens[i] = [i, this.state.data.tokens[i]];
        }
        this.setState({ tokens: tokens, text: null, cleanTokens: [], commonWords: null, frequency: null });
    }

    getCleanTokensUrl() {
        let cleanTokens = [];
        let allWords = [];
        for (let i in this.state.data.nonStopWord) {
            cleanTokens[i] = [i, this.state.data.nonStopWord[i]];
            allWords.push(this.state.data.nonStopWord[i])
        }
        this.setState({ cleanTokens: cleanTokens, text: null, tokens: [], commonWords: null, frequency: null, allWords });
    }

    getCleanTokensText() {
        let cleanTokens = [];
        let allWords = [];
        for (let i in this.state.data.clean) {
            cleanTokens[i] = [i, this.state.data.clean[i]];
            allWords.push(this.state.data.clean[i])
        }
        this.setState({ cleanTokens: cleanTokens, text: null, tokens: [], commonWords: null, frequency: null, allWords });
    }

    getCleanTokens() {
        if (this.state.service === 'text') {
            this.getCleanTokensText()
        } else if (this.state.service === 'url') {
            this.getCleanTokensUrl()
        }
    }

    getDispersionPlot() {
        this.setState({ openDialog: true });
    }

    handleCloseDialog() {
        this.setState({ openDialog: false })
    }

    callTokenForText(e) {
        if (e.action === 'get-common-words-for-text') {
            let common_words = [];
            let info = e.data.common_words;
            for (let i in info) {
                common_words[i] = [info[i][0], info[i][1]];
            }
            this.setState({ commonWords: common_words, text: null, cleanTokens: [], tokens: [], frequency: null });
        } else if (e.action === 'get-common-words-for-url') {
            let common_words = [];
            let info = e.data.common_words;
            for (let i in info) {
                common_words[i] = [info[i][0], info[i][1]];
            }
            this.setState({ commonWords: common_words, text: null, cleanTokens: [], tokens: [], frequency: null })
        } else if (e.action === 'get-frequency-words-for-text') {
            this.setState({ frequency: e.data.freq, text: null, cleanTokens: [], tokens: [], commonWords: null })
        }
    }

    render() {
        return (
            <Box className="MainTextTokenBox">
                <Box className="DataNameBox">
                    <Typography mb={6} fontSize={25} variant="body1" fontWeight="500">Processing data for:
                        <span style={{ marginLeft: 10, fontWeight: 'bold' }}>{this.state.dataName} </span>
                    </Typography>
                </Box>
                <Box className="FunctionalityBtn">
                    <Button variant="contained" className='GetTokensBtn' size='medium' onClick={() => this.getText()}>Text</Button>
                    <Button variant="contained" className='GetTokensBtn' size='medium' onClick={() => this.getTokens()} >Tokens</Button>
                    <Button variant="contained" className='GetTokensBtn' size='medium' onClick={() => this.getCleanTokens()} >CLean Tokens</Button>
                    <Button variant="contained" className='GetTokensBtn' size='medium' onClick={() => this.getDispersionPlot()} >dispersion plot</Button>
                    <CommonWordsFrequency />
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
                                            {e[0] * 1 + 1}
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
                                            {e[0] * 1 + 1}
                                        </td>
                                        <td>
                                            {e[1]}
                                        </td>
                                    </tr>))}
                            </tbody>
                        </table>
                    </Box>}
                {this.state.commonWords !== null &&
                    <Box className="DataDisplayBox">
                        <table width="100%">
                            <tbody >
                                <tr>
                                    <th>index</th>
                                    <th>Word</th>
                                    <th>Count</th>
                                </tr>
                                {this.state.commonWords.map((e, i) => (
                                    <tr key={i} >
                                        <td>
                                            {i + 1}
                                        </td>
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
                {this.state.frequency !== null &&
                    <Box className="DataDisplayBox">
                        <table width="100%">
                            <tbody >
                                <tr>
                                    <th>index</th>
                                    <th>Word</th>
                                    <th>Frequency</th>
                                </tr>
                                {this.state.frequency.map((e, i) => (
                                    <tr key={i} >
                                        <td>
                                            {i + 1}
                                        </td>
                                        <td>
                                            {e[0]}
                                        </td>
                                        <td>
                                            {(e[1] * 1).toFixed(4)}
                                        </td>
                                    </tr>))}
                            </tbody>
                        </table>
                    </Box>}
                <Dialog open={this.state.openDialog} onClose={() => this.handleCloseDialog()}>
                    <DispersionPlot allWords={this.state.allWords} close={this.handleCloseDialog} />
                </Dialog>
            </Box>
        );
    }
};