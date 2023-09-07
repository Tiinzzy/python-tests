import React from "react";

import Box from '@mui/material/Box';
import Tooltip from '@mui/material/Tooltip';
import Paper from '@mui/material/Paper';
import TableContainer from '@mui/material/TableContainer';
import Table from '@mui/material/Table';
import TableHead from '@mui/material/TableHead';
import TableBody from '@mui/material/TableBody';
import TableRow from '@mui/material/TableRow';
import TableCell from '@mui/material/TableCell';

import { PATTERN1, PATTERN2, PATTERN3, PATTERN4, tableReadyData, sumAllScores } from "./functions";


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
        let totalScores = sumAllScores(fullDetail);
        this.setState({ fullDetail, totalScores });
    }

    render() {
        return (
            <Box style={{ width: '65%' }}>
                <TableContainer component={Paper}>
                    <Table>
                        <TableHead>
                            <TableRow>
                                <TableCell align="center" style={{ fontWeight: 'bold', fontSize: '13px' }}>Index</TableCell>
                                <TableCell style={{ fontWeight: 'bold', fontSize: '13px' }}>Title</TableCell>
                                <TableCell align="center" style={{ fontWeight: 'bold', fontSize: '13px' }}>NLTK</TableCell>
                                <TableCell align="center" style={{ fontWeight: 'bold', fontSize: '13px' }}>Text Blob</TableCell>
                                <TableCell align="center" style={{ fontWeight: 'bold', fontSize: '13px' }}>Vader</TableCell>
                                <TableCell align="center" style={{ fontWeight: 'bold', fontSize: '13px' }}>Score</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {this.state.fullDetail && this.state.fullDetail.map((e, i) => (
                                <TableRow key={i}>
                                    <TableCell align="center">{e.index}</TableCell>
                                    <TableCell>
                                        {e.title.replace(PATTERN1, '').replace(PATTERN2, '').replace(PATTERN3, '').replace(PATTERN4, '')}
                                    </TableCell>
                                    <TableCell align="center">
                                        <Tooltip title={<div>{e.nltk_sentiment === 'Positive' ? 1 : e.nltk_sentiment === 'Negative' ? -1 : 0}</div>} placement="top" arrow>
                                            <span>{e.nltk_sentiment}</span>
                                        </Tooltip>
                                    </TableCell>
                                    <TableCell align="center">
                                        <Tooltip title={<div>{e.blob_sentiment === 'Positive' ? 1 : e.blob_sentiment === 'Negative' ? -1 : 0}</div>} placement="top" arrow>
                                            <span>{e.blob_sentiment}</span>
                                        </Tooltip>
                                    </TableCell>
                                    <TableCell align="center">
                                        <Tooltip title={<div>{e.vader_sentiment === 'Positive' ? 1 : e.vader_sentiment === 'Negative' ? -1 : 0}</div>} placement="top" arrow>
                                            <span>{e.vader_sentiment}</span>
                                        </Tooltip>
                                    </TableCell>
                                    <TableCell align="center">{e.totalScore}</TableCell>
                                </TableRow>
                            ))}
                            <TableRow >
                                <TableCell align="center">
                                </TableCell>
                                <TableCell>
                                </TableCell>
                                <TableCell align="center">
                                </TableCell>
                                <TableCell align="center">
                                </TableCell>
                                <TableCell align="center" style={{ fontWeight: 'bold', fontSize: '13px' }}>
                                    Total Score
                                </TableCell>
                                <TableCell align="center">
                                    {this.state.totalScores}
                                </TableCell>
                            </TableRow>
                        </TableBody>
                    </Table>
                </TableContainer>
            </Box>
        );
    }
}