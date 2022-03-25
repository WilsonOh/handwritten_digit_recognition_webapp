import express from "express";
import fetch from "node-fetch";

const app = express();

app.use(express.json());
app.use("/", express.static("./static"));

app.post("/submit", async (req, res) => {
  try {
    const data = req.body;
    let predictions = await fetch(
      "http://13.215.15.247:8501/v1/models/digit_recognition/versions/0:predict",
      {
        method: "post",
        body: JSON.stringify({ instances: data }),
        headers: { "Content-Type": "application/json" },
      }
    );
    predictions = await predictions.json();
    console.log(predictions);
    const guess = argmax(predictions.predictions[0]);
    res.send(guess.toString());
  } catch (err) {
    console.log(err);
  }
});

function argmax(predictions) {
  let max = predictions[0];
  let max_id = 0;
  predictions.forEach((val, idx) => {
    if (val > max) {
      max = val;
      max_id = idx;
    }
  });
  return max_id;
}

app.listen(3000);
