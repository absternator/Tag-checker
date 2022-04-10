import React, { useState } from "react";

function App() {
  const [stringToCheck, setStringToCheck] = useState("");
  const [checkedStringMessage, setCheckedStringMessage] = useState("");

  const handleSubmit = async (event: React.SyntheticEvent) => {
    event.preventDefault();

    try {
      let response = await fetch(
        "https://k14k10veo5.execute-api.us-east-1.amazonaws.com/",
        { method: "POST", body: JSON.stringify({ stringToCheck }) }
      );
      let message = await response.json();
      setCheckedStringMessage(message.checkedMessage);
    } catch (error) {
      console.error(error);
      setCheckedStringMessage(
        `Error occured! Expected checked message, please try again later`
      );
    }

    // reset input
    setStringToCheck("");
  };
  return (
    <>
      <div
        style={{
          display: "flex",
          alignItems: "center",
          height: "900px",
          justifyContent: "center",
        }}
      >
        <div>
          <form onSubmit={handleSubmit}>
            <label>Input tag string: </label>
            <input
              type="text"
              name="inputText"
              value={stringToCheck}
              onChange={(e) => setStringToCheck(e.target.value)}
            />
            <input type="submit" value="submit" />
          </form>
          <div style={{ marginTop: ".5rem" }}>
            Checked String Result:
            <strong
              style={{
                color: checkedStringMessage?.includes("Expected")
                  ? "red"
                  : "green",
              }}
            >
              {" "}
              {checkedStringMessage}
            </strong>
          </div>
        </div>
      </div>
    </>
  );
}

export default App;
