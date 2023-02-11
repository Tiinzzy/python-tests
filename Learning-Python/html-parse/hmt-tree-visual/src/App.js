import React from 'react';
import Graph from './components/Graph';

export default class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {}
  }

  render() {
    return (
      <Graph />
    );
  }
}
