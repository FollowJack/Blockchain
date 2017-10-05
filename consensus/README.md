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

What is BFT?
The term Byzantine was used due to the similarity of the problem to that faced by generals of the Byzantine army attempting to co-ordinate themselves to attack Rome using only messengers, where one of the generals may be a traitor [61]. In a crash fault, a process simply halts. In a Byzantine fault, it can
behave arbitrarily. Crash faults are easier to handle, as no process can lie to another process. Systems which only tolerate crash faults can operate via simple majority rule, and therefore typically tolerate simultaneous failure of up to half of the system. If the number of failures the system can tolerate is f, such systems must have at least 2f +1 processes. Byzantine failures are more complicated. In a system of 2f +1 processes,
if f are Byzantine, they can co-ordinate to say arbitrary things to the other f + 1 processes. For instance, suppose we are trying to agree on the value of a single bit, and f = 1, so we have N = 3 processes, A, B, and C, where C is Byzantine, as in Figure 2.2. C can tell A that the value is 0 and tell B that it’s 1. If A agrees that its 0, and B agrees that its 1, then they will both think they have a majority and commit, thereby violating the safety condition. Hence, the upper bound on faults tolerated by a Byzantine system is strictly lower than a non-Byzantine one. In fact, it can be shown that the upper limit on f for Byzantine faults
is f < N/3 [78]. Thus, to tolerate a single Byzantine process, we require at least N = 4. Then the faulty process can’t split the vote the way it was able to


At each
height, validators take turns proposing new blocks in rounds, such that for
any given round there is at most one valid proposer.

Proposers are ordered via a simple, deterministic round robin, so only
a single proposer is valid for a given round, and every validator knows the correct proposer. If a proposal is received for a lower round, or from an incorrect proposer, it is rejected.