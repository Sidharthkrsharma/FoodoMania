import cors from "cors";
import 'dotenv/config.js';
import express from "express";
import { connectDB } from "./config/db.js";
import cartRouter from "./routes/cartRoute.js";
import foodRouter from "./routes/foodRoute.js";
import orderRouter from "./routes/orderRoute.js";
import userRouter from "./routes/userRoute.js";

// app config
const app = express();
const port =  4000 || process.env.PORT;

// middleware
app.use(express.json());
app.use(cors());


// db config
connectDB();

// api endpoint
app.use("/api/food", foodRouter)
app.use("/images", express.static('uploads'))
app.use("/api/user", userRouter)
app.use("/api/cart", cartRouter)
app.use("/api/order", orderRouter)

// routes
app.get("/",(req,res)=>{
  res.send("API is running...");
});

app.use((req, res, next) => {
  res.status(404).send("404 Not Found");
});

app.listen(port, (err) => {
  if (err) {
      console.error('Error starting server:', err);
      process.exit(1); // Exit with failure code
  }
  console.log(`Server is running on port ${port}`);
});