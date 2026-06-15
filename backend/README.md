#Flipo-saas Starter Backend

This backend provides the FastAPI foundation for theFlipo-saas starter app. It includes API routing, CORS configuration, a basic auth guard, Hugging Face inference wiring, and Stripe checkout session creation.

## Stack

- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic Settings
- Stripe Python SDK
- Requests / HTTPX

## Project Layout

```text
backend/
├── app/
│   ├── api/
│   │   ├── v1/endpoints/
│   │   └── routes.py
│   ├── core/
│   │   ├── auth.py
│   │   ├── config.py
│   │   ├── prompt.py
│   │   └── security.py
│   ├── db/
│   ├── models/
│   ├── services/
│   │   ├── huggingface_service.py
│   │   └── stripe_service.py
│   └── main.py
├── requirements.txt
├── run-backend.sh
└── tests/
```

## Setup

From the repository root:

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file in `backend/` with the required values:

```env
STRIPE_SECRET_KEY=your_stripe_secret_key
STRIPE_WEBHOOK_SECRET=your_stripe_webhook_secret
HUGGINGFACE_TOKEN=your_huggingface_token
OPENAI_API_KEY=your_openai_api_key
SUPABASE_URL=your_supabase_project_url
SUPABASE_JWT_SECRET=your_supabase_jwt_secret
BACKEND_CORS_ORIGINS=["http://localhost:3000","http://localhost:5173"]
```

Notes:

- `OPENAI_API_KEY` is optional in the current codebase.
- `HUGGINGFACE_TOKEN` is optional in settings, but the prediction endpoint expects it for authenticated inference requests.
- `BACKEND_CORS_ORIGINS` should be a JSON-style list because it is parsed by Pydantic settings.

## Run Locally

Option 1:

```bash
cd backend
./run-backend.sh
```

Option 2:

```bash
cd backend
source .venv/bin/activate
uvicorn app.main:app --reload
```

The API will start at `http://localhost:8000`.

## Available Endpoints

Public:

- `GET /` returns a welcome message

Protected by the current auth dependency:

- `GET /api/v1/health`
- `POST /api/v1/predict`
- `POST /api/v1/create-checkout-session`

## Endpoint Notes

### `POST /api/v1/predict`

Calls the Hugging Face inference API using the configured token and returns the model response.

Example request:

```bash
curl -X POST "http://localhost:8000/api/v1/predict?input_text=I%20love%20this" \
  -H "Authorization: Bearer your-token"
```

### `POST /api/v1/create-checkout-session`

Creates a Stripe Checkout session and returns the hosted checkout URL.

Before using it, update the placeholder values in `app/services/stripe_service.py`:

- Stripe price ID
- Success URL
- Cancel URL

## Authentication

All `/api/v1` routes currently depend on `verify_supabase_token`.

Right now, that function only checks whether the `Authorization` header exists. It does not yet validate the Supabase JWT, so this should be treated as scaffolding rather than production-ready authentication.

## Testing

There is an initial test file in `backend/tests/test_user.py`, but the backend test setup is still minimal. Expand coverage as endpoints and services become more stable.

## Current Gaps

- Supabase JWT validation is not fully implemented.
- Stripe checkout uses placeholder configuration values.
- No checked-in `.env.example` file yet.
- Test coverage is still minimal.
