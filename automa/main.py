import fastapi_jsonrpc as jsonrpc
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from automa.core.queue import queue
from automa.core.errors import *

# JSON-RPC entrypoint
api_v1 = jsonrpc.Entrypoint("/v0")

# Server singletons: database, queue and library handler

# RPC Methods


@api_v1.method(errors=[])
def account(client: str, random_nonce: int, signature: str) -> dict:
    """Get the associated account information for a signing wallet, will create resource if none exists"""

    logger.info("account {} was fetched", client)


@api_v1.method(errors=[])
def allocation(client: str, capability: int, nonce: int, signature: str) -> dict:
    """Get assigned a tranche of TMs to compute and submit before the epoch ends """

    logger.info("allocation requested for {} ", client)


@api_v1.method()
def network() -> dict:
    """Gets the latest volunteer network information"""


# entrypoint: ./api/v1/... methods=stamp, tree, validate
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
    logger.info("Provisioning auth store...")


# Dump the logs if a shutdown is occuring.
@app.on_event("shutdown")
async def shutdown():
    # ideally you'd put this backup in a docker volume, S3 or Grafana-compatible store.
    logger.info("Service is Shutting Down")
    # make one last attempt to anchor the sidetree before shutdown


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=5000, debug=True, access_log=False)
