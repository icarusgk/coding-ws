import { defineStore } from "pinia";

// A counter store
// A store is just a object with functions within!
export const useCounterStore = defineStore({
  id: "counter",
  // Store state
  state: () => ({
    counter: 0,
  }),
  // Store getters
  getters: {
    doubleCount: (state) => state.counter * 2,
  },
  // Store actions
  actions: {
    increment() {
      // Increments the counter
      this.counter++;
    },
  },
});
