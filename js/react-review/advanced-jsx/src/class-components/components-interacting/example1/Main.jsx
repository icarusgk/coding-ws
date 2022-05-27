import React from "react";
import { Greeting } from "./Greeting";

export class Main extends React.Component {
  render() {
    return (
      <div>
        <p>The following is a greeting</p>
        <Greeting name="Icarus" />
      </div>
    )
  }
}