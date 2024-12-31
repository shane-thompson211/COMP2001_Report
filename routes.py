from flask import Blueprint, jsonify, request
from db_connection import get_db_connection

# Create a Blueprint for routes
api = Blueprint('api', __name__)

# GET /trails: Fetch all trails
@api.route('/trails', methods=['GET'])
def get_trails():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("EXEC CW2.GetAllTrails")  # Call stored procedure
        trails = []
        for row in cursor.fetchall():
            trails.append({
                "TrailID": row[0],
                "TrailName": row[1],
                "Location": row[2]
            })
        return jsonify(trails)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

# POST /trails: Add a new trail
@api.route('/trails', methods=['POST'])
def add_trail():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "EXEC CW2.InsertTrail ?, ?, ?, ?, ?, ?, ?, ?, ?",
            data['TrailName'], data['TrailSummary'], data['TrailDescription'],
            data['Difficulty'], data['Location'], data['Length'],
            data['ElevationGain'], data['RouteType'], data['OwnerID']
        )
        conn.commit()
        return jsonify({"message": "Trail added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

# DELETE /trails/<trail_id>: Delete a trail
@api.route('/trails/<int:trail_id>', methods=['DELETE'])
def delete_trail(trail_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("EXEC CW2.DeleteTrail ?", trail_id)
        conn.commit()
        return jsonify({"message": f"Trail {trail_id} deleted successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

# Optional: GET /trails/<trail_id>: Fetch a specific trail
@api.route('/trails/<int:trail_id>', methods=['GET'])
def get_trail(trail_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("EXEC CW2.GetTrailByID ?", trail_id)
        row = cursor.fetchone()
        if row:
            return jsonify({
                "TrailID": row[0],
                "TrailName": row[1],
                "Location": row[2]
            })
        else:
            return jsonify({"message": "Trail not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()
