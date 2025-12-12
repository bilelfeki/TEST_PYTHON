from flask import Flask, request, jsonify

app = Flask(__name__)

def build_postman_oauth_mapping(d):
    return {
        "Grant Type": "Authorization Code",
        "Callback URL": d["ru"],
        "Auth URL": d["pu"] + d["oa"],
        "Access Token URL": d["pu"] + d["ot"],
        "Client ID": d["ci"],
        "Client Secret": d["cs"],
        "Revoke URL": d["pu"] + d["or"],
        "Issuer URL": d["iu"],
        "Token Issuer": d["ti"],
        "Environment": d["ev"],
        "Version": d["v"]
    }

@app.route("/map", methods=["POST"])
def map_oauth():
    data = request.json
    return jsonify(build_postman_oauth_mapping(data))
