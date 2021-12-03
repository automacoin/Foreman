# The simple Automacoin manager node

This repo contains the necessary components to manage a swarm of browser clients in a volunteer swarm. Refer to the messages reference JSON to implement non-browser clients that are interoperable with this manager node.

to run execute run.sh, or use gunicorn in production. You will need to have python  poetry and a redis server installed and configured correctly to run this node.

## Design

This node accept JSON-RPC requests for allocations, which represent a tranche of TMs the requester is assigned. They are due to be completed by the end of the epoch. If they are completed, they go into the queue and a subset of them are double checked. Once the foreman has confidence that tranche is honest, the Tapes are submitted to the library and all unpaid submissions are periodically settled in automacoin to the tranche signatory's addresss.

When combined with the browser frontend, this completes V0 of the automacoin system.


# Development

To Run:
`$ docker-compose up -d --build`