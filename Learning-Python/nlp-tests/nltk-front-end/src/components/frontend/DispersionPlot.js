import React from 'react';

import Box from '@mui/system/Box';
import DialogContent from '@mui/material/DialogContent';
import DialogTitle from '@mui/material/DialogTitle';
import Button from '@mui/material/Button';
import DialogActions from '@mui/material/DialogActions';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import LinearProgress from '@mui/material/LinearProgress';

import BackEndConnection from './BackEndConnection';
import { shared } from './helper';

import './style.css';

const backend = BackEndConnection.INSTANCE()
const ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];

export default class DispersionPlot extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            close: props.close,
            selectedWords: {},
            loading: false
        };
    }

    componentDidMount() {
        let that = this;
        that.setState({ loading: true }, function () {
            backend.get_all_words((data) => {
                that.setState({ allWords: data.cleanTokens });
                let uniqWOrds = [...new Set(that.state.allWords)];
                let selectedWords = {};
                for (let w in uniqWOrds) {
                    selectedWords[uniqWOrds[w]] = false;
                }
                that.setState({ uniqWOrds, selectedWords, loading: false });
            });

        })
    }

    wordSelected(e) {
        let start = Date.now();
        let selectedWords = this.state.selectedWords;
        selectedWords[e] = !selectedWords[e];
        this.setState({ selectedWords });
    }

    submitWords() {
        let SELECTED_WORDS = [];
        for (let w in this.state.selectedWords) {
            if (this.state.selectedWords[w]) {
                SELECTED_WORDS.push(w);
            }
        }
        let that = this;
        backend.get_dispersion_plot_graph(SELECTED_WORDS.join(','), (data) => {
            let image = document.getElementById('chart_place_holder');
            image.src = 'data:image/png;base64, ' + data.image;
            shared.callTokenForText({ action: 'display-graph' });
            that.state.close();
        })
    }

    render() {
        return (
            <Box>
                <DialogTitle>
                    {"Select the words you would like to compare the frequency across your data:"}
                </DialogTitle>
                <DialogContent>
                    {this.state.loading ?
                        <Box style={{ height: 4, color: 'rgb(31, 76, 142)' }}><LinearProgress color="inherit" /></Box> :
                        <Box style={{ height: 4 }}></Box>}
                    <div className='EachWordDiv'>
                        {this.state.uniqWOrds && this.state.uniqWOrds.sort().map((e, i) => (
                            <FormControlLabel key={i} control={<Checkbox checked={this.state.selectedWords[e]} onChange={() => this.wordSelected(e)} />} label={e} />
                        ))}
                    </div>
                </DialogContent>
                <DialogActions mb={2}>
                    <Button onClick={() => this.submitWords()} variant="contained" className='GetTokensBtn' size='medium'>Submit</Button>
                </DialogActions>

            </Box>
        );
    }
};

