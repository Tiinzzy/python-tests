import React from 'react';

import Box from '@mui/system/Box';
import Button from '@mui/material/Button';
import DialogActions from '@mui/material/DialogActions';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Divider from '@mui/material/Divider';
import DialogTitle from '@mui/material/DialogTitle';

import BackEndConnection from './BackEndConnection';
import { shared } from './helper';

import './style.css';

const backend = BackEndConnection.INSTANCE()
const ALPHABET = new Array(26).fill(0).map((e, i) => String.fromCharCode(i + 65));

export default class DispersionPlot extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            close: props.close,
            selectedWords: {},
            loading: false,
            filter: null
        };
    }

    componentDidMount() {
        let that = this;
        that.setState({ loading: true }, function () {
            backend.get_all_words((data) => {
                that.setState({ allWords: data.cleanTokens });
                let uniqWOrds = [...new Set(that.state.allWords)];
                let selectedWords = {};
                uniqWOrds.forEach(uw => {
                    selectedWords[uw] = false;
                });
                that.setState({ uniqWOrds, selectedWords, loading: false });
            });
        })
    }

    wordSelected(e) {
        let selectedWords = this.state.selectedWords;
        selectedWords[e] = !selectedWords[e];
        this.setState({ selectedWords });

        let selected = [];
        for (let w in this.state.selectedWords) {
            if (this.state.selectedWords[w]) {
                selected.push(w);
            }
        }
        this.setState({ selected });
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

    filterData(e) {
        this.setState({ filter: e })
    }

    cancelAndClose() {
        this.state.close();
    }

    render() {
        return (
            <Box className="FilterResultBox">
                <DialogTitle id="alert-dialog-title">
                    {"Filter Words"}
                </DialogTitle>

                <Divider />
                <Box className="EachWordDiv">
                    {ALPHABET.map((e, i) => (<div className='EachAlphabetBox' key={i} onClick={() => this.filterData(e)}> {e}</div>))}
                </Box>
                <Divider className='DividerDialog' />

                <Box p={1} style={{ height: 250, border: 'solid 1px #eaeaea', margin: '0px 20px 0px 20px', borderRadius: 2 }}>
                    {this.state.filter !== null && this.state.uniqWOrds &&
                        this.state.uniqWOrds.filter(e => e.startsWith(this.state.filter.toLowerCase())).sort().map((e, i) => (
                            <div key={i} style={{ display: 'inline-block', padding: 5 }}>
                                <FormControlLabel
                                    control={<Checkbox
                                        checked={this.state.selectedWords[e]}
                                        onChange={() => this.wordSelected(e)} />}
                                    label={e} />
                            </div>))}
                </Box>
                <Box className="HelperTextBox">
                    *Select words to compare their frequency across data
                </Box>

                <Box className="SelectedResultBox">
                    Selected Words:
                    {this.state.selected && this.state.selected.map((e, i) => (<div className='EachSelection' key={i}>{e}</div>))}
                </Box>
                <DialogActions>
                    <Button onClick={() => this.cancelAndClose()} variant="contained" className='GetTokensBtn' size='medium'>Cancel</Button>
                    <Button onClick={() => this.submitWords()} variant="contained" className='GetTokensBtn' size='medium'>Submit</Button>
                </DialogActions>

            </Box>
        );
    }
};

