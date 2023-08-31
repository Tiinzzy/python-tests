import React from "react";

import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import InputBase from '@mui/material/InputBase';
import IconButton from '@mui/material/IconButton';
import SearchIcon from '@mui/icons-material/Search';
import Typography from "@mui/material/Typography";


import BackEndConnection from './BackEndConnection';

const backend = BackEndConnection.INSTANCE();

export default class UserInput extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            searchItem: '',
        }
    }

    getSearchPrompt(e) {
        this.setState({ searchItem: e.target.value });
        console.log(e.keyCode)
        if (e.keyCode === 13) {
            e.preventDefault();
        }
        let key = e.code || "";
        let isEnter = key.toLowerCase().indexOf('enter') >= 0;
        if (isEnter) {
            this.searchForSentiment();
        }
    }

    searchForSentiment(e) {
        let query = { prompt: this.state.searchItem }
        backend.send_search_prompt(query, (data) => {
            if (data) {
                console.log(data);
                this.setState({ searchItem: '', titles: data.array_of_titles, promptSentiment: data.prompt_sentiment, titlesSentiment: data.titles_sentiment });
            };
        })
        console.log(this.state.searchItem)
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
                    <Box style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', flexDirection: 'row' }}>
                        {this.state.promptSentiment && <span style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', flexDirection: 'row' }}>
                            <Typography fontWeight="600" mr={1}> Search Prompt Sentiment: </Typography>
                            <Typography mr={5}>{this.state.promptSentiment}</Typography>
                        </span>}
                        {this.state.titlesSentiment && <span style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', flexDirection: 'row' }}>
                            <Typography fontWeight="600" mr={1}>All Titles Sentiment: </Typography>
                            <Typography>{this.state.titlesSentiment}</Typography>
                        </span>}
                    </Box>
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