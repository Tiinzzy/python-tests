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

const COMMON_WORDS_AMOUNT = [-1, 5, 10, 15, 20]

export default class CommonWordsText extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            selectedCount: COMMON_WORDS_AMOUNT[0],
            data: null        };
    }


    getCommonWordValue(e) {
        this.setState({ selectedCount: e.target.value });
        backend.get_common_words(e.target.value, (data) => {
            let that = this;
            that.setState({ data: data }, () => {
                    shared.callTokenForText({ action: 'get-common-words-for-text', data: that.state.data });
            });
        });

        backend.get_frequency_of_words(3, (data) => {
            console.log(data);
        })
    }

    render() {
        return (
            <Box style={{ display: 'flex', flexDirection: 'row' }}>
                <FormControl>
                    <InputLabel id="select-label">Common Words Count</InputLabel>
                    <Select
                        style={{ width: 208 }}
                        labelId="select-label"
                        value={this.state.selectedCount}
                        label="Common Words Count"
                        onChange={(e) => this.getCommonWordValue(e)}>
                        {COMMON_WORDS_AMOUNT.map((e, i) => (
                            <MenuItem key={i} value={e}>
                                {e < 0 ? 'Select a Count' : e}
                            </MenuItem>
                        ))}
                    </Select>
                </FormControl>

                {/* Virtualized List tomorrow */}
            </Box>
        );
    }
};