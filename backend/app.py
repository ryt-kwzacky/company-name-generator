import responder
import name_generator

api = responder.API(
    cors=True,
    allowed_hosts=["*"],
    cors_params={"allow_origins": "*",
                 "allow_methods": "*",
                 "allow_headers": "*"
                 })

@api.route("/")
def hello_world(req, resp):
    text = name_generator.test()

    resp.headers = {"Content-Type": "application/json; charset=utf-8"}
    resp.text = text


if __name__ == '__main__':
    api.run(address='0.0.0.0', port=5000)