from flask import Flask, render_template, request, escape
def search4letters(phrase: str, letters: str='aeiou') -> set:
    return set(letters).intersection(set(phrase))

app=Flask(__name__)
@app.route('/')
def hello()-> str:
     return 'Hello world from Flask'

@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('log.txt') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html', the_title='Viev Log', the_row_titles=titles,the_data=contents,)


@app.route('/test')
def test_page()->'html':
    return render_template('test.html', the_title="Welcom")

@app.route('/test-result', methods=['POST'])
def testPost()->'html':
    your_name=request.form['your_name']
    return render_template('test-result.html', your_name=your_name)

def log_request(req:'flask_request', res: str) -> None:
    with open('log.txt', 'a') as log:
        print(req.form, req.remote_addr,req.user_agent,res,file=log, sep='|')
@app.route('/search4', methods=['POST'])
def do_search()->'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                            the_phrase=phrase,
                            the_letters=letters,
                            the_title=title,
                            the_results=results)
@app.route('/entry')
def entry_page()->'html':
    return render_template('entry.html', the_title="Welcom")

app.run()
