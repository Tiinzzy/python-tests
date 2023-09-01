import React from "react";

import Box from '@mui/material/Box';

export default class Table extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            allSentiments: props.allSentiments
        }
    }

    componentDidMount() {
        this.setState({
            nltk_pormpt: this.state.allSentiments.nltk_prompt_sentiment, nltk_titles: this.state.allSentiments.nltk_titles_sentiment, nltkScore: this.state.allSentiments.nltk_score.compound,
            blob_prompt: this.state.allSentiments.text_blob_prompt_sentiment, blob_titles: this.state.allSentiments.text_blob_titles_sentiment, blobScore: this.state.allSentiments.text_blob_score,
            vader_prompt: this.state.allSentiments.vader_prompt_sentiment, vader_titles: this.state.allSentiments.vader_titles_sentiment, vaderScore: this.state.allSentiments.vader_score
        });
        this.updateStateFromProps(this.props.allSentiments);
    }

    componentDidUpdate(prevProps) {
        if (this.props.allSentiments !== prevProps.allSentiments) {
            this.updateStateFromProps(this.props.allSentiments);
        }
    }

    updateStateFromProps(allSentiments) {
        this.setState({
            nltk_pormpt: allSentiments.nltk_prompt_sentiment,
            nltk_titles: allSentiments.nltk_titles_sentiment,
            nltkScore: allSentiments.nltk_score.compound,
            blob_prompt: allSentiments.text_blob_prompt_sentiment,
            blob_titles: allSentiments.text_blob_titles_sentiment,
            blobScore: allSentiments.text_blob_score,
            vader_prompt: allSentiments.vader_prompt_sentiment,
            vader_titles: allSentiments.vader_titles_sentiment,
            vaderScore: allSentiments.vader_score
        });
    }


    render() {
        return (
                <Box style={{ width: '50%' }}>
                    <table width="100%" style={{ fontSize: '80%', backgroundColor: 'white', maring: 5, border: 'solid 1px black' }} cellPadding={0} cellSpacing={1}>
                        <tbody style={{ backgroundColor: 'white', border: 'solid 1px black' }} >
                            <tr style={{ backgroundColor: 'white', border: 'solid 1px black' }}>
                                <th width='30%' style={{ border: 'solid 1px black' }}>Sentiment Predictor</th>
                                <th width='30%' style={{ border: 'solid 1px black' }}>Search Prompt Sentiment</th>
                                <th width='30%' style={{ border: 'solid 1px black' }}>All Titles Sentiment</th>
                                <th width='10%' style={{ border: 'solid 1px black' }}>Scores</th>
                            </tr>
                            <tr style={{ backgroundColor: 'white', border: 'solid 1px black' }}>
                                <td style={{ border: 'solid 1px black' }}>
                                    NLTK Sentiment
                                </td>
                                <td style={{ border: 'solid 1px black' }}>
                                    {this.state.nltk_pormpt}
                                </td>
                                <td style={{ border: 'solid 1px black' }}>
                                    {this.state.nltk_titles}
                                </td>
                                <td style={{ border: 'solid 1px black' }}>
                                    {(this.state.nltkScore * 1).toFixed(4)}
                                </td>
                            </tr>
                            <tr style={{ backgroundColor: 'white', border: 'solid 1px black' }}>
                                <td style={{ border: 'solid 1px black' }}>
                                    Text Blob Sentiment
                                </td>
                                <td style={{ border: 'solid 1px black' }}>
                                    {this.state.blob_prompt}
                                </td>
                                <td style={{ border: 'solid 1px black' }}>
                                    {this.state.blob_titles}
                                </td>
                                <td style={{ border: 'solid 1px black' }}>
                                    {(this.state.blobScore * 1).toFixed(4)}
                                </td>
                            </tr>
                            <tr style={{ backgroundColor: 'white', border: 'solid 1px black' }}>
                                <td style={{ border: 'solid 1px black' }}>
                                    Vader Sentiment
                                </td>
                                <td style={{ border: 'solid 1px black' }}>
                                    {this.state.vader_prompt}
                                </td>
                                <td style={{ border: 'solid 1px black' }}>
                                    {this.state.vader_titles}
                                </td>
                                <td style={{ border: 'solid 1px black' }}>
                                    {(this.state.vaderScore * 1).toFixed(4)}
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </Box>
        );
    }
}