# Testing best-practices

https://www.youtube.com/watch?v=ESHn53myB88&ab_channel=ContinuousDelivery

- Testing gets harder at the _edges_ of our systems (DB, filesystem, messaging, UI, upsteam/downstream systems, etc)
- Individual components should be easy to test
- Make all logic unit-testable in memory
  - Create an _abstraction_ of an edge. Example: abstraction of writing to a file.
  - Test to that abstraction


## Example

File words sorter
- Read a list of words from a file, sort them and write the sorted list of words to another file.
