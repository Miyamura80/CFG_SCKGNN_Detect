# CFG_SCKGNN_Detect

Tooling to convert bytecode into knowledge graphs (KG). We generate the bytecode control flow graph (CFG) from the bytecode, then develop an encoding scheme for a general bytecode block, to map a sequence of smart contract bytecode instructions to a latent vector representation of a bytecode block (i.e. a node of the KG). 

We develop two variants of this KG dataset, one using the OpenAI embeddings, and another with our own trained Autoencoder. We then use these KGs to run classification with KG graph neural networks, to develop new tools for smart contract vulnerability classification against a dataset of the most significant vulnerabilities. 
![ourmethodology](https://github.com/Miyamura80/CFG_SCKGNN_Detect/assets/38335479/51ffa743-ddb8-461c-943a-ad738225ae7a)


![knowledge graph generation](https://github.com/Miyamura80/CFG_SCKGNN_Detect/assets/38335479/401a830d-968e-4dc1-b533-dea2e01bf77f)


![autoencoder](https://github.com/Miyamura80/CFG_SCKGNN_Detect/assets/38335479/fb027842-14bb-411b-a5a7-371635470c3a)
