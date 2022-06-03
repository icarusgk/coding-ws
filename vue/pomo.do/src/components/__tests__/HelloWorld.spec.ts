import { describe, it, expect } from "vitest";

import { mount } from "@vue/test-utils";
import HelloWorld from "../HelloWorld.vue";

describe("HelloWorld", () => {
  it("renders properly", () => {
    // Mounts the component and passes a prop named msg
    const wrapper = mount(HelloWorld, { props: { msg: "Hello Vitest" } });
    // Assert the condition
    expect(wrapper.text()).toContain("Hello Vitest");
  });
});
