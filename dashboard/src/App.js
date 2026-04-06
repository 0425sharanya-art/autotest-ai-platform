import React, { useState } from "react";
import axios from "axios";

function App() {

  const [result, setResult] = useState("");

  const runTests = async () => {
    const res = await axios.post("http://localhost:8000/run-tests");
    setResult(JSON.stringify(res.data, null, 2));
  };

  return (
    <div style={{padding:"40px"}}>
      <h1>AutoTest AI Dashboard</h1>

      <button onClick={runTests}>
        Run Tests
      </button>

      <pre>{result}</pre>
    </div>
  );
}

export default App;
