## 📊 Analysis Service

The **Analysis Service** provides AI-based fashion analysis for a given product in the context of a selected user profile. It connects with a Chrome extension frontend and uses the OpenAI ChatGPT API to generate intelligent fashion insights.

---

### 🚀 Features

* Accepts JSON input with a **profile** and **product**.
* Uses the **ChatGPT API** to analyze the product in the context of the profile.
* Designed to be consumed directly by the **Chrome Extension**.
* Can access `/profiles` endpoint to retrieve all accessible user profiles for a given user.

---

### 📦 API Endpoints

#### `POST /verdict`

* **Description**: Analyze a product for a given profile.
* **Request Body**:

  ```json
  {
    "profile": { /* profile object */ },
    "product": { /* product object */ }
  }
  ```
* **Response**:

  ```json
  {
    "analysis": "This outfit suits your warm skin tone and oval face shape..."
  }
  ```

#### `GET /profiles`

* **Description**: Returns all profiles the authenticated user has access to.

---

### 🔐 Authentication

* This service expects an **Authorization token** (e.g., Keycloak JWT) in requests.
* User access control is enforced at the `/profiles` level.

---

### 🧠 AI Integration

* Uses **OpenAI's ChatGPT API** to generate natural language analysis.
* Prompt generation is done internally based on the provided profile and product structure.

---

### 🧪 Health Check

* `GET /health` returns a `200 OK` if the service is running.

---

### 🔧 Environment Variables

| Variable Name         | Description                      |
| --------------------- | -------------------------------- |
| `OPENAI_API_KEY`      | API key to access ChatGPT        |
| `KEYCLOAK_URL`        | URL for Keycloak authentication  |
| `PROFILE_SERVICE_URL` | URL to fetch accessible profiles |

---

### 🔗 Consumes / Talks To

* ✅ **Chrome Extension** – directly consumes this service.
* ✅ **Keycloak** – used for authentication and authorization.
* ✅ **Profile Service** – via `/profiles` endpoint.

