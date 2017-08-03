from flask import Flask
app = Flask(__name__)

@app.route('/build', methods=['POST'])
def build():
    branch, tag = GitHubEventParser.get_branch_and_tag()

if __name__ == '__main__':
    app.run()
