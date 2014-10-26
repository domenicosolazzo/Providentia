from flask import Flask
from flask import jsonify
from providentia.core.brain import ProvidentiaBrain
app = Flask(__name__)

@app.route('/keywords')
def keywords():
    brain = ProvidentiaBrain()
    k = brain.fetch_top_keywords()
    return jsonify(data={'entries':k, 'count':len(k)})


@app.route('/')
def top_keywords():
    brain = ProvidentiaBrain()
    data = brain.winsdom()
    clusters = data.get('clusters', [])
    titles = data.get('titles', [])
    k = data.get('keywords',[])

    c = {}
    keys = []
    for key in clusters:
       documents = []
       for id in clusters[key]:
         documents.append({'id':id,'title:':titles[id]})
       c[key] = documents
    return jsonify(data={ 'keywords':{'entries':k, 'count':len(k)},
                          'clusters':c,
                          'titles':{'entries':titles, 'count':len(titles)}})

if __name__ == '__main__':
    app.debug = True
    app.run()
