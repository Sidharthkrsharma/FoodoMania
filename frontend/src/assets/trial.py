import os

from bson import ObjectId
from gridfs import GridFS
from pymongo import MongoClient

# Replace with your MongoDB connection string
client = MongoClient("mongodb+srv://foodomania:7CUaeDQcUdquGUpQ@cluster0.fqkaivr.mongodb.net/foodomania")

# Access your database
db = client['foodomania']
collection = db['foods']

# Create a GridFS object
fs = GridFS(db)

# List of image file paths to be inserted
image_files = [
    r'D:\FoodoMania\frontend\src\assets\food_1.png',
    r'D:\FoodoMania\frontend\src\assets\food_2.png',
    r"D:\FoodoMania\frontend\src\assets\food_3.png",
    r"D:\FoodoMania\frontend\src\assets\food_4.png",
    r"D:\FoodoMania\frontend\src\assets\food_5.png",
    r"D:\FoodoMania\frontend\src\assets\food_6.png",
    r"D:\FoodoMania\frontend\src\assets\food_7.png",
    r"D:\FoodoMania\frontend\src\assets\food_8.png",
    r"D:\FoodoMania\frontend\src\assets\food_9.png",
    r"D:\FoodoMania\frontend\src\assets\food_10.png",
    r"D:\FoodoMania\frontend\src\assets\food_11.png",
    r"D:\FoodoMania\frontend\src\assets\food_12.png",
    r"D:\FoodoMania\frontend\src\assets\food_13.png",
    r"D:\FoodoMania\frontend\src\assets\food_14.png",
    r"D:\FoodoMania\frontend\src\assets\food_15.png",
    r"D:\FoodoMania\frontend\src\assets\food_16.png",
    r"D:\FoodoMania\frontend\src\assets\food_17.png",
    r"D:\FoodoMania\frontend\src\assets\food_18.png",
    r"D:\FoodoMania\frontend\src\assets\food_19.png",
    r"D:\FoodoMania\frontend\src\assets\food_20.png",
    r"D:\FoodoMania\frontend\src\assets\food_21.png",
    r"D:\FoodoMania\frontend\src\assets\food_22.png",
    r"D:\FoodoMania\frontend\src\assets\food_23.png",
    r"D:\FoodoMania\frontend\src\assets\food_24.png",
    r"D:\FoodoMania\frontend\src\assets\food_25.png",
    r"D:\FoodoMania\frontend\src\assets\food_26.png",
    r"D:\FoodoMania\frontend\src\assets\food_27.png",
    r"D:\FoodoMania\frontend\src\assets\food_28.png",
    r"D:\FoodoMania\frontend\src\assets\food_29.png",
    r"D:\FoodoMania\frontend\src\assets\food_30.png",
    r"D:\FoodoMania\frontend\src\assets\food_31.png",
    r"D:\FoodoMania\frontend\src\assets\food_32.png"
]

