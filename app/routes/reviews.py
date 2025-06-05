from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Review, Book

bp = Blueprint('reviews', __name__)

@bp.route('/books/<int:book_id>/reviews', methods=['POST'])
@jwt_required()
def submit_review(book_id):
    user_id = get_jwt_identity()
    if Review.query.filter_by(user_id=user_id, book_id=book_id).first():
        return jsonify({'error': 'Already reviewed'}), 400
    data = request.json
    review = Review(user_id=user_id, book_id=book_id, rating=data['rating'], comment=data['comment'])
    db.session.add(review)
    db.session.commit()
    return jsonify({'message': 'Review submitted'}), 201

@bp.route('/reviews/<int:review_id>', methods=['PUT'])
@jwt_required()
def update_review(review_id):
    user_id = get_jwt_identity()
    review = Review.query.get_or_404(review_id)
    if review.user_id != user_id:
        return jsonify({'error': 'Unauthorized'}), 403
    data = request.json
    review.rating = data.get('rating', review.rating)
    review.comment = data.get('comment', review.comment)
    db.session.commit()
    return jsonify({'message': 'Review updated'})

@bp.route('/reviews/<int:review_id>', methods=['DELETE'])
@jwt_required()
def delete_review(review_id):
    user_id = get_jwt_identity()
    review = Review.query.get_or_404(review_id)
    if review.user_id != user_id:
        return jsonify({'error': 'Unauthorized'}), 403
    db.session.delete(review)
    db.session.commit()
    return jsonify({'message': 'Review deleted'})
