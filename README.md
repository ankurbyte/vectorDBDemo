# VectorDB Demos

1. Multi-modal product image search for an e-Commerce store with 40,000+ products

# vectordb_uploader.py
## Overview
This Python module provides functionality for uploading fashion product data to VikingDB, a vector database service from BytePlus. It's designed to handle large datasets by implementing batch processing with retry logic and rate limiting protection.

## Features
- Batch uploading of data to VectorDB
- Random vector generation for embedding representation
- Support for image paths and text metadata
- Exponential backoff retry mechanism for handling rate limits
- Asynchronous processing for improved performance
## Requirements
- Python 3.7+
- volcengine SDK
- pandas
- asyncio

## image_search_app.py
### Overview
Based on product catalogue data uploaded in above step this application provides a user-friendly interface for searching e-Commerce fashion products using either text descriptions or image uploads. The application leverages VikingDB, a vector database service from BytePlus, to perform multimodal searches and find similar fashion products.

### Features
- Text-based Search : Users can enter text descriptions to find matching fashion products
- Image-based Search : Users can upload images to find visually similar fashion products
- Interactive UI : Clean interface with tabs for different search methods
- Detailed Results : Displays product information including name, color, and similarity score
### Technical Details
The application uses:

- Streamlit : For the web interface
- VikingDB : For vector similarity search
- BytePlus Object Storage (TOS) : For storing and retrieving product images
  
### How It Works
1. Text Search :
   
   - User enters a text description
   - The application converts this to a vector representation
   - VikingDB finds products with similar vector representations
   - Results are displayed with product details and images
2. Image Search :
   
   - User uploads an image
   - The image is encoded in base64 format
   - VikingDB finds visually similar products
   - Results are displayed with product details and images
     
3. Image Display :
   
   - Product images are stored in BytePlus Object Storage (TOS)
   - The application converts TOS paths to HTTP URLs for display
     
### Setup Requirements
- Python 3.6+
- Streamlit
- Pandas
- Pillow (PIL)
- BytePlus VikingDB SDK


2. Text Search Example

# VectorDB Text Data Uploader
## Overview
This script is designed to upload music data to VikingDB, a vector database service from BytePlus. It processes a CSV file containing music metadata and uploads it in batches to a specified collection.

## Features
- Asynchronous batch uploading to VikingDB
- Random vector generation for embedding representation
- Handles multiple data types (strings, integers, floats, booleans)
- Progress tracking with batch completion notifications
## Requirements
- Python 3.7+
- volcengine SDK
- pandas
- asyncio
## Configuration
Before using the script, you need to:

1. Set your BytePlus VikingDB credentials:
   
   - Replace "Your BytePlus AK" with your actual Access Key
   - Replace "Your BytePlus SK" with your actual Secret Key
     
2. Ensure your CSV file contains the following columns:
   
   - artist
   - song
   - duration_ms
   - explicit
   - year
   - popularity
   - danceability
   - energy
   - key
   - loudness
   - mode
   - speechiness
   - acousticness
   - instrumentalness
   - liveness
   - valence
   - tempo
   - genre
## Usage
1. Prepare your music dataset in CSV format
2. Update the file path in the script to point to your CSV file
3. Run the script: python UpsertData_Text.py


# app.py (Music Similarity Search Application)
## Overview
Based on music dataset uploaded in above step this Streamlit application provides a user-friendly interface for searching similar songs based on song names and energy levels. The application leverages VikingDB, a vector database service from BytePlus, to perform multimodal searches and find similar music tracks.

## Features
- Song Name Search : Find songs similar to a given song name
- Energy-Based Recommendations : Discover songs with similar energy levels
- Detailed Results : View comprehensive information about each song including artist, genre, year, popularity, and energy level
## Technical Details
The application uses:

- Streamlit : For the web interface
- VikingDB : For vector similarity search
- Multimodal Search : To find similar songs based on text input
## How It Works
1. Similar Songs Search :
   
   - User enters a song name
   - The application searches for similar songs using VikingDB's multimodal search
   - Results display song details including similarity scores
2. Energy-Based Recommendations :
   
   - The application extracts the energy level from the top search result
   - It then finds additional songs with similar energy levels
   - These are presented as "You May Also Like" recommendations
## Setup Requirements
- Python 3.6+
- Streamlit
- BytePlus VikingDB SDK
