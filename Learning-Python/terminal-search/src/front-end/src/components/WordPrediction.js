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
            text: ''
        }
    }

    handleTextChange(e) {
        console.log(e.target.value)
        this.setState({ text: e.target.value });
    }

    handleClearText() {
        this.setState({ text: "" });
    };

    processText() {
        let query = { 'text': this.state.text.replace(/[!"'`!?,.-_()]/g, '') };
        this.setState({ displayProgress: true }, () => {
            setTimeout(() => {
                backend.predict_rest_of_text(query, (data) => {
                    console.log(data)
                    if (data) {
                        this.setState({ displayProgress: false });
                    }
                });
            }, 300);
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
                            rows={10}
                            fullWidth value={this.state.text}
                            onChange={(e) => this.handleTextChange(e)} />
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