import React from "react";

import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import InputBase from '@mui/material/InputBase';
import IconButton from '@mui/material/IconButton';
import SearchIcon from '@mui/icons-material/Search';
import Typography from "@mui/material/Typography";


import BackEndConnection from './BackEndConnection';
import Table from "./Table";
import RadioButton from "./RadioButton";

const backend = BackEndConnection.INSTANCE();

export default class UserInput extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            searchItem: '',
        }
        this.callBack = this.callBack.bind(this);
    }

    getSearchPrompt(e) {
        this.setState({ searchItem: e.target.value });
        if (e.keyCode === 13) {
            e.preventDefault();
        }
        let key = e.code || "";
        let isEnter = key.toLowerCase().indexOf('enter') >= 0;
        if (isEnter) {
            this.searchForSentiment();
        }
    }

    searchForSentiment() {
        this.callBack(1);
    }

    callBack(e) {
        if (e && e === 1) {
            let query = { prompt: this.state.searchItem, msg: 'all' };
            backend.send_search_prompt(query, (data) => {
                if (data) {
                    this.setState({ allSentiments: data, titles: data.array_of_titles });
                };
            })
        } else if (e && e === 2) {
            let query = { prompt: this.state.searchItem, msg: 'oneByOne' };
            backend.send_search_prompt(query, (data) => {
                if (data) {
                    this.setState({ allSentiments: data, titles: data.array_of_titles });
                };
            })
        }
    }

    render() {
        return (
            <>
                <Box style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', flexDirection: 'column' }}>
                    <Paper component="form" sx={{ p: '2px 4px', display: 'flex', alignItems: 'center', width: 400, marginTop: 5, marginBottom: 5 }} >
                        <InputBase sx={{ ml: 1, flex: 1 }} placeholder="Search Prompt" inputProps={{ 'aria-label': 'Search Prompt' }}
                            onChange={(e) => this.getSearchPrompt(e)}
                            onKeyDown={(e) => this.getSearchPrompt(e)} />
                        <IconButton type="button" sx={{ p: '10px' }} aria-label="search"
                            onClick={(e) => this.searchForSentiment(e)}>
                            <SearchIcon />
                        </IconButton>
                    </Paper>
                    <RadioButton callBack={this.callBack} />
                    {this.state.allSentiments && <Table allSentiments={this.state.allSentiments} />}
                    <Box style={{ border: 'solid 1px #eaeaea', borderRadius: 4, width: '40%', padding: 10, height: '40%', marginTop: 15 }}>
                        {this.state.titles && this.state.titles.map((e, i) => (
                            <Typography key={i} variant="body1">
                                {i + 1}: {e}
                            </Typography>
                        ))}
                    </Box>
                </Box >
            </>

        );
    }
}