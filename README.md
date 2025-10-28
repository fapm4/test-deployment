# Tech Product Comparison App

A Streamlit web application for comparing technical specifications, prices, and ratings of popular tech products.

## Features

- 💻 Compare smartphones, laptops, and tablets side-by-side
- 🔍 Filter products by category, brand, price range, and rating
- 📊 Sort products by name, price, rating, or release year
- ⚡ Interactive comparison with visual highlighting of differences
- 📱 Responsive design with wide layout

## Installation

1. Clone this repository:
```bash
git clone https://github.com/fapm4/test-deployment.git
cd test-deployment
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`.

## Features in Detail

### Filters
- **Category**: Filter by Smartphone, Laptop, or Tablet
- **Brand**: Filter by manufacturer (Apple, Samsung, Google, Dell, Lenovo)
- **Price Range**: Adjust slider to filter by budget
- **Minimum Rating**: Filter products by minimum rating

### Comparison
1. Use the filters to narrow down products
2. Select two products from the dropdown menus
3. View side-by-side comparison with highlighted differences
4. Green checkmarks indicate better values (lower price, higher rating)

### Product Data
The app includes sample data for popular products including:
- iPhone 15 Pro, Samsung Galaxy S24, Google Pixel 8 Pro
- MacBook Pro 14", Dell XPS 15, ThinkPad X1 Carbon
- iPad Pro 12.9", Samsung Galaxy Tab S9

## Technologies Used

- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis

## License

MIT