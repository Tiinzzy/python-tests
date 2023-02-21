import { Box } from '@mui/system';
import React from 'react';
import InitUrlProcess from './InitUrlProcess';

export default class Home extends React.Component {
    constructor(props) {
        super(props);
        this.state = {

        };

    }

    render() {
        return (
            <Box style={{ width: 600, justifyContent: 'center', margin: 'auto' }}>
                <InitUrlProcess />
            </Box>
        );
    }
};