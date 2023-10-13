import React from "react";

import Box from '@mui/material/Box';
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import LinearProgress from '@mui/material/LinearProgress';

import BackEndConnection from './BackEndConnection';

const backend = BackEndConnection.INSTANCE();

export default class WordPrediction extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            text: '',
            suggestion: null
        }
    }

    handleTextChange(e) {
        this.setState({ text: e.target.value }, () => {
            if (this.state.text.length >= 14) {
                let query = { 'text': this.state.text.toLowerCase() };
                this.setState({ displayProgress: true }, () => {
                    backend.predict_rest_of_text(query, (data) => {
                        if (data) {
                            this.setState({ displayProgress: false, suggestion: data.result });
                        }
                    });
                })
            } else {
                this.setState({ suggestion: null })
            }
        });
    }

    handleClearText() {
        this.setState({ text: "" });
    };

    processText() {
        let query = { 'text': this.state.text.toLowerCase() };
        this.setState({ displayProgress: true }, () => {
            backend.predict_rest_of_text(query, (data) => {
                if (data) {
                    this.setState({ displayProgress: false, suggestion: data.result }, () => {
                        if (this.state.text.length === 0) {
                            this.setState({ suggestion: null })
                        }
                    });
                }
            });
        })
    }

    render() {
        return (
            <>
                {this.state.displayProgress ? <Box style={{ width: '100%', height: '4px' }}><LinearProgress /></Box> : <Box style={{ height: '4px', width: '100%' }}></Box>}
                <Box style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', flexDirection: 'column', marginTop: 25, marginBottom: 25 }}>
                    <Box width={4 / 5}>
                        <TextField
                            label="Enter a text for prediction of the rest"
                            variant="outlined"
                            multiline
                            autoFocus
                            rows={1}
                            fullWidth value={this.state.text}
                            onChange={(e) => this.handleTextChange(e)} />
                        {this.state.suggestion !== null &&
                            <div style={{ marginTop: 1, backgroundColor: '#F8FCFF', border: 'solid 2px #1769aa', borderRadius: 4, padding: 6 }}>
                                {this.state.suggestion}
                            </div>}
                        <Box display='flex'>
                            <Box flexGrow={1} />
                            <Button variant="contained" size="small" onClick={() => this.handleClearText()}
                                style={{ marginTop: 15, marginLeft: 20, marginBottom: 15 }}>
                                Clear Text
                            </Button>
                            <Button variant="contained" style={{ marginTop: 15, marginLeft: 20, marginBottom: 15 }} size="small" onClick={() => this.processText()}>
                                Predict Rest
                            </Button>
                        </Box>
                    </Box>
                </Box>
            </>

        );
    }
}