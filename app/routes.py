from flask import render_template, request, redirect, url_for, flash
from app import app

# In-memory data store
topics = []

@app.route('/')
def index():
    return render_template('index.html', topics=topics)

@app.route('/topic/<int:topic_id>')
def topic(topic_id):
    topic = next((t for t in topics if t['id'] == topic_id), None)
    if topic:
        return render_template('topic.html', topic=topic)
    else:
        flash('Topic not found', 'error')
        return redirect(url_for('index'))

@app.route('/create_topic', methods=['GET', 'POST'])
def create_topic():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        content = request.form.get('content')
        if title and author and content:
            new_topic = {
                'id': len(topics) + 1,
                'title': title,
                'author': author,
                'content': content,
                'replies': []
            }
            topics.append(new_topic)
            flash('Topic created successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('All fields are required', 'error')
    return render_template('create_topic.html')

@app.route('/topic/<int:topic_id>/reply', methods=['POST'])
def add_reply(topic_id):
    topic = next((t for t in topics if t['id'] == topic_id), None)
    if topic:
        author = request.form.get('author')
        content = request.form.get('content')
        if author and content:
            topic['replies'].append({'author': author, 'content': content})
            flash('Reply added successfully!', 'success')
        else:
            flash('All fields are required', 'error')
    else:
        flash('Topic not found', 'error')
    return redirect(url_for('topic', topic_id=topic_id))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404