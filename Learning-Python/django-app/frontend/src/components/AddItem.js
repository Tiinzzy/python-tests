import React, { Component } from 'react';
import axios from 'axios';

class AddItem extends Component {
  constructor(props) {
    super(props);
    this.state = {
      name: '',
    };
  }

  handleChange = (e) => {
    this.setState({ name: e.target.value });
  };

  handleSubmit = () => {
    const { name } = this.state;
    axios
      .post('/api/create-item/', { name })
      .then((response) => {
        console.log('Item added:', response.data);
        this.setState({ name: '' });
      })
      .catch((error) => {
        console.error('Error adding item:', error);
      });
  };

  render() {
    const { name } = this.state;

    return (
      <div>
        <h2>Add Item</h2>
        <input
          type="text"
          placeholder="Item Name"
          value={name}
          onChange={this.handleChange}
        />
        <button onClick={this.handleSubmit}>Add</button>
      </div>
    );
  }
}

export default AddItem;
