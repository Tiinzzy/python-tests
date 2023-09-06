import React from "react";

import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Typography from "@mui/material/Typography";

import SentimentUserInput from "./SentimentUserInput";
import Vectorizer from "./Vectorizer";

export default class Home extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            displaySentiment: true
        }
    }

    switchPage(pageNum) {
        if (pageNum === 1) {
            this.setState({ displaySentiment: true });
        } else {
            this.setState({ displaySentiment: false });
        }
    }

    render() {
        return (
            <>
                <Box style={{ display: 'flex', alignItems: 'center', justifyContent: 'left', padding: 10, borderBottom: 'solid 2px #41424C', backgroundColor: '#0288d1' }}>
                    <Button variant="text" style={{ color: 'white', marginLeft: 20, marginRight: 15, backgroundColor: this.state.displaySentiment === true && '#EFF8FF33' }} size="small" onClick={() => this.switchPage(1)}>Sentiment Processor</Button>
                    <Button variant="text" style={{ color: 'white', backgroundColor: this.state.displaySentiment === false && '#EFF8FF33'}} size="small" onClick={() => this.switchPage(2)}>Vector Classifier</Button>
                </Box>
                {this.state.displaySentiment ? <SentimentUserInput /> : <Vectorizer />}

            </>

        );
    }
}