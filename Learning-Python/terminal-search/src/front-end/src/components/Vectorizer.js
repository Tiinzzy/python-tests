import React from "react";

import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import LinearProgress from '@mui/material/LinearProgress';

import BackEndConnection from './BackEndConnection';

const backend = BackEndConnection.INSTANCE();

export default class Vectorizer extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            text: "",
            result: "",
            displayProgress: false
        };
    }

    handleTextChange(e) {
        this.setState({ text: e.target.value });
    };

    handleFileUpload(e) {
        const file = e.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (event) => {
                this.setState({ text: event.target.result });
            };
            reader.readAsText(file);
        }
    };

    handleDragDrop(e) {
        e.preventDefault();
        const file = e.dataTransfer.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (event) => {
                this.setState({ text: event.target.result });
            };
            reader.readAsText(file);
        }
    };

    preventDefault(e) {
        e.preventDefault();
    };

    processText() {
        let query = { 'text': this.state.text.replace(/[!"'`!?,.-_()]/g, '') };
        this.setState({ displayProgress: true }, () => {
            backend.vector_classifying_text(query, (data) => {
                if (data.prediction[0] === 0) {
                    this.setState({ result: 'Not a Recipe', displayProgress: false });
                } else {
                    this.setState({ result: 'is a Recipe', displayProgress: false });
                }
            });
        })
    }

    render() {
        return (
            <>
                {this.state.displayProgress ? <Box style={{ width: '100%', height: '4px' }}><LinearProgress /></Box> : <Box style={{ height: '4px', width: '100%' }}></Box>}
                <Box style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', flexDirection: 'column', marginTop: 25 }}></Box>
                <Box style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', flexDirection: 'column', marginTop: 25 }}>
                    <Box>
                        <TextField
                            label="Enter or Drag a Text File"
                            variant="outlined"
                            multiline
                            rows={6}
                            fullWidth
                            value={this.state.text}
                            onChange={(e) => this.handleTextChange(e)}
                            onDragOver={(e) => this.preventDefault(e)}
                            onDrop={(e) => this.handleDragDrop(e)}
                        />
                        <input
                            type="file"
                            accept=".txt"
                            style={{ display: "none" }}
                            id="fileInput"
                            onChange={(e) => this.handleFileUpload(e)} />
                        <label htmlFor="fileInput">
                            <Button variant="contained" style={{ marginTop: 15, marginBottom: 15 }} size="small" onClick={() => { document.getElementById("fileInput").click() }}>
                                Upload Text File
                            </Button>
                        </label>
                        <Button variant="contained" style={{ marginTop: 15, marginLeft: 20, marginBottom: 15 }} size="small" onClick={() => this.processText()}>
                            Process Text
                        </Button>
                        <Typography>The text you have entered is {this.state.result}</Typography>
                    </Box>
                </Box>
            </>
        );
    }
}