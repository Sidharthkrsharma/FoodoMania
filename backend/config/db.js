import dotenv from "dotenv";
import mongoose from "mongoose";

dotenv.config();

export const connectDB = async () => {
    try {
        await mongoose.connect(process.env.MONGODB_URI);
        console.log("Db connection established");
    } catch (error) {
        console.error("Db connection error:", error);
        process.exit(1); // Exit the process if unable to connect
    }
}

export default connectDB;

