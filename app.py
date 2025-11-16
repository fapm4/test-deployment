import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Tech Product Comparison",
    page_icon="💻",
    layout="wide"
)

# Sample tech products data
@st.cache_data
def load_products():
    products = [
        {
            "name": "iPhone 15 Pro",
            "category": "Smartphone",
            "brand": "Apple",
            "price": 999,
            "rating": 4.7,
            "screen_size": "6.1 inches",
            "storage": "256GB",
            "ram": "8GB",
            "battery": "3274 mAh",
            "release_year": 2023
        },
        {
            "name": "Samsung Galaxy S24",
            "category": "Smartphone",
            "brand": "Samsung",
            "price": 899,
            "rating": 4.6,
            "screen_size": "6.2 inches",
            "storage": "256GB",
            "ram": "8GB",
            "battery": "4000 mAh",
            "release_year": 2024
        },
        {
            "name": "Google Pixel 8 Pro",
            "category": "Smartphone",
            "brand": "Google",
            "price": 899,
            "rating": 4.5,
            "screen_size": "6.7 inches",
            "storage": "128GB",
            "ram": "12GB",
            "battery": "5050 mAh",
            "release_year": 2023
        },
        {
            "name": "MacBook Pro 14\"",
            "category": "Laptop",
            "brand": "Apple",
            "price": 1999,
            "rating": 4.8,
            "screen_size": "14 inches",
            "storage": "512GB SSD",
            "ram": "16GB",
            "battery": "70 Wh",
            "release_year": 2023
        },
        {
            "name": "Dell XPS 15",
            "category": "Laptop",
            "brand": "Dell",
            "price": 1799,
            "rating": 4.6,
            "screen_size": "15.6 inches",
            "storage": "512GB SSD",
            "ram": "16GB",
            "battery": "86 Wh",
            "release_year": 2023
        },
        {
            "name": "ThinkPad X1 Carbon",
            "category": "Laptop",
            "brand": "Lenovo",
            "price": 1599,
            "rating": 4.7,
            "screen_size": "14 inches",
            "storage": "512GB SSD",
            "ram": "16GB",
            "battery": "57 Wh",
            "release_year": 2023
        },
        {
            "name": "iPad Pro 12.9\"",
            "category": "Tablet",
            "brand": "Apple",
            "price": 1099,
            "rating": 4.8,
            "screen_size": "12.9 inches",
            "storage": "256GB",
            "ram": "8GB",
            "battery": "40.88 Wh",
            "release_year": 2023
        },
        {
            "name": "Samsung Galaxy Tab S9",
            "category": "Tablet",
            "brand": "Samsung",
            "price": 799,
            "rating": 4.5,
            "screen_size": "11 inches",
            "storage": "128GB",
            "ram": "8GB",
            "battery": "8400 mAh",
            "release_year": 2023
        }
    ]
    return pd.DataFrame(products)

