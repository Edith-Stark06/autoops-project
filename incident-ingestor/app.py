from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

@app.route("/incident", methods=["POST"])
def receive_incident():
    incident = request.json

    # Basic validation
    required_fields = [
        "incident_id",
        "source",
        "service_name",
        "symptom",
        "timestamp",
        "severity_hint"
    ]

    for field in required_fields:
        if field not in incident:
            return jsonify({"error": f"Missing field: {field}"}), 400

    enriched_incident = {
        "internal_id": str(uuid.uuid4()),
        "received_at": datetime.utcnow().isoformat(),
        "status": "RECEIVED",
        **incident
    }

    return jsonify({
        "message": "Incident received successfully",
        "incident": enriched_incident
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
