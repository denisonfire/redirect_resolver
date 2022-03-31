import uuid

from flask import Flask, redirect, url_for, stream_with_context

app = Flask(__name__)


@app.route("/cycle/one")
def cycle_one():
    return redirect(url_for('cycle_two'))


@app.route("/cycle/two")
def cycle_two():
    return redirect(url_for('cycle_one'))


@app.route("/inf")
def inf():
    def gen():
        while True:
            yield uuid.uuid4().hex.upper()

    return app.response_class(stream_with_context(gen()), status=302, headers={"Location": "https://google.com"})


@app.route("/chain/<int:chain_id>")
def chain(chain_id):
    redirect_chain = iter(range(1, 6))
    for i in redirect_chain:
        if i == chain_id:
            try:
                return redirect(url_for('chain', chain_id=next(redirect_chain)))
            except StopIteration:
                return "<p>Success</p>"
