import React, { Component } from 'react';
import axios from 'axios';

class App extends Component {
  constructor() {
    super();
    this.state = {
      data: {},
      postData: { 'name': 'Tina', 'age': 26 }
    };
  }

  componentDidMount() {
    // const fetchedToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

    let query = new FormData();
    query.append("post_data", this.state.postData);
    // query.append("csrfmiddlewaretoken", { fetchedToken })

    axios.get('http://localhost:8000/api/sample/')
      .then(response => {
        this.setState({ data: response.data });
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });

    axios.post('http://localhost:8000/api/post/', query)
      .then(response => {
        this.setState({ data: response.data });
      })
      .catch(error => {
        console.error('Error sending data:', error);
      });

    // try {
    //   const csrfTokenResponse = await axios.get('http://localhost:8000/csrf-token/');
    //   const csrfToken = csrfTokenResponse.data.csrfToken;
    //   await axios.post('http://localhost:8000/api/post/', this.state.postData, {
    //     headers: {
    //       'X-CSRFToken': csrfToken
    //     }
    //   })
    //     .then(response => {
    //       this.setState({ data: response.data });
    //     })
    //     .catch(error => {
    //       console.error('Error sending data:', error);
    //     });
    // } catch (error) {
    //   console.error('Error fetching CSRF token:', error);
    // }
  }

  render() {
    const { data } = this.state;

    return (
      <div>
        <h1>React App (Class Component)</h1>
        <p>Data from Django: {data.message}</p>
      </div>
    );
  }
}

export default App;
