import React from 'react';
import ReactDOM from 'react-dom';

class App extends React.Component {
  // constructor method begins here:
  constructor(props) {
    // Pass the props to React.Component
    super(props);
    this.state = {
      title: 'Best App'
    }
  }

  render() {
    return (
      <h1>
        {this.state.title}
      </h1>
    );
  }
}