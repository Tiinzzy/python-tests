import React from 'react';

import Box from '@mui/system/Box';
import Select from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';
import InputLabel from '@mui/material/InputLabel';
import FormControl from '@mui/material/FormControl';


import BackEndConnection from './BackEndConnection';
import { shared } from './helper';

import './style.css';

const backend = BackEndConnection.INSTANCE();

const COMMON_WORDS_AMOUNT = [-1, 5, 10, 15, 20];
const WORD_FREQUENCY = [-1, 5, 10, 15, 20, 'All']

export default class CommonWordsUrl extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            selectedCountCW: COMMON_WORDS_AMOUNT[0],
            data: null,
            selectedCountFW: WORD_FREQUENCY[0],
            all: null
        };
    }


    getCommonWordValue(e) {
        this.setState({ selectedCountCW: e.target.value });
        backend.get_common_words(e.target.value, (data) => {
            let that = this;
            that.setState({ data: data, all: data.all }, () => {
                shared.callTextTokensForUrl({ action: 'get-common-words-for-url', data: that.state.data });
            });
        });
    }

    getFrequencyValue(e) {
        console.log(e.target.value, 'value')
        if (e.target.value === 'All') {
            this.setState({ selectedCountFW: this.state.all })
            console.log(this.state.all)
            console.log(this.state.selectedCountFW, '<<<')

        } else {
            this.setState({ selectedCountFW: e.target.value });
            console.log('>>>', this.state.selectedCountFW)
        }
        backend.get_frequency_of_words(this.state.selectedCountFW, (data) => {
            let that = this;
            that.setState({ data: data }, () => {
                shared.callTextTokensForUrl({ action: 'get-frequency-words-for-url', data: that.state.data });
            });
        })
    }

    render() {
        return (
            <Box style={{ display: 'flex', flexDirection: 'row' }}>
                <FormControl>
                    <InputLabel id="select-label">Common Words Count</InputLabel>
                    <Select
                        style={{ width: 208, marginRight: 15 }}
                        labelId="select-label"
                        value={this.state.selectedCountCW}
                        label="Common Words Count"
                        onChange={(e) => this.getCommonWordValue(e)}>
                        {COMMON_WORDS_AMOUNT.map((e, i) => (
                            <MenuItem key={i} value={e}>
                                {e < 0 ? 'Select a Count' : e}
                            </MenuItem>
                        ))}
                    </Select>
                </FormControl>
                <Box display="flex" flexGrow={1} />
                <FormControl>
                    <InputLabel id="select-label-1">Words Frequency Count</InputLabel>
                    <Select
                        style={{ width: 208 }}
                        labelId="select-label-1"
                        value={this.state.selectedCountFW}
                        label="Words Frequency Count"
                        onChange={(e) => this.getFrequencyValue(e)}>
                        {WORD_FREQUENCY.map((e, i) => (
                            <MenuItem key={i} value={e}>
                                {e < 0 ? 'Select a Count' : e}
                            </MenuItem>
                        ))}
                    </Select>
                </FormControl>
            </Box>
        );
    }
};