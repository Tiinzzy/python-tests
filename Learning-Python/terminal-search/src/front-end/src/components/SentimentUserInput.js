import React from "react";

import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import InputBase from '@mui/material/InputBase';
import IconButton from '@mui/material/IconButton';
import SearchIcon from '@mui/icons-material/Search';
import Typography from "@mui/material/Typography";


import BackEndConnection from './BackEndConnection';
import DisplayTable from "./DisplayTable";
import RadioButton from "./RadioButton";

const backend = BackEndConnection.INSTANCE();

export default class SentimentUserInput extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            searchItem: '',
            displaySearchBar: false,
            msg: ''
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
            backend.send_search_prompt(query, (data) => {
                if (data) {
                    this.setState({ allSentiments: data, titles: data.array_of_titles });
                };
            })
        }
    }
    searchForSentiment() {
        let query = { prompt: this.state.searchItem, msg: this.state.msg };
        backend.send_search_prompt(query, (data) => {
            if (data) {
                this.setState({ allSentiments: data, titles: data.array_of_titles });
            };
        })
    }

    callBack(e) {
        if (e && e === 1) {
            this.setState({ msg: 'all', displaySearchBar: true });
        } else if (e && e === 2) {
            this.setState({ msg: 'oneByOne', displaySearchBar: true });
        }
    }

    render() {
        return (
            <Box style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', flexDirection: 'column', marginTop: 25 }}>
                <RadioButton callBack={this.callBack} />
                {this.state.displaySearchBar &&
                    <Paper component="form" sx={{ p: '2px 4px', display: 'flex', alignItems: 'center', width: 400, marginTop: 5, marginBottom: 5 }} >
                        <InputBase sx={{ ml: 1, flex: 1 }} placeholder="Search Prompt" inputProps={{ 'aria-label': 'Search Prompt' }}
                            onChange={(e) => this.getSearchPrompt(e)}
                            onKeyDown={(e) => this.getSearchPrompt(e)} />
                        <IconButton type="button" sx={{ p: '10px' }} aria-label="search"
                            onClick={(e) => this.searchForSentiment(e)}>
                            <SearchIcon />
                        </IconButton>
                    </Paper>}
                {this.state.allSentiments && <DisplayTable allSentiments={this.state.allSentiments} msg={this.state.msg} />}
            </Box>

        );
    }
}