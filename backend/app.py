import responder
import name_generator

api = responder.API(
    cors=True,
    allowed_hosts=["*"],
    cors_params={"allow_origins": "*",
                 "allow_methods": "*",
                 "allow_headers": "*"
                 })

@api.route("/api/generate")
async def on_post(req, resp):
    data = await req.media()
    print(data)
    compamy_name = name_generator.nama_generate(data["length"], data["fix_word"])

    resp.headers = {"Content-Type": "application/json; charset=utf-8"}
    resp.text = compamy_name

if __name__ == '__main__':
    api.run(address='0.0.0.0', port=5000)