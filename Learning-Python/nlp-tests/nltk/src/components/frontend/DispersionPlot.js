import React from 'react';

import Box from '@mui/system/Box';
import DialogContent from '@mui/material/DialogContent';
import DialogTitle from '@mui/material/DialogTitle';
import Button from '@mui/material/Button';
import DialogActions from '@mui/material/DialogActions';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';

import BackEndConnection from './BackEndConnection';
import { shared } from './helper';

import './style.css';

const backend = BackEndConnection.INSTANCE();

export default class DispersionPlot extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            allWords: props.allWords,
            close: props.close,
            selectedWords: {}
        };
    }

    componentDidMount() {
        let uniqWOrds = [...new Set(this.state.allWords)];
        let selectedWords = {};

        for (let w in uniqWOrds) {
            selectedWords[uniqWOrds[w]] = false;
        }

        this.setState({ uniqWOrds, selectedWords })
    }

    wordSelected(e) {
        let start = Date.now();
        let selectedWords = this.state.selectedWords;
        console.log(Object.keys(selectedWords).length);
        selectedWords[e] = !selectedWords[e]
        this.setState({ selectedWords }, function () {
            console.log(Date.now() - start);
        })
    }

    submitWords() {
        let SELECTED_WORDS = [];
        console.log(new Date());
        for (let w in this.state.selectedWords) {
            if (this.state.selectedWords[w]) {
                SELECTED_WORDS.push(w);
            }
        }
        console.log(new Date());

        this.state.close();
        let words = { 'words': SELECTED_WORDS };

        let url = 'http://localhost:8000/get-graph-of-dispersion-plot?words=' + SELECTED_WORDS.join(',')
        let image = document.getElementById('chart_place_holder');
        image.src = url;
        shared.callTokenForText({ action: 'display-graph' })
        // window.open(url, '_blank')
        // backend.get_dispersion_plot_graph(words, (data) => {
        //     console.log(data);
        // })
    }

    render() {
        return (
            <Box>
                <DialogTitle>
                    {"Select the words you would like to compare the frequency across your data:"}
                </DialogTitle>
                <DialogContent>
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