# Main app
def main():
    st.title("💻 Tech Product Comparison Tool")
    st.markdown("Compare specifications, prices, and ratings of popular tech products")
    
    # Load data
    df = load_products()
    
    # Sidebar filters
    st.sidebar.header("Filters")
    
    # Category filter
    categories = ["All"] + sorted(df["category"].unique().tolist())
    selected_category = st.sidebar.selectbox("Category", categories)
    
    # Brand filter
    brands = ["All"] + sorted(df["brand"].unique().tolist())
    selected_brand = st.sidebar.selectbox("Brand", brands)
    
    # Price range filter
    min_price, max_price = int(df["price"].min()), int(df["price"].max())
    price_range = st.sidebar.slider(
        "Price Range ($)",
        min_price,
        max_price,
        (min_price, max_price)
    )
    
    # Rating filter
    min_rating = st.sidebar.slider("Minimum Rating", 0.0, 5.0, 0.0, 0.1)
    
    # Apply filters
    filtered_df = df.copy()
    if selected_category != "All":
        filtered_df = filtered_df[filtered_df["category"] == selected_category]
    if selected_brand != "All":
        filtered_df = filtered_df[filtered_df["brand"] == selected_brand]
    filtered_df = filtered_df[
        (filtered_df["price"] >= price_range[0]) &
        (filtered_df["price"] <= price_range[1]) &
        (filtered_df["rating"] >= min_rating)
    ]
    
    # Sorting
    st.sidebar.header("Sorting")
    sort_by = st.sidebar.selectbox(
        "Sort by",
        ["name", "price", "rating", "release_year"]
    )
    sort_order = st.sidebar.radio("Order", ["Ascending", "Descending"])
    ascending = sort_order == "Ascending"
    filtered_df = filtered_df.sort_values(by=sort_by, ascending=ascending)
    
    # Display products
    st.subheader(f"Found {len(filtered_df)} products")
    
    if len(filtered_df) == 0:
        st.warning("No products match your filters. Try adjusting the criteria.")
    else:
        # Product comparison mode
        st.markdown("---")
        st.subheader("Compare Products")
        
        # Select products to compare
        product_names = filtered_df["name"].tolist()
        
        col1, col2 = st.columns(2)
        
        with col1:
            product1 = st.selectbox("Select Product 1", product_names, key="p1")
        
        with col2:
            available_products = [p for p in product_names if p != product1]
            if available_products:
                product2 = st.selectbox("Select Product 2", available_products, key="p2")
            else:
                product2 = None
                st.warning("Add more products to compare")
        
        if product1 and product2:
            # Display comparison
            st.markdown("---")
            
            p1_data = filtered_df[filtered_df["name"] == product1].iloc[0]
            p2_data = filtered_df[filtered_df["name"] == product2].iloc[0]
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"### {p1_data['name']}")
                st.markdown(f"**Brand:** {p1_data['brand']}")
                st.markdown(f"**Category:** {p1_data['category']}")
                st.markdown(f"**Price:** ${p1_data['price']}")
                st.markdown(f"**Rating:** {p1_data['rating']:.1f} ⭐")
                st.markdown(f"**Screen Size:** {p1_data['screen_size']}")
                st.markdown(f"**Storage:** {p1_data['storage']}")
                st.markdown(f"**RAM:** {p1_data['ram']}")
                st.markdown(f"**Battery:** {p1_data['battery']}")
                st.markdown(f"**Release Year:** {p1_data['release_year']}")
            
            with col2:
                st.markdown(f"### {p2_data['name']}")
                st.markdown(f"**Brand:** {p2_data['brand']}")
                st.markdown(f"**Category:** {p2_data['category']}")
                
                # Highlight price difference
                if p2_data['price'] < p1_data['price']:
                    st.markdown(f"**Price:** ${p2_data['price']} :green[✓ Cheaper]")
                elif p2_data['price'] > p1_data['price']:
                    st.markdown(f"**Price:** ${p2_data['price']} :red[More expensive]")
                else:
                    st.markdown(f"**Price:** ${p2_data['price']}")
                
                # Highlight rating difference
                if p2_data['rating'] > p1_data['rating']:
                    st.markdown(f"**Rating:** {p2_data['rating']:.1f} ⭐ :green[✓ Higher]")
                elif p2_data['rating'] < p1_data['rating']:
                    st.markdown(f"**Rating:** {p2_data['rating']:.1f} ⭐ :red[Lower]")
                else:
                    st.markdown(f"**Rating:** {p2_data['rating']:.1f} ⭐")
                
                st.markdown(f"**Screen Size:** {p2_data['screen_size']}")
                st.markdown(f"**Storage:** {p2_data['storage']}")
                st.markdown(f"**RAM:** {p2_data['ram']}")
                st.markdown(f"**Battery:** {p2_data['battery']}")
                st.markdown(f"**Release Year:** {p2_data['release_year']}")
        
        # Show all filtered products in a table
        st.markdown("---")
        st.subheader("All Products")
        
        # Format the dataframe for display
        display_df = filtered_df.copy()
        display_df["price"] = display_df["price"].apply(lambda x: f"${x}")
        display_df = display_df.rename(columns={
            "name": "Product",
            "category": "Category",
            "brand": "Brand",
            "price": "Price",
            "rating": "Rating",
            "screen_size": "Screen Size",
            "storage": "Storage",
            "ram": "RAM",
            "battery": "Battery",
            "release_year": "Year"
        })
        
        st.dataframe(display_df, use_container_width=True, hide_index=True)

if __name__ == "__main__":
    main()
