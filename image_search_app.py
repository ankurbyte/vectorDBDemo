import streamlit as st
import base64
from io import BytesIO
import pandas as pd
from PIL import Image
import os
from volcengine.viking_db import *

# Initialize VikingDB service
vikingdb_service = VikingDBService("api-vikingdb.mlp.ap-mya.byteplus.com", "ap-southeast-1")
vikingdb_service.set_ak("Your BytePlus AK")
vikingdb_service.set_sk("Your BytePlus SK")

# Get the index (do this once during initialization)
index = vikingdb_service.get_index("Ankur_Product_Image_Collection", "Ankur_Product_Image_Index")

def convert_tos_to_http_url(tos_path):
    """Convert TOS path to HTTP URL"""
    if not tos_path or not isinstance(tos_path, str):
        return None
    
    if tos_path.startswith('tos://'):
        # Extract the bucket and object key from the TOS path
        # Format: tos://{bucket}/{object_key}
        parts = tos_path.replace('tos://', '').split('/', 1)
        if len(parts) == 2:
            bucket = parts[0]
            object_key = parts[1]
            # Construct the HTTP URL
            return f"https://{bucket}.tos-ap-southeast-1.bytepluses.com/{object_key}"
    
    return tos_path  # Return original if not a TOS path or already HTTP

def search_with_text(text_query):
    """Search for similar images using text query"""
    try:
        results = index.search_with_multi_modal(
            text=text_query,
            limit=10,  # Get top 10 similar images
            need_instruction=False,
            output_fields=["productDisplayName", "baseColour", "image"]
        )
        return results
    except Exception as e:
        st.error(f"Error searching with text: {str(e)}")
        return []

def search_with_image(image_file):
    """Search for similar images using uploaded image"""
    try:
        # Read the image file
        image_bytes = image_file.getvalue()
        
        # Convert to base64 for API
        image_base64 = base64.b64encode(image_bytes).decode('utf-8')
        
        # Search using the image - add the required "base64://" prefix
        results = index.search_with_multi_modal(
            image=f"base64://{image_base64}",  # Add the required prefix
            limit=10,  # Get top 10 similar images
            need_instruction=False,
            output_fields=["productDisplayName", "baseColour", "image"]
        )
        return results
    except Exception as e:
        st.error(f"Error searching with image: {str(e)}")
        return []

def display_results(results):
    """Display search results in a grid layout"""
    if not results:
        st.warning("No similar images found.")
        return
    
    # Create rows with 3 images each
    for i in range(0, len(results), 3):
        cols = st.columns(3)
        
        # Add images to each column in the current row
        for j in range(3):
            if i + j < len(results):
                result = results[i + j]
                fields = result.fields
                score = result.score
                
                with cols[j]:
                    # Display product information
                    st.markdown(f"**{fields.get('productDisplayName', 'Unknown Product')}**")
                    st.markdown(f"Color: {fields.get('baseColour', 'Unknown')}")
                    st.markdown(f"Similarity: {score:.2f}")
                    
                    # Display image if available
                    if 'image' in fields and fields['image']:
                        try:
                            # Convert TOS path to HTTP URL
                            image_url = convert_tos_to_http_url(fields['image'])
                            # Use use_container_width instead of use_column_width
                            st.image(image_url, use_container_width=True)
                        except Exception as e:
                            st.error(f"Error displaying image: {str(e)}")
                    else:
                        st.info("No image available")
                    
                    st.markdown("---")

# Streamlit UI
st.title("Fashion Image Search")
st.write("Search for similar fashion products using text or upload an image")

# Create tabs for text search and image upload
tab1, tab2 = st.tabs(["Text Search", "Image Upload"])

with tab1:
    # Text search interface
    text_query = st.text_input("Enter search text:")
    
    if text_query:
        with st.spinner('Searching for similar images...'):
            results = search_with_text(text_query)
            display_results(results)

with tab2:
    # Image upload interface
    uploaded_file = st.file_uploader("Upload an image to find similar products:", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        # Display the uploaded image
        # Use use_container_width instead of use_column_width
        st.image(uploaded_file, caption="Uploaded Image", width=300)
        
        # Search button
        if st.button("Search for Similar Images"):
            with st.spinner('Searching for similar images...'):
                results = search_with_image(uploaded_file)
                display_results(results)