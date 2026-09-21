from time import perf_counter

from fastapi.testclient import TestClient

from app.main import app


def main() -> None:
    requests = 100
    started = perf_counter()
    with TestClient(app) as client:
        responses = [client.get("/api/v1/items/?limit=3") for _ in range(requests)]
    elapsed_ms = round((perf_counter() - started) * 1000, 3)
    assert all(response.status_code == 200 for response in responses)
    print({"requests": requests, "elapsedMilliseconds": elapsed_ms, "successful": len(responses)})


if __name__ == "__main__":
    main()
