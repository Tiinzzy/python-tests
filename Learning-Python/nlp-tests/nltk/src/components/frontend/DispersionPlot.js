import React from 'react';

import Box from '@mui/system/Box';
import DialogContent from '@mui/material/DialogContent';
import DialogTitle from '@mui/material/DialogTitle';
import Button from '@mui/material/Button';
import DialogActions from '@mui/material/DialogActions';

import './style.css';

const SELECTED_WORDS = [];

export default class DispersionPlot extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            allWords: props.allWords,
            close: props.close
        };
    }

    componentDidMount() {
        let uniqWOrds = [...new Set(this.state.allWords)];
        this.setState({ uniqWOrds })
    }

    wordSelected(e) {
        SELECTED_WORDS.push(e.target.innerText);
    }

    submitWords() {
        this.state.close();
        console.log(SELECTED_WORDS);
    }

    render() {
        return (
            <Box>
                <DialogTitle>
                    {"Select the words you would like to compare the frequency across the text:"}
                </DialogTitle>
                <DialogContent>
                    <div className='EachWordDiv'>
                        {this.state.uniqWOrds && this.state.uniqWOrds.map((e, i) => (
                            <div key={i} className="EachWord" onClick={(e) => this.wordSelected(e)}>{e}</div>
                        ))}
                    </div>
                </DialogContent>
                <DialogActions>
                    <Button onClick={() => this.submitWords()}>Submit</Button>
                </DialogActions>
            </Box>
        );
    }
};