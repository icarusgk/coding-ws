import React from "react"

export class Greeting extends React.Component {
  render() {
    return (
      <h1>Hello there! {this.props.name}</h1>
    )
  }
}