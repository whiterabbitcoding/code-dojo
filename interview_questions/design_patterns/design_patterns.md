What is your favourite design pattern?

Factory Method is often really helpful has been used it multiple times. As a creator
its quite powerful

Used it as part of rules engine for performing data transformation, each cell
would have a rule and rules could perform different transformations so we had
arithmetic rules, semantic rules and more

Also used a DAG factory with airflow to automate the creation of dags just by
setting parameters in a data structure, which was also pretty powerful and
reduces your code significantly

Singelton - ensure you only have one instance of a class. Useful if you want a
class that cannot be duplicated. for example configuration information with
private keys etc.

Orchestrator - Orchestration is ideal for large projects with complex
microservice architectures.

It manages to calls to multiple services based on the input it receives, these
are to process information for the client, but it can also deliver information
to other services for monitoring etc. Control the lines and traffic but does not
execute any process on data.
