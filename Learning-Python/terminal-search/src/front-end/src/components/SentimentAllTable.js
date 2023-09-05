import React from "react";

import Box from '@mui/material/Box';

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
            <Box style={{ width: '50%' }}>
                <table width="100%" style={{ fontSize: '80%', backgroundColor: 'white', maring: 5, border: 'solid 1px black' }} cellPadding={0} cellSpacing={1}>
                    <tbody style={{ backgroundColor: 'white', border: 'solid 1px black' }} >
                        <tr style={{ backgroundColor: 'white', border: 'solid 1px black' }}>
                            <th width='23%' style={{ border: 'solid 1px black' }}>Sentiment Predictor</th>
                            <th width='35%' style={{ border: 'solid 1px black' }}>Total Search Prompt Sentiment</th>
                            <th width='34%' style={{ border: 'solid 1px black' }}>Total All Titles Sentiment</th>
                            <th width='8%' style={{ border: 'solid 1px black' }}>Scores</th>
                        </tr>
                        <tr style={{ backgroundColor: 'white', border: 'solid 1px black' }}>
                            <td style={{ border: 'solid 1px black', padding: 2 }}>
                                NLTK Sentiment
                            </td>
                            <td style={{ border: 'solid 1px black', padding: 2 }}>
                                {this.state.nltk_pormpt}
                            </td>
                            <td style={{ border: 'solid 1px black', padding: 2 }}>
                                {this.state.nltk_titles}
                            </td>
                            <td style={{ border: 'solid 1px black', padding: 2 }}>
                                {this.state.nltkScore && (this.state.nltkScore * 1).toFixed(4)}
                            </td>
                        </tr>
                        <tr style={{ backgroundColor: 'white', border: 'solid 1px black' }}>
                            <td style={{ border: 'solid 1px black', padding: 2 }}>
                                Text Blob Sentiment
                            </td>
                            <td style={{ border: 'solid 1px black', padding: 2 }}>
                                {this.state.blob_prompt}
                            </td>
                            <td style={{ border: 'solid 1px black', padding: 2 }}>
                                {this.state.blob_titles}
                            </td>
                            <td style={{ border: 'solid 1px black', padding: 2 }}>
                                {this.state.blobScore && (this.state.blobScore * 1).toFixed(4)}
                            </td>
                        </tr>
                        <tr style={{ backgroundColor: 'white', border: 'solid 1px black' }}>
                            <td style={{ border: 'solid 1px black', padding: 2 }}>
                                Vader Sentiment
                            </td>
                            <td style={{ border: 'solid 1px black', padding: 2 }}>
                                {this.state.vader_prompt}
                            </td>
                            <td style={{ border: 'solid 1px black', padding: 2 }}>
                                {this.state.vader_titles}
                            </td>
                            <td style={{ border: 'solid 1px black', padding: 2 }}>
                                {this.state.vaderScore && (this.state.vaderScore * 1).toFixed(4)}
                            </td>
                        </tr>
                    </tbody>
                </table>
                <table width="100%" style={{ fontSize: '80%', backgroundColor: 'white', maring: 5, border: 'solid 1px black', marginTop: 20 }} cellPadding={0} cellSpacing={1}>
                    <tbody style={{ backgroundColor: 'white', border: 'solid 1px black' }} >
                        <tr style={{ backgroundColor: 'white', border: 'solid 1px black' }}>
                            <th width='10%' style={{ border: 'solid 1px black' }}>Index</th>
                            <th width='90%' style={{ border: 'solid 1px black' }}>Title</th>
                        </tr>
                        {this.state.titles && this.state.titles.map((e, i) => (
                            <tr style={{ backgroundColor: 'white', border: 'solid 1px black' }} key={i}>
                                <td style={{ border: 'solid 1px black', padding: 2 }}>
                                    {i + 1}
                                </td>
                                <td style={{ border: 'solid 1px black', padding: 2 }}>
                                    {e.replace(PATTERN1, '').replace(PATTERN2, '').replace(PATTERN3, '').replace(PATTERN4, '')}
                                </td>
                            </tr>))}
                    </tbody>
                </table>
            </Box>
        );
    }
}