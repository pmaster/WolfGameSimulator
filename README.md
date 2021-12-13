# WolfGameSimulator

Run simulator.py to run a simulation of a very simplified initial version


Current oversimplified rules, 12/13/21

1) The tax rate for a round is the median wolf tax price.

2) Sheep that have signaled a willingness to pay at least this amount, pay the tax and are safe.

3) Sheep that have not signaled a willingness to pay that high of a tax are hit with a fear wool generation modifier for their daily wool generation, and are vulnerable to having their wool from this round stolen by the wolves.

4) All wolves attack all sheep that didn't pay tax.

5) All wolves split the pool of wool from the taxes and attacks evenly.


Need to figure out a prisoner's dilemma for the wolves.

The prisoner's dilemma that currently exists for the sheep is that the sheep are better off collectively if they all pay tax or they all refuse to pay tax.
If sheep plan to protest taxes they perceive to be excessive and not pay them, any sheep that chooses to break the picket line and pay the tax will have higher EV wool production for the round (unless the tax is extremely high).
Further, this will cause the other sheep to be more vulnerable to steals, as they'll lose some degree of safety in numbers.
As the attacking wolf to defending sheep ratio increases, the probability of a successful theft on a given sheep increases faster than linear.

Further, going to add in mechanics that incentivize sheep to hold wool from previous rounds.
Sheep will need to claim their wool (or turn on auto-claim) to harvest their wool from a round.
Sheep holding (and risking) wool from previous rounds will generate extra wool proportional (or better than proportional) to the extra wool they're risking.
Perhaps every round comes with a bonus pot of wool, and sheep get proportional (or better) access to this pot based on their held wool.

More thoughts and mechanics coming.
