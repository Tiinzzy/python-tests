import React from "react";

import Box from '@mui/material/Box';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

import { PATTERN1, PATTERN2, PATTERN3, PATTERN4 } from "./functions";

export default class SentimentAllTable extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            allSentiments: props.allSentiments
        }
    }

    componentDidMount() {
        if (this.state.allSentiments.hasOwnProperty('all_ten')) {
            this.setState({
                titles: this.state.allSentiments.array_of_titles,
                nltk_pormpt: this.state.allSentiments.data.nltk_prompt_sentiment, nltk_titles: this.state.allSentiments.data.nltk_titles_sentiment, nltkScore: this.state.allSentiments.data.nltk_score.compound,
                blob_prompt: this.state.allSentiments.data.text_blob_prompt_sentiment, blob_titles: this.state.allSentiments.data.text_blob_titles_sentiment, blobScore: this.state.allSentiments.data.text_blob_score,
                vader_prompt: this.state.allSentiments.data.vader_prompt_sentiment, vader_titles: this.state.allSentiments.data.vader_titles_sentiment, vaderScore: this.state.allSentiments.data.vader_score
            });
            this.updateStateFromProps(this.props.allSentiments);
        }
    }

    componentDidUpdate(prevProps) {
        if (this.props.allSentiments !== prevProps.allSentiments) {
            this.updateStateFromProps(this.props.allSentiments);
        }
    }

    updateStateFromProps(allSentiments) {
        this.setState({
            titles: allSentiments.array_of_titles,
            nltk_pormpt: allSentiments.data.nltk_prompt_sentiment,
            nltk_titles: allSentiments.data.nltk_titles_sentiment,
            nltkScore: allSentiments.data.nltk_score.compound,
            blob_prompt: allSentiments.data.text_blob_prompt_sentiment,
            blob_titles: allSentiments.data.text_blob_titles_sentiment,
            blobScore: allSentiments.data.text_blob_score,
            vader_prompt: allSentiments.data.vader_prompt_sentiment,
            vader_titles: allSentiments.data.vader_titles_sentiment,
            vaderScore: allSentiments.data.vader_score
        });
    }


    render() {
        return (
            <Box style={{ width: '65%' }}>
                <TableContainer component={Paper}>
                    <Table>
                        <TableHead>
                            <TableRow>
                                <TableCell width='23%'>Sentiment Predictor</TableCell>
                                <TableCell width='35%'>Total Search Prompt Sentiment</TableCell>
                                <TableCell width='34%'>Total All Titles Sentiment</TableCell>
                                <TableCell width='8%'>Scores</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            <TableRow>
                                <TableCell>NLTK Sentiment</TableCell>
                                <TableCell>{this.state.nltk_pormpt}</TableCell>
                                <TableCell>{this.state.nltk_titles}</TableCell>
                                <TableCell>
                                    {this.state.nltkScore && (this.state.nltkScore * 1).toFixed(4)}
                                </TableCell>
                            </TableRow>
                            <TableRow>
                                <TableCell>Text Blob Sentiment</TableCell>
                                <TableCell>{this.state.blob_prompt}</TableCell>
                                <TableCell>{this.state.blob_titles}</TableCell>
                                <TableCell>
                                    {this.state.blobScore && (this.state.blobScore * 1).toFixed(4)}
                                </TableCell>
                            </TableRow>
                            <TableRow>
                                <TableCell>Vader Sentiment</TableCell>
                                <TableCell>{this.state.vader_prompt}</TableCell>
                                <TableCell>{this.state.vader_titles}</TableCell>
                                <TableCell>
                                    {this.state.vaderScore && (this.state.vaderScore * 1).toFixed(4)}
                                </TableCell>
                            </TableRow>
                        </TableBody>
                    </Table>
                </TableContainer>

                <TableContainer component={Paper} style={{ marginTop: '20px' }}>
                    <Table>
                        <TableHead>
                            <TableRow>
                                <TableCell width='10%'>Index</TableCell>
                                <TableCell width='90%'>Title</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {this.state.titles &&
                                this.state.titles.map((e, i) => (
                                    <TableRow key={i}>
                                        <TableCell>{i + 1}</TableCell>
                                        <TableCell>
                                            {e
                                                .replace(PATTERN1, '')
                                                .replace(PATTERN2, '')
                                                .replace(PATTERN3, '')
                                                .replace(PATTERN4, '')}
                                        </TableCell>
                                    </TableRow>
                                ))}
                        </TableBody>
                    </Table>
                </TableContainer>
            </Box>
        );
    }
}