import { Box } from '@mui/system';
import React from 'react';
import Url from './Url';

export default class Home extends React.Component {
    constructor(props) {
        super(props);
        this.state = {

        };

    }

    render() {
        return (
            <Box style={{ width: 600, justifyContent: 'center', margin: 'auto' }}>
                <Url />
            </Box>
        );
    }
};