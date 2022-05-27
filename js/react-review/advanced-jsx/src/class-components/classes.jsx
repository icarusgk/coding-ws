import React from 'react';

// React component is a js class, in order to create our own component
// we must subclass it

class MyComponent extends React.Component {
  render() {
    return (
      <div>
        <h1>Hello world!</h1>
        <p>Hi there!</p>
      </div>
    )
  }
}

export default MyComponent;