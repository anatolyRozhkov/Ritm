<h3>Swagger Documentation</h3>
[Swagger for regres.in](https://reqres.in/api-docs/)

<h3>Usage</h3>

```bash
docker-compose up -d --build

docker exec -it app bash

pytest -sv --tb long
```

<h3>Hello</h3>
Here I've constructed several 'integration tests'. 
I take the word integration into quotation marks because here
I actually don't have access to the DB tho it is required for 
the tests to actually fulfil their purpose. 

Instead, I've constructed a few fixtures that would make requests to 
the users endpoint and store data, so that I could use the data for 
cross-verification instead of the DB. 

<h3>Checkout Actions</h3>
You can review how the tests have run in the Actions dashboard.
Just make sure to open the Run Tests dropdown.