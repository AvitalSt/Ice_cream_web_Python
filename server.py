from flask import Flask, request, render_template, redirect, url_for,session,flash
from models import login_model, ice_cream_model

app = Flask(__name__)
app.secret_key = 's3cr3t_k3y_th4t_i5_l0ng_4nd_r4nd0m'
@app.route('/')
def root():
    return redirect(url_for('login_page'))

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':  
        user_name = request.form['user_name']
        password = request.form['password']
        if login_model.is_admin(user_name, password):
            session['user_name'] = user_name
            return redirect(url_for('home', success='admin_enter', user_name=user_name))
        elif login_model.is_register(user_name, password):
            session['user_name'] = user_name
            return redirect(url_for('home', success="user_enter", user_name=user_name))
        else:
            if login_model.search_user_by_name(user_name):
                return redirect(url_for('login', success='exist_in', user_name=user_name))
            else:
                login_model.add_user(user_name, password)
                session['user_name'] = user_name
                return redirect(url_for('home', success='user_added', user_name=user_name))
    
    # אם זו בקשת GET, נבצע רינדור של עמוד ההתחברות
    success = request.args.get('success')
    user_name = request.args.get('user_name')
    return render_template('login.html', success=success, user_name=user_name)


@app.route('/index.html')
def home():
    return render_template('index.html') 

@app.route('/product.html')
def product():
    ice_creams = ice_cream_model.get_all_ice()
    return render_template('product.html', ice_creams=ice_creams)

@app.route('/add_ice_cream', methods=['GET', 'POST'])
def add_ice_cream():
    if request.method == 'POST':
        ice_cream_name = request.form['ice_cream_name']
        description = request.form['description']
        price_per_ball = request.form['price_per_ball']
        price_per_kilo = request.form['price_per_kilo']
        img = request.form['img']
        ice_cream_model.add_ice_cream(ice_cream_name, description, price_per_ball, price_per_kilo, img)
        return redirect(url_for('home'))  
    return render_template('add_ice_cream.html')

@app.route('/form_add_ice_cream')
def form_add_ice():
    return render_template('add_ice_cream.html')

@app.route('/more_details_ice_cream/<int:ice_cream_id>')
def more_details(ice_cream_id):
    ice_cream = ice_cream_model.get_ice_cream_by_id(ice_cream_id)
    return render_template('more_details_ice_cream.html', ice_cream=ice_cream)

@app.route('/search_ice_cream')
def search_ice_cream_route():
    search_query = request.args.get('search', '')
    ice_creams = ice_cream_model.search_ice_cream(search_query)
    return render_template('product.html', ice_creams=ice_creams)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
