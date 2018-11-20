# Inner function uses generator to yield data
# Invoke this function and pass it to the response object

from flask import Response


@app.route('/file.csv')
# Generate comma separated values
def generate_csv():
    def generate():
        for row in iter_rows():
            yield ','.join(row) + '\n'

    return Response(generate(), mimetype='text/csv')


def iter_rows():
    with open('large_file.csv') as fh_csv:
        for line in fh_csv:
            yield line
