import { Box } from '@mui/system';
import React from 'react';
import InitUrlProcess from './InitUrlProcess';

import './style.css';

export default class Home extends React.Component {
    constructor(props) {
        super(props);
        this.state = {

        };

    }

    render() {
        return (
            <Box className="MainHomeBox">
                <InitUrlProcess />
            </Box>
        );
    }
};