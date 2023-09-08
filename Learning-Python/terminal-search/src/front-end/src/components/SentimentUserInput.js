import React from "react";

import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import InputBase from '@mui/material/InputBase';
import IconButton from '@mui/material/IconButton';
import SearchIcon from '@mui/icons-material/Search';
import LinearProgress from '@mui/material/LinearProgress';

import BackEndConnection from './BackEndConnection';
import DisplayTable from "./DisplayTable";
import RadioButton from "./RadioButton";

const backend = BackEndConnection.INSTANCE();

export default class SentimentUserInput extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            searchItem: '',
            msg: '',
            displayProgress: false
        }
        this.callBack = this.callBack.bind(this);
    }

    getSearchPrompt(e) {
        this.setState({ searchItem: e.target.value });
        let query = { prompt: this.state.searchItem, msg: this.state.msg };
        if (e.keyCode === 13) {
            e.preventDefault();
        }
        let key = e.code || "";
        let isEnter = key.toLowerCase().indexOf('enter') >= 0;
        if (isEnter) {
            this.setState({ displayProgress: true }, () => {
                backend.send_search_prompt(query, (data) => {
                    if (data) {
                        this.setState({ allSentiments: data, titles: data.array_of_titles, displayProgress: false });
                    };
                })
            })
        }
    }

    searchForSentiment() {
        let query = { prompt: this.state.searchItem, msg: this.state.msg };
        this.setState({ displayProgress: true }, () => {
            backend.send_search_prompt(query, (data) => {
                if ((data.hasOwnProperty('array_of_titles') && data.array_of_titles.length === 4) || (data.hasOwnProperty('nltk_step_sentiment') && data.nltk_step_sentiment.length === 4)) {
                    this.setState({ displayProgress: false });
                } else {
                    this.setState({ allSentiments: data, titles: data.array_of_titles, displayProgress: false });
                }
            })
        })
    }

    callBack(e) {
        if (e && e === 1) {
            this.setState({ msg: 'all' });
        } else if (e && e === 2) {
            this.setState({ msg: 'oneByOne' });
        }
    }

    render() {
        return (
            <>
                {this.state.displayProgress ? <Box style={{ width: '100%', height: '4px' }}><LinearProgress /></Box> : <Box style={{ height: '4px', width: '100%' }}></Box>}
                <Box style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', flexDirection: 'column', marginTop: 25 }}>
                    <RadioButton callBack={this.callBack} />

                    <Paper component="form" sx={{ p: '2px 4px', display: 'flex', alignItems: 'center', width: 400, marginTop: 5, marginBottom: 5 }} >
                        <InputBase sx={{ ml: 1, flex: 1 }} placeholder="Search Prompt" inputProps={{ 'aria-label': 'Search Prompt' }}
                            autoFocus
                            onChange={(e) => this.getSearchPrompt(e)}
                            onKeyDown={(e) => this.getSearchPrompt(e)} />
                        <IconButton type="button" sx={{ p: '10px' }} aria-label="search"
                            onClick={(e) => this.searchForSentiment(e)}>
                            <SearchIcon />
                        </IconButton>
                    </Paper>
                    {this.state.allSentiments && <DisplayTable allSentiments={this.state.allSentiments} msg={this.state.msg} />}
                </Box>
            </>
        );
    }
}