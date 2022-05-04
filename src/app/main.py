import fastapi_jsonrpc as jsonrpc
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from sqlalchemy import *
from app.errors import *
from app.queue import Queue

# JSON-RPC entrypoint
api_v1 = jsonrpc.Entrypoint("/v1")

# Server singletons: database, queue and library handler
queue = Queue("redis")
# RPC Methods


@api_v1.method(errors=[])
def allocation() -> dict:
    """Get assigned a start for your brick of TMs to compute and submit"""
    logger.info("allocation requested ")


@api_v1.method(errors=[])
def submission(client: str, start_tm: int, result_map: dict) -> dict:
    """Submit your TM results for an allocated compute task"""
    logger.info("submission made for {} ", start_tm)


@api_v1.method()
def network() -> dict:
    """Gets the latest volunteer network information"""
    results = {
        "latest_turing_space": 3,
        "total_clients": 112,
        "automacoin_supply": 10000,
        "brick_size": 500,
    }
    return results


# entrypoint: ./api/v1/... methods=account, allocation, network
app = jsonrpc.API()
app.bind_entrypoint(api_v1)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# configure logger session
@app.on_event("startup")
async def startup():
    logger.add("file_{time}.log")
    logger.info("Service is Spinning Up")
    logger.info("Starting tape store...")


# Dump the logs if a shutdown is occuring.
@app.on_event("shutdown")
async def shutdown():
    # ideally you'd put this backup in a docker volume, S3 or Grafana-compatible store.
    logger.info("Service is Shutting Down")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=5000, debug=True, access_log=False)
