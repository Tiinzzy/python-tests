import * as React from 'react';

import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormControl from '@mui/material/FormControl';
import FormLabel from '@mui/material/FormLabel';

export default class RadioButton extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            callBack: props.callBack
        }
    }

    selectedButton(e) {
        this.state.callBack(e);
    }

    render() {
        return (
            <>
                <FormControl>
                    <FormLabel id="demo-row-radio-buttons-group-label">Title Process </FormLabel>
                    <RadioGroup row >
                        <FormControlLabel value="All" control={<Radio />} label="All" onChange={() => this.selectedButton(1)} />
                        <FormControlLabel value="One by One" control={<Radio />} label="One by One" onChange={() => this.selectedButton(2)} />
                    </RadioGroup>
                </FormControl>
            </>

        );
    }
}