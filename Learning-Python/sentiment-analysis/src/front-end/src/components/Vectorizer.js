import React from "react";

import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import LinearProgress from '@mui/material/LinearProgress';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

import BackEndConnection from './BackEndConnection';

const backend = BackEndConnection.INSTANCE();

const aPageStyle = (displayProgress) => {
    return {
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        flexDirection: 'column',
        marginTop: 25,
        opacity: displayProgress ? 0.2 : 1
    }
}

export default class Vectorizer extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            text: "",
            displayProgress: false,
            result: false,
            convert: ['No', 'Yes']
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
            setTimeout(() => {
                backend.vector_classifying_text(query, (data) => {
                    if (data) {
                        this.setState({ displayProgress: false, result: true, adaboost: data.adaboost_prediction, forest: data.random_forest_prediction, svm: data.svc_prediction });
                    }
                });
            }, 300);
        })
    }

    handleClearText() {
        this.setState({ text: "" });
    };

    render() {
        return (
            <>
                {this.state.displayProgress ? <Box style={{ width: '100%', height: '4px' }}><LinearProgress /></Box> : <Box style={{ height: '4px', width: '100%' }}></Box>}
                <Box style={aPageStyle(this.state.displayProgress)}>
                    <Box width={4 / 5}>
                        <TextField
                            label="Enter or Drag a Text File"
                            variant="outlined"
                            multiline
                            autoFocus
                            rows={10}
                            fullWidth value={this.state.text}
                            onChange={(e) => this.handleTextChange(e)}
                            onDragOver={(e) => this.preventDefault(e)}
                            onDrop={(e) => this.handleDragDrop(e)} />
                        <Box display='flex'>
                            <Box flexGrow={1} />
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
                            <Button variant="contained" size="small" onClick={() => this.handleClearText()}
                                style={{ marginTop: 15, marginLeft: 20, marginBottom: 15 }}>
                                Clear Text
                            </Button>
                            <Button variant="contained" style={{ marginTop: 15, marginLeft: 20, marginBottom: 15 }} size="small" onClick={() => this.processText()}>
                                Process Text
                            </Button>
                        </Box>
                        {this.state.result &&
                            <Box style={{ marginTop: 25 }}>
                                <TableContainer component={Paper}>
                                    <Table>
                                        <TableHead>
                                            <TableRow>
                                                <TableCell width='33%' style={{ fontWeight: 'bold', fontSize: '13px' }}>Adaboost</TableCell>
                                                <TableCell width='33%' style={{ fontWeight: 'bold', fontSize: '13px' }}>SVM</TableCell>
                                                <TableCell width='33%' style={{ fontWeight: 'bold', fontSize: '13px' }}>Random Forest</TableCell>
                                            </TableRow>
                                        </TableHead>
                                        <TableBody>
                                            <TableRow>
                                                <TableCell>{this.state.convert[this.state.adaboost]}</TableCell>
                                                <TableCell>{this.state.convert[this.state.svm]}</TableCell>
                                                <TableCell>{this.state.convert[this.state.forest]}</TableCell>
                                            </TableRow>
                                        </TableBody>
                                    </Table>
                                </TableContainer>
                            </Box>}
                    </Box>
                </Box>
            </>
        );
    }
}