# Quickstart

Start server:

uvicorn api.server:app --reload

Register node:

curl -X POST http://127.0.0.1:8000/register \
-H "Content-type: application/json" \
-d '{"node_id":"node-1","gpu":"A100","location":"Mumbai"}'

Submit job:

curl -X POST http://127.0.0.1:8000/submit \
-H "Content-type: application/json" \
-d '{"id":"job-001","gpu_required":"A100"}'

Dispatch:

curl -X POST http://127.0.0.1:8000/dispatch
