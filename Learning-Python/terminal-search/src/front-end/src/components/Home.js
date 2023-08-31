import React from "react";

import Box from '@mui/material/Box';
import Typography from "@mui/material/Typography";

import UserInput from "./UserInput";

export default class Home extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
        }
    }

    render() {
        return (
            <>
                <Box style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', marginTop: 20, borderBottom: 'solid 2px #41424C' }}>
                    <Typography mt={1} mb={1.5} variant="body1" style={{ color: '#333333' }}>
                        News Title Sentiment Predictor
                    </Typography>
                </Box>

                <UserInput />
            </>

        );
    }
}