import React, { Component } from 'react';
import axios from 'axios';

class ItemList extends Component {
  constructor(props) {
    super(props);
    this.state = {
      items: [],
    };
  }

  componentDidMount() {
    axios
      .get('/api/get-items/')
      .then((response) => {
        this.setState({ items: response.data });
      })
      .catch((error) => {
        console.error('Error fetching items:', error);
      });
  }

  render() {
    const { items } = this.state;

    return (
      <div>
        <h2>Items</h2>
        <ul>
          {items.map((item) => (
            <li key={item.id}>{item.name}</li>
          ))}
        </ul>
      </div>
    );
  }
}

export default ItemList;
