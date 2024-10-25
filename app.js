import express from 'express';
import bodyParser from 'body-parser';

const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.post('/data', (req, res) => {
  const humidity = req.body.humidity;
  console.log('Received humidity data:', humidity);

  // Process humidity data as needed

  res.json({ success: true, message: 'Humidity data received successfully.' });
});

app.use((req, res) => {
  res.status(404).json({ success: false, message: 'Not Found' });
});

app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ success: false, message: 'Internal Server Error' });
});

app.listen(port, () => {
  console.log(`Server listening at http://172.20.10.2:${port}`);
});
