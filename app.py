from flask import Flask, render_template, request
from scrape_amazon import scrape_amazon
from scrape_flipkart import scrape_flipkart
from scrape_croma import scrape_croma  # Import your Croma scraping function
from scrape_snapdeal import scrape_snapdeal  # Import your Snapdeal scraping function

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/compare', methods=['POST'])
def compare():
    product_name = request.form['product_name']

    # Get the selected websites from the form
    selected_websites = request.form.getlist('websites')

    results = {
        'amazon': [],
        'flipkart': [],
        'croma': [],
        'snapdeal': []
    }

    # Scrape results based on selected websites
    if 'amazon' in selected_websites:
        results['amazon'] = scrape_amazon(product_name)
    if 'flipkart' in selected_websites:
        results['flipkart'] = scrape_flipkart(product_name)
    if 'croma' in selected_websites:
        results['croma'] = scrape_croma(product_name)
    if 'snapdeal' in selected_websites:
        results['snapdeal'] = scrape_snapdeal(product_name)

    # Debugging lines to check the results
    print("Results:", results)

    return render_template('results.html', product_name=product_name,
                           amazon_results=results['amazon'],
                           flipkart_results=results['flipkart'],
                           croma_results=results['croma'],
                           snapdeal_results=results['snapdeal'])


if __name__ == '__main__':
    app.run(debug=True)
