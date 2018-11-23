# Stream data from templates

from flask import stream_with_context
from flask import Response, Flask


app = Flask(__name__)


def stream_templates(template_name, **context):
    app.update_template_context(context)
    temp = app.jinja_env.get_template(template_name)
    rv = temp.stream(context)
    rv.enable_buffering(5)

    return rv


@app.route('large_page.html')
def render_template():
    rows = iter_all_rows()
    return Response(stream_templates('template.html'), rows=rows)


def iter_all_rows():
    with open('file') as fh:
        for line in fh:
            yield line


# Keep the context during generation


@app.route('/stream')
def stream_context():
    @stream_with_context
    def generate():
        iter_all_rows()

    return Response(generate())