# Data to be inserted with image file names
data = [
    {"_id": ObjectId(), "name": "Greek salad", "image_filename": None, "price": 12, "description": "Food provides essential nutrients for overall health and well-being", "category": "Salad"},
    {"_id": ObjectId(), "name": "Veg salad", "image_filename": None, "price": 18, "description": "Food provides essential nutrients for overall health and well-being", "category": "Salad"},
    {"_id": ObjectId(), "name": "Clover Salad", "image_filename": None, "price": 16, "description": "Food provides essential nutrients for overall health and well-being", "category": "Salad"},
    {"_id": ObjectId(), "name": "Chicken Salad", "image_filename": None, "price": 24, "description": "Food provides essential nutrients for overall health and well-being", "category": "Salad"},
    {"_id": ObjectId(), "name": "Lasagna Rolls", "image_filename": None, "price": 14, "description": "Food provides essential nutrients for overall health and well-being", "category": "Rolls"},
    {"_id": ObjectId(), "name": "Peri Peri Rolls", "image_filename": None, "price": 12, "description": "Food provides essential nutrients for overall health and well-being", "category": "Rolls"},
    {"_id": ObjectId(), "name": "Chicken Rolls", "image_filename": None, "price": 20, "description": "Food provides essential nutrients for overall health and well-being", "category": "Rolls"},
    {"_id": ObjectId(), "name": "Veg Rolls", "image_filename": None, "price": 15, "description": "Food provides essential nutrients for overall health and well-being", "category": "Rolls"},
    {"_id": ObjectId(), "name": "Ripple Ice Cream", "image_filename": None, "price": 14, "description": "Food provides essential nutrients for overall health and well-being", "category": "Deserts"},
    {"_id": ObjectId(), "name": "Fruit Ice Cream", "image_filename": None, "price": 22, "description": "Food provides essential nutrients for overall health and well-being", "category": "Deserts"},
    {"_id": ObjectId(), "name": "Jar Ice Cream", "image_filename": None, "price": 10, "description": "Food provides essential nutrients for overall health and well-being", "category": "Deserts"},
    {"_id": ObjectId(), "name": "Vanilla Ice Cream", "image_filename": None, "price": 12, "description": "Food provides essential nutrients for overall health and well-being", "category": "Deserts"},
    {"_id": ObjectId(), "name": "Chicken Sandwich", "image_filename": None, "price": 12, "description": "Food provides essential nutrients for overall health and well-being", "category": "Sandwich"},
    {"_id": ObjectId(), "name": "Vegan Sandwich", "image_filename": None, "price": 18, "description": "Food provides essential nutrients for overall health and well-being", "category": "Sandwich"},
    {"_id": ObjectId(), "name": "Grilled Sandwich", "image_filename": None, "price": 16, "description": "Food provides essential nutrients for overall health and well-being", "category": "Sandwich"},
    {"_id": ObjectId(), "name": "Bread Sandwich", "image_filename": None, "price": 24, "description": "Food provides essential nutrients for overall health and well-being", "category": "Sandwich"},
    {"_id": ObjectId(), "name": "Cup Cake", "image_filename": None, "price": 14, "description": "Food provides essential nutrients for overall health and well-being", "category": "Cake"},
    {"_id": ObjectId(), "name": "Vegan Cake", "image_filename": None, "price": 12, "description": "Food provides essential nutrients for overall health and well-being", "category": "Cake"},
    {"_id": ObjectId(), "name": "Butterscotch Cake", "image_filename": None, "price": 20, "description": "Food provides essential nutrients for overall health and well-being", "category": "Cake"},
    {"_id": ObjectId(), "name": "Sliced Cake", "image_filename": None, "price": 15, "description": "Food provides essential nutrients for overall health and well-being", "category": "Cake"},
    {"_id": ObjectId(), "name": "Garlic Mushroom", "image_filename": None, "price": 14, "description": "Food provides essential nutrients for overall health and well-being", "category": "Pure Veg"},
    {"_id": ObjectId(), "name": "Fried Cauliflower", "image_filename": None, "price": 22, "description": "Food provides essential nutrients for overall health and well-being", "category": "Pure Veg"},
    {"_id": ObjectId(), "name": "Mix Veg Pulao", "image_filename": None, "price": 10, "description": "Food provides essential nutrients for overall health and well-being", "category": "Pure Veg"},
    {"_id": ObjectId(), "name": "Rice Zucchini", "image_filename": None, "price": 12, "description": "Food provides essential nutrients for overall health and well-being", "category": "Pure Veg"},
    {"_id": ObjectId(), "name": "Cheese Pasta", "image_filename": None, "price": 12, "description": "Food provides essential nutrients for overall health and well-being", "category": "Pasta"},
    {"_id": ObjectId(), "name": "Tomato Pasta", "image_filename": None, "price": 18, "description": "Food provides essential nutrients for overall health and well-being", "category": "Pasta"},
    {"_id": ObjectId(), "name": "Creamy Pasta", "image_filename": None, "price": 16, "description": "Food provides essential nutrients for overall health and well-being", "category": "Pasta"},
    {"_id": ObjectId(), "name": "Chicken Pasta", "image_filename": None, "price": 24, "description": "Food provides essential nutrients for overall health and well-being", "category": "Pasta"},
    {"_id": ObjectId(), "name": "Buttter Noodles", "image_filename": None, "price": 14, "description": "Food provides essential nutrients for overall health and well-being", "category": "Noodles"},
    {"_id": ObjectId(), "name": "Veg Noodles", "image_filename": None, "price": 12, "description": "Food provides essential nutrients for overall health and well-being", "category": "Noodles"},
    {"_id": ObjectId(), "name": "Somen Noodles", "image_filename": None, "price": 20, "description": "Food provides essential nutrients for overall health and well-being", "category": "Noodles"},
    {"_id": ObjectId(), "name": "Cooked Noodles", "image_filename": None, "price": 15, "description": "Food provides essential nutrients for overall health and well-being", "category": "Noodles"}
]

# Check if the number of images matches the number of data entries
if len(image_files) != len(data):
    raise ValueError("The number of images and data entries must be the same.")

# Store images in GridFS and update data with image filenames
for i, image_path in enumerate(image_files):
    try:
        with open(image_path, 'rb') as image_file:
            filename = os.path.basename(image_path)
            fs.put(image_file, filename=filename)
            data[i]['image_filename'] = filename
    except Exception as e:
        print(f"Error storing image {image_path}: {e}")

# Insert data into the collection
try:
    collection.insert_many(data)
    print("Data and images inserted successfully")
except Exception as e:
    print(f"Error inserting data into the collection: {e}")

# Example: Retrieve and save an image from GridFS using filename
try:
    filename = data[0]['image_filename']  # Change as needed
    stored_image = fs.find_one({"filename": filename})
    if stored_image:
        output_path = 'retrieved_image.png'
        with open(output_path, 'wb') as f:
            f.write(stored_image.read())
        print(f"Image retrieved and saved as '{output_path}'")
    else:
        print(f"Image with filename '{filename}' not found in GridFS")
except Exception as e:
    print(f"Error retrieving or saving the image: {e}")
