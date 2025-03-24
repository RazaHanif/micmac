require('dotenv').config();
require('express-async-errors');
const express = require('express');
const app = express();

// connectDB
const connectDB = require('./db/connect')

// Routers
const authRoute = require('./routes/auth')
const jobRoute = require('./routes/jobs')

// error handler
const notFoundMiddleware = require('./middleware/not-found');
const errorHandlerMiddleware = require('./middleware/error-handler');

// Middleware
const authMiddleware = require('./middleware/authentication')


app.use(express.json());
// extra packages

// Routes
app.use('/api/v1/jobs', authMiddleware, jobRoute)
app.use('/api/v1/auth', authRoute)

app.use(notFoundMiddleware);
app.use(errorHandlerMiddleware);

const port = process.env.PORT || 3000;

const start = async () => {
  try {
    await connectDB(process.env.MONGO_URI)
    app.listen(port, () =>
      console.log(`Live Server:${port}...`)
    );
  } catch (error) {
    console.log(error);
  }
};

start();
