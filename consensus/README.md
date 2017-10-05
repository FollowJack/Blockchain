What is the FLP impossibility?
The FLP result does not state that consensus 
can never be reached: merely that under the 
model's assumptions, no algorithm can always 
reach consensus in bounded time. In practice 
it is highly unlikely to occur.

Consensus primitives:
termination - every correct process eventually 
decides
integrity - every correct process decides at 
most once
agreement - if one correct process decides 1 
and another decides v 2, 
then v1 = v2• validity - if a correct process decides v, at least one process proposed v

What is Paxos?
simultaneously empowered and confused the discipline of consensus science,
on  the  one  hand  by  providing  the  first  real-world,  practical,  fault-tolerant
consensus  algorithm.
Paxos has been the staple consensus algorithm for industry, upon which
the likes of Amazon [26], Google [10], and others have built out highly avail-
able global Internet services.  The Paxos consensus sits at the bottom of the
application stack,  providing a consistent interface to resource management
and allocation, operating at much slower time scales than the highly-available
applications facing the users.

What is Raft?
In  2013,  Ongaro  and  Ousterhout  published  Raft  [75],  a  state  machine
replication  algorithm  whose  motivating  design  goal  was  understandability.
Rather than starting from a consensus algorithm, and attempting to build
what was needed (ABC), the design of Raft considered first and foremost the
transaction log, and sought orthogonal components which could fit together
to provide what is ultimately ABC, though it is not described as such.