from flask import Flask,render_template,request
from supabase import create_client, Client
import os

app = Flask(__name__)
url = os.getenv("url","https://iapmnqxcyfcrgenxhfgl.supabase.co")
key = os.getenv("key","eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlhcG1ucXhjeWZjcmdlbnhoZmdsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTUxMzQwNzEsImV4cCI6MjA3MDcxMDA3MX0.IvavLJVTVJtBD2N7FMCo6Ro-Xomyx2apdoyQBYWcp0s")
supabase: Client = create_client(url, key)

@app.route('/')
def index():
    response = supabase.table('Nucleus').select('*').execute()
    return render_template('index.html', data=response.data)

@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('name')
    amount = request.form.get('amount')
    supabase.table('Nucleus').insert({'name': name,'amount': amount}).execute()
    return 'Added successfully! <a href="/">Go back</a>'

@app.route('/delete/<int:item_id>', methods=['GET'])
def delete():
    item_id = request.args.get('id')
    supabase.table('Nucleus').delete().eq('id', item_id).execute()
    return 'Deleted successfully! <a href="/">Go back</a>'

if __name__ == '__main__':
    app.run(debug=True)
