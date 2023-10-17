import React, { Component } from "react";

import ActualApp from "./components/ActualApp";
import NewApp from "./components/NewApp";


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {

    };
  }
  render() {
    return (
      <>
        <ActualApp />
      </>
    );
  }
}

export default App;