import React from 'react';

import List from '@mui/material/List';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemText from '@mui/material/ListItemText';
import Collapse from '@mui/material/Collapse';
import ExpandLess from '@mui/icons-material/ExpandLess';
import ExpandMore from '@mui/icons-material/ExpandMore';
import Divider from '@mui/material/Divider';

import BackEndConnection from './BackEndConnection';
import { shared } from './helper';

import './style.css';

const backend = BackEndConnection.INSTANCE();

const COMMON_WORDS_AMOUNT = [5, 10, 15, 20]

export default class CommonWords extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            open: false,
            value: 'Common Words',
            data: null
        };
    }

    handleOpen() {
        this.setState({ open: true });
    }

    sendCommonWordValue(e) {
        this.setState({ open: false, value: e + ' Common Words' });
        backend.get_common_words(e, (data) => {
            let that = this;
            that.setState({ data: data }, () => {
                shared.callTextTokens({ action: 'get-common-words', data: that.state.data })
            })
        })
    }

    render() {
        return (
            <>
                <List sx={{ width: 210, bgcolor: 'background.paper', border: 'solid 1px #eaeaea', marginTop: 1, borderRadius: 4 }} component="nav">
                    <ListItemButton onClick={() => this.handleOpen()}>
                        <ListItemText primary={this.state.value} />
                        {this.state.open ? <ExpandLess /> : <ExpandMore />}
                    </ListItemButton>
                    <Collapse in={this.state.open} timeout="auto" unmountOnExit>
                        <List component="div" disablePadding>
                            {COMMON_WORDS_AMOUNT.map((e, i) => (
                                <ListItemButton key={i} onClick={() => this.sendCommonWordValue(e)}>
                                    <ListItemText primary={e} />
                                    <Divider />
                                </ListItemButton>
                            ))}
                        </List>
                    </Collapse>
                </List>
            </>
        );
    }
};