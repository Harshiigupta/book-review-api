from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Book, Review
from app import db
from sqlalchemy.sql import func

bp = Blueprint('books', __name__, url_prefix='/books')

@bp.route('', methods=['POST'])
@jwt_required()
def add_book():
    data = request.json
    book = Book(**data)
    db.session.add(book)
    db.session.commit()
    return jsonify({'message': 'Book added'}), 201

@bp.route('', methods=['GET'])
def get_books():
    page = int(request.args.get('page', 1))
    author = request.args.get('author')
    genre = request.args.get('genre')
    query = Book.query
    if author:
        query = query.filter(Book.author.ilike(f'%{author}%'))
    if genre:
        query = query.filter_by(genre=genre)
    books = query.paginate(page, 10, False).items
    return jsonify([{'id': b.id, 'title': b.title, 'author': b.author, 'genre': b.genre} for b in books])

@bp.route('/<int:book_id>', methods=['GET'])
def book_details(book_id):
    book = Book.query.get_or_404(book_id)
    avg_rating = db.session.query(func.avg(Review.rating)).filter_by(book_id=book_id).scalar() or 0
    reviews = [{'user_id': r.user_id, 'rating': r.rating, 'comment': r.comment} for r in book.reviews]
    return jsonify({
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'genre': book.genre,
        'average_rating': round(avg_rating, 2),
        'reviews': reviews
    })

@bp.route('/search', methods=['GET'])
def search_books():
    q = request.args.get('q', '')
    results = Book.query.filter((Book.title.ilike(f'%{q}%')) | (Book.author.ilike(f'%{q}%'))).all()
    return jsonify([{'id': b.id, 'title': b.title, 'author': b.author} for b in results])
