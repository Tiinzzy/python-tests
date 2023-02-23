import React from 'react';

import Box from '@mui/system/Box';

import InitProcess from './InitProcess';

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
                <InitProcess />
            </Box>
        );
    }
};