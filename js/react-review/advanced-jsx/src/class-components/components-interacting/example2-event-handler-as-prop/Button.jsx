import React from 'react';

export class Button extends React.Component {
  render() {
    return (
      // Here it has special meaning
      <button onClick={this.props.onClick}>
        Click me!
      </button>
    );
  }
}