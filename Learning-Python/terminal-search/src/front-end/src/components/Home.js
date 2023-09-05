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
                <Box style={{ display: 'flex', alignItems: 'center', justifyContent: 'left', paddingLeft: 20, borderBottom: 'solid 2px #41424C', backgroundColor: '#0288d1' }}>
                    <Typography mt={1} mb={1.5} variant="body1" style={{ color: '#01579d', padding: 5, border: 2, fontWeight: 'bolder' }}>
                        News Title Processor
                    </Typography>
                    <Button variant="text" style={{ color: 'white', marginLeft: 30, marginRight: 5 }} size="small" onClick={() => this.switchPage(1)}>Sentiment</Button>
                    <Button variant="text" style={{ color: 'white' }} size="small" onClick={() => this.switchPage(2)}>Vectorizer</Button>
                </Box>
                {this.state.displaySentiment ? <SentimentUserInput /> : <Vectorizer />}

            </>

        );
    }
}