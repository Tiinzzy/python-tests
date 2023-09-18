import React from "react";

import Box from '@mui/material/Box';
import Button from '@mui/material/Button';

import SentimentUserInput from "./SentimentUserInput";
import Vectorizer from "./Vectorizer";
import WordPrediction from "./WordPrediction";


export default class Home extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            pageNumber: 1
        }
    }

    switchPage(pageNum) {
        if (pageNum === 1) {
            this.setState({ pageNumber: 1 });
        } else if (pageNum === 2) {
            this.setState({ pageNumber: 2 });
        } else if (pageNum === 3) {
            this.setState({ pageNumber: 3 });
        }
    }

    render() {
        return (
            <>
                <Box style={{ display: 'flex', alignItems: 'center', justifyContent: 'left', padding: 10, borderBottom: 'solid 2px #41424C', backgroundColor: '#0288d1' }}>
                    <Button variant="text" style={{ color: 'white', marginLeft: 20, marginRight: 15, backgroundColor: this.state.pageNumber === 1 && '#EFF8FF33' }} size="small" onClick={() => this.switchPage(1)}>News Sentiment Processor</Button>
                    <Button variant="text" style={{ marginRight: 15, marginLeft: 15, color: 'white', backgroundColor: this.state.pageNumber === 2 && '#EFF8FF33' }} size="small" onClick={() => this.switchPage(2)}>Recipe Classifier</Button>
                    <Button variant="text" style={{ marginRight: 15, marginLeft: 15, color: 'white', backgroundColor: this.state.pageNumber === 3 && '#EFF8FF33' }} size="small" onClick={() => this.switchPage(3)}>Word Prediction</Button>
                </Box>
                {this.state.pageNumber === 1 ? <SentimentUserInput /> : this.state.pageNumber === 2 ? <Vectorizer /> : this.state.pageNumber === 3 ? <WordPrediction /> : null}
            </>
        );
    }
}