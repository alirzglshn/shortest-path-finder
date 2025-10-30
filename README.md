SHORTEST PATH FINDER

## 📚 API Documentation

The full API documentation and Postman collection can be accessed here:  
https://alirzglshn-8297069.postman.co/workspace/Alireza's-Workspace~49656c62-33a9-48a0-8b97-02f1425f975e/collection/48359113-b8c2a685-2ae4-4d60-8139-4408ad7a7283?action=share&source=copy-link&creator=48359113

You can import this directly into Postman to start testing all endpoints.

🔷 Project Overview 

Shortest Path Finder is a RESTful API built with Django REST Framework that allows you to:

Create, retrieve, update, and delete graphs, nodes, and edges.

Compute shortest paths using Dijkstra’s algorithm for any graph.

Explore and test graph structures programmatically via HTTP requests.

This API is ideal for frontend developers to integrate interactive graph features into web apps.


🧩 Features

🔸Full CRUD functionality for:

Graphs

Nodes

Edges

🔸 Custom endpoint to calculate shortest paths:

Returns distances from a start node to all other nodes

Optional path reconstruction to a target node

🔸 Clean and scalable project structure

🔸 Designed for easy collaboration with frontend developers


📂 Project Structure
dijkstra/             # Django project root
├─ dijkstra/          # Project settings
│  ├─ settings.py
│  ├─ urls.py
├─ graph/             # Main app
│  ├─ models.py       # Graph, Node, Edge
│  ├─ serializers.py  # DRF serializers
│  ├─ views.py        # ViewSets & endpoints
│  ├─ urls.py         # App URL routing
│  ├─ algorithm.py    # Dijkstra algorithm logic
│  ├─ priorityqueue.py# Simple priority queue for Dijkstra
├─ manage.py


🚀 Installation & Setup
Prerequisites

asgiref             
Django              
djangorestframework 
mysqlclient (if your db is mysql)
pip                 
setuptools          
sqlparse           
tzdata              
Virtual environment (optional but recommended)


Steps : 

# 1. Clone the repo
git clone https://github.com/alirzglshn/shortest-path-finder.git
cd dijkstra

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Run server
python manage.py runserver

Your API should now be available at :
http://127.0.0.1:8000/


🛠️ API Endpoints

All endpoints in postman are prefixed by the base URL: {{base_url}} = http://127.0.0.1:8000/

GRAPHS:
| Method | Endpoint                    | Description                    |
| ------ | --------------------------- | ------------------------------ |
| GET    | /graphs/                    | Retrieve all graphs            |
| POST   | /graphs/                    | Create a new graph             |
| GET    | /graphs/{id}/               | Get single graph               |
| PUT    | /graphs/{id}/               | Update a graph                 |
| DELETE | /graphs/{id}/               | Delete a graph                 |
| POST   | /graphs/{id}/shortest_path/ | Compute Dijkstra shortest path |

NODES:
| Method | Endpoint     | Description        |
| ------ | ------------ | ------------------ |
| GET    | /nodes/      | Retrieve all nodes |
| POST   | /nodes/      | Create a new node  |
| GET    | /nodes/{id}/ | Get single node    |
| PUT    | /nodes/{id}/ | Update a node      |
| DELETE | /nodes/{id}/ | Delete a node      |

EDGES :
| Method | Endpoint     | Description        |
| ------ | ------------ | ------------------ |
| GET    | /edges/      | Retrieve all edges |
| POST   | /edges/      | Create a new edge  |
| GET    | /edges/{id}/ | Get single edge    |
| PUT    | /edges/{id}/ | Update an edge     |
| DELETE | /edges/{id}/ | Delete an edge     |


💻 Example Request
POST Create Graph

Request:
{
  "name": "Iran Cities Graph",
  "description": "Graph connecting major Iranian cities."
}

Response :

{
  "id": 1,
  "name": "Iran Cities Graph",
  "description": "Graph connecting major Iranian cities.",
  "nodes": [],
  "edges": []
}

POST Shortest Path Example:

request :
{
  "start_node_id": 9
}

response :
{
  "Distances": {
    "Tehran": 0,
    "Tabriz": 600,
    "Esfahan": 400,
    "Shiraz": 900
  }
}

⚡ Tips for Frontend Developers

Use GraphViewSet endpoints for main graph operations.

Nodes and edges can be created or updated dynamically.

Dijkstra endpoint returns distances by node names for easy display.

Thanks for viewing this repository.
