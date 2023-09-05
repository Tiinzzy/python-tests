import React from "react";

import Box from '@mui/material/Box';
import Tooltip from '@mui/material/Tooltip';

import { PATTERN1, PATTERN2, PATTERN3, PATTERN4, tableReadyData } from "./functions";

export default class SentimentOneByOneTable extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            allSentiments: props.allSentiments,
            fullDetail: [],
        }
    }

    componentDidMount() {
        this.updateFullDetail(this.props.allSentiments);
    }

    componentDidUpdate(prevProps) {
        if (prevProps.allSentiments !== this.props.allSentiments) {
            this.updateFullDetail(this.props.allSentiments);
        }
    }

    updateFullDetail(allData) {
        let fullDetail = tableReadyData(allData);
        this.setState({ fullDetail });
    }

    render() {
        return (
            <Box style={{ width: '50%' }}>
                <table width="100%" style={{ fontSize: '80%', backgroundColor: 'white', maring: 5, border: 'solid 1px black' }} cellPadding={0} cellSpacing={1}>
                    <tbody style={{ backgroundColor: 'white', border: 'solid 1px black' }} >
                        <tr style={{ backgroundColor: 'white', border: 'solid 1px black' }}>
                            <th width='8%' style={{ border: 'solid 1px black' }}>index</th>
                            <th width='50%' style={{ border: 'solid 1px black' }}>title</th>
                            <th width='10%' style={{ border: 'solid 1px black' }}>NLTK</th>
                            <th width='12%' style={{ border: 'solid 1px black' }}>Text Blob</th>
                            <th width='10%' style={{ border: 'solid 1px black' }}>Vader</th>
                            <th width='10%' style={{ border: 'solid 1px black' }}>Total Score</th>
                        </tr>
                        {this.state.fullDetail && this.state.fullDetail.map((e, i) => (
                            <tr style={{ backgroundColor: 'white', border: 'solid 1px black' }} key={i}>
                                <td style={{ border: 'solid 1px black', padding: 2 }}>
                                    {e.index}
                                </td>
                                <td style={{ border: 'solid 1px black', padding: 2 }}>
                                    {e.title.replace(PATTERN1, '').replace(PATTERN2, '').replace(PATTERN3, '').replace(PATTERN4, '')}
                                </td>
                                <Tooltip title={e.nltk_sentiment === 'Positive' ? 1 : e.nltk_sentiment === 'Negative' ? -1 : 0} placement="top" arrow>
                                    <td style={{ border: 'solid 1px black', padding: 2 }}>
                                        {e.nltk_sentiment}
                                    </td>
                                </Tooltip>
                                <Tooltip title={e.blob_sentiment === 'Positive' ? 1 : e.blob_sentiment === 'Negative' ? -1 : 0} placement="top" arrow>
                                    <td style={{ border: 'solid 1px black', padding: 2 }}>
                                        {e.blob_sentiment}
                                    </td>
                                </Tooltip>
                                <Tooltip title={e.vader_sentiment === 'Positive' ? 1 : e.vader_sentiment === 'Negative' ? -1 : 0} placement="top" arrow>
                                    <td style={{ border: 'solid 1px black', padding: 2 }}>
                                        {e.vader_sentiment}
                                    </td>
                                </Tooltip>
                                <td style={{ border: 'solid 1px black', padding: 2 }}>
                                    {e.totalScore}
                                </td>
                            </tr>
                        ))}

                    </tbody>
                </table>
            </Box>
        );
    }
}