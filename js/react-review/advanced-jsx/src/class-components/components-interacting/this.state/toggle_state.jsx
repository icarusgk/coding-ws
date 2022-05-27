import React from 'react';
import './toggle_state_style.css';

const green = '#39D1B4';
const yellow = '#FFD712';

export class Toggle extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      color: green
    }
    this.changeColor = this.changeColor.bind(this);
  }

  changeColor() {
    this.setState({ color: this.state.color === green ? yellow : green });
  }

  render() {
    return (
      <div style={{ background: this.state.color }}>
        <h1>
          Change my color
        </h1>
        <button onClick={this.changeColor}>
          Change color
        </button>
      </div>
    );
  }
}
