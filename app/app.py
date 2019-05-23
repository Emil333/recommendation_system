from flask import Flask, request
import product_pref as product_pref
import user_pref as user_pref
import recommendation as recommendation

app = Flask(__name__, static_url_path='')


@app.route('/set-user-pref', methods=['POST'])
def take_user_input():
    request_body = request.get_json()
    user_pref.clear_user_pref()
    user_pref.preferences = request_body[0]
    return 'success'

@app.route('/set-product-list', methods=['POST'])
def set_product_list():
    request_body = request.get_json()
    product_pref.clear_product_pref()
    product_pref.products = list(request_body)
    return 'success'

@app.route('/get-recommended', methods=['GET'])
def get_recommended_products():
    # recommendation.get_recommended_product()
    print(recommendation.get_recommended_product())
    return 'success'

@app.route('/set-weights', methods=['POST'])
def set_weights():
    request_body = request.get_json()
    recommendation.weights = list(request_body)
    print(recommendation.weights)
    return 'success'




if __name__ == '__main__':
    app.run(host='0.0.0.0')