from flask import Flask, flash, redirect, render_template, request, session, abort,send_from_directory,send_file,jsonify
import pandas as pd
import json
import numpy as np
import json_generator

application= Flask(__name__)

class KeyStore():
    key=None
keyStore=KeyStore()

params = {
    'number_of_items_to_display': 700,
    'key_sort': 'scores_overall' #stats_salary, scores_overall
}


@application.route("/",methods=["GET","POST"])
def homepage():
    return render_template("index.html")

@application.route("/get-data",methods=["GET","POST"])
def returnProdData():
    if keyStore.key == "overall":
        json_data = json_generator.json_over_score(key_sort=params['key_sort'], nums_of_items=params['number_of_items_to_display'])
        return jsonify(json_data)
    if keyStore.key == "region":
        json_data = json_generator.json_over_score_region(key_sort=params['key_sort'], nums_of_items=params['number_of_items_to_display'])
        return jsonify(json_data)
    if keyStore.key == "salary":
        json_data = json_generator.json_over_score_salary_region(key_sort=params['key_sort'], nums_of_items=params['number_of_items_to_display'])
        return jsonify(json_data)
    if keyStore.key == "subject":
        json_data = json_generator.json_over_score_subject(key_sort=params['key_sort'], nums_of_items=params['number_of_items_to_display'])
        return jsonify(json_data)
    return jsonify({'name': "Not found!", "children":[]})

@application.route("/circle_packing",methods=["GET","POST"])
def circle_packing():
    keyStore.key = request.form.get('key', "overall")
    print(keyStore.key)
    return {"status": "ok"}

@application.route("/render_detail",methods=["GET","POST"])
def render_detail():
    return render_template("detail.html")

if __name__ == "__main__":
    application.run(debug=True)


