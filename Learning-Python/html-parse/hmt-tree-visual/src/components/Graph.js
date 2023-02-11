import React from 'react';

import { Graphviz } from "graphviz-react";
import BackEndConnection from './BackEndConnection';
const backend = BackEndConnection.INSTANCE();


export default class Graph extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            graphString: null
        }
    }

    componentDidMount() {
        backend.get_data_from_backaned(this, this.myCallBack);
    }

    myCallBack = (componenet, data) => {
        let graphString = data.map(e => `"${e.from_title}"->"${e.to_title}";`).join('');
        graphString = `digraph G { ${graphString} }`;
        console.log(graphString);
        componenet.setState({ graphString: graphString });
    }

    render() {
        return (
            <>
                {this.state.graphString !== null && <Graphviz
                    dot={this.state.graphString}
                    options={{ zoom: true, width: '100%', height: '100%', useWorker: false }}
                />}
            </>
        );
    }
}