---
title: 01 • The Mutation Game and a foundational exercise
subtitle: Dynamics on Graphs
date: 06/10/2021
author: /phi
content:
    title: Articles
    items: '@self.children'
taxonomy:
    photon:
    category: 
    tag: 
---



===

> The Mutation Game is a remarkable way of generating a lot of Lie theory and exceptional structures directly from graphs. This is the first video in a series where we explain how this game, and the dual Numbers game of Mozes, explains the ubiquity of the ADE graphs and connects a lot of special mathematical objects and physical theories.
> 
> We end with a really great Exercise / Challenge that in my view is perhaps the very best introduction to Research Level Pure Maths for a general audience. This is a challenge that very well may take you several days or even weeks to tackle, but if you proceed slowly and logically, you can do it!

> This is part of the series: Exceptional Structures in Mathematics and Physics from Dynamics on Graphs
> - [DoG 1: The Mutation Game and a foundational exercise / challenge | Explore Research Maths | Wild Egg - YouTube](https://www.youtube.com/watch?v=u7cUXZHZHEE)
> - Thu Jun 10 2021

------------------------------

> Gianfranco
>
> Funny enough, trying to play the mutation game on a star graph with one central vertex and many  neighbours I got the Fibonacci sequence on the vertices
> - [DoG 1: The Mutation Game and a foundational exercise / challenge | Explore Research Maths | Wild Egg - YouTube](https://www.youtube.com/watch?v=u7cUXZHZHEE)
> - Thu Jun 10 2021

----------------------------------------

> Jaanus Kiipli
> For a vertex value to go up the sum of it's neighbours must be more than twice the value at the vertex. Second thing to observe is that stating from a singleton we can populate any graph with 1 at every vertex. The increasing process gets stuck at the ends of branches. It is easy to see see that cyclical graphs are fee from this problem and thus can grow unboundedly (at the closing of the cycle last vertex value gets bumped up because of meeting the first vertex of the cycle, seeding the next cycle with a bigger value) also it is easy to see that any star- or tree-like structures with more than 3 edges coming out of a vertex can grow unboundedly. A-graphs can have roots with vertex values only 0 or 1. So all of the above pretty much limits the study to graphs which have binary tree like structure.
> - [DoG 1: The Mutation Game and a foundational exercise / challenge | Explore Research Maths | Wild Egg - YouTube](https://www.youtube.com/watch?v=u7cUXZHZHEE)
> - Thu Jun 10 2021

----------------------------------------

> Gianfranco
I agree with Jaanus it’s not so complicated to realise that if there is a cycle, there is a way tom play the game on it in order to produce arbitrary big population. There reduce drastically the graph candidates to trees. Then as Jaanus wrote it’s also easy to see that we cannot have a vertex of degree more than 3. Then we have only to consider binary trees. Moreover, let's call the “degree” of a fork (with at most 3 branches now) the minimum of the length of its branches. An induction argument shows quite easily that this degree cannot be more than 1. 

Moreover, it’s a direct computation to see that you cannot have 2 vertices of degree 3 connected by a path of edges. 

What is remaining?  Essentially “horizontal” chains of edges with eventually somewhere one vertex of degree 3. That looks more and more as ADE graphs. 

For narrowing to the ADE graphs, take a chain with eventually a vertex of degree 3 and by direct computation see that the chain cannot be (surprisingly enough) arbitrary long if there is a vertex of degree 3 but can be arbitrary long if all vertices are of degree 1 or 2.

It remains to see where the degree of degree 3 (if any) must be positioned
> - [DoG 1: The Mutation Game and a foundational exercise / challenge | Explore Research Maths | Wild Egg - YouTube](https://www.youtube.com/watch?v=u7cUXZHZHEE)
> - Thu Jun 10 2021

----------------------------------------

> Peter Hille
Obviously the Mutation Game is a generalisation of the discrete laplace.  The discrete Laplace Operator is obtained by   applying  S operators in a special order. I would like to  outline it here but it is a bit chaotic  posting tex code in these comments. (Is there an other way to write formulas?)
One S operator has Eigenvalues 0, and >1. So we have to find the fixpoints for a sequence of certain S operators. There is no one for Eigenvalues >1 or > -1.  The eigenvalues of a sequence of S depends on the permutations and boundary conditions. Which group represents the S operations? What is the influence fo permutation and structure of the graph on eigenvalues? 
I would like to figure out these questions and  outline all this in mathematical well written text, but I need a hint how to do it here. The noncomutativity of the S is something very interesting, also the treatment on graphs.
> - [DoG 1: The Mutation Game and a foundational exercise / challenge | Explore Research Maths | Wild Egg - YouTube](https://www.youtube.com/watch?v=u7cUXZHZHEE)
> - Thu Jun 10 2021

----------------------------------------

> Wild Egg Maths
Hi Peter, Perhaps "variant of the discrete Laplacian" would be more accurate. In the usual discrete Laplacian, the degrees of the vertices figure, here in the Mutation Game they don't. But they certainly are closely related!
> - [DoG 1: The Mutation Game and a foundational exercise / challenge | Explore Research Maths | Wild Egg - YouTube](https://www.youtube.com/watch?v=u7cUXZHZHEE)
> - Thu Jun 10 2021

----------------------------------------

> @Wild Egg Maths  Ok, I got it. I have to look for Eigenvalues of $p(x) + \Delta p(x)$ not on the Eigenvalues of $\Delta p(x)$ with p Population, with x the set of edges and $\Delta $ the discrete Laplace. So the population is  unchanged, if we have $\Delta p =0$ which means that p is some kind of discrete Laplace potential, depending on the order of S_x  permutations. We have to look for such solutions. I will try first for A_n graphs and look for boundary conditions. The boundary conditions layed out in the video are Dirichlets conditions, there are also Neumann conditions. While Dirichlets conditions are $\delta(p(x_0)) = p(x_1)-2 p(x_0)$   , the Neumann conditions are $\delta(p(x_0)) = p(x_1)- p(x_0)$. This all holds only for A_n with a special order of the mutations S_x.

Because there are various posibilities not only in the shape of the graphs, but also in the permutation of the mutations S_x,  it might be usefull to concentrate on special orders of the S_x. I am not sure what is the right way to shrink these possibilities.
> - [DoG 1: The Mutation Game and a foundational exercise / challenge | Explore Research Maths | Wild Egg - YouTube](https://www.youtube.com/watch?v=u7cUXZHZHEE)
> - Thu Jun 10 2021
