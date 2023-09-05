import React from "react";

import SentimentAllTable from "./SentimentAllTable";
import SentimentOneByOneTable from "./SentimentOneByOneTable";

export default class Table extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            allSentiments: props.allSentiments,
            msg: props.msg
        }
    }

    render() {
        return (
            <>
                {this.props.msg === 'all' ? <SentimentAllTable allSentiments={this.props.allSentiments} />
                    : <SentimentOneByOneTable allSentiments={this.props.allSentiments} />}
            </>
        );
    }
}