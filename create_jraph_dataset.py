import jraph
import numpy as np
import pickle
import jax
import jax.numpy as jnp

n_points = 30
dataset = []
key = jax.random.PRNGKey(0)


for i in range(n_points):
    # Nodes
    nodes = np.array([
        [1.0, 2.0],  # Node 0
        [3.0, 4.0],  # Node 1
        [5.0, 6.0]   # Node 2
    ])

    # Edges
    edges = np.array([
        [0.5, 0.6],  # Edge 0
        [0.7, 0.8]   # Edge 1
    ])

    # Globals
    global_attr = np.array([0.1, 0.2])


    # Senders and Receivers
    senders = np.array([0, 1])     # Node 0 sends Edge 0, Node 1 sends Edge 1
    receivers = np.array([1, 2])   # Node 1 receives Edge 0, Node 2 receives Edge 1

    graph = jraph.GraphsTuple(
        n_node=np.array([len(nodes)]),  # Number of nodes in each graph
        n_edge=np.array([len(edges)]),  # Number of edges in each graph
        nodes=nodes,
        edges=edges,
        globals=global_attr,
        senders=senders,
        receivers=receivers,
    )

    # Standardize the GraphsTuple for use in a Graph Net.
    graph = jraph.GraphsTuple(nodes=jax.random.normal(key, (5, 64)),
                  edges=jax.random.normal(key, (10, 64)),
                  senders=jnp.array([0,0,1,1,2,2,3,3,4,4]),
                  receivers=jnp.array([1,2,0,2,1,0,2,1,3,2]),
                  n_node=jnp.array([5]),
                  n_edge=jnp.array([10]),
                  globals=jax.random.normal(key, (1, 64)))

    target = [1]
    dataset.append({"input_graph": graph, "target": target})


with open('graph_test_dataset.pkl', 'wb') as f:
    pickle.dump(dataset, f)

with open('graph_test_dataset.pkl', 'rb') as f:
    dataset = pickle.load(f)
print(dataset[23].keys())