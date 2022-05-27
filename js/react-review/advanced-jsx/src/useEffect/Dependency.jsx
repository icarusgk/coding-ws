import { useState, useEffect } from "react";

export const Dependency = () => {
  const [count, setCount] = useState(0);

  useEffect(() => {
    // The document title is set to when the page first renders
    // If we specify the count as a dependency then, each time
    // count changes, so will the title
    document.title = `You've clicked ${count} times`;
  }, [count]);

  return (
    <div>
      <h1>Click below!</h1>
      <button onClick={() => setCount((prev) => prev + 1)}>Click!</button>
    </div>
  );
};
