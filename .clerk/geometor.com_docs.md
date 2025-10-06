


# GEOMETOR


![_images/splash.png](_images/splash.png)
`geometor.model` is the foundational library for the [GEOMETOR](https://geometor.com) initiative.


At the core of the module is the `Model` class which establishes the field
and methods of operation for creating the geometric constructions while maintaining integrity.


The **field** might be easy to consider as a Cartesian grid. But in reality, it
is an ordered set of information and operations. Points are the information.
Lines and circles are the operations.


In our system, all geometric elements of the `Model` are defined as [Sympy Geometry](https://docs.sympy.org/latest/modules/geometry/index.html)
objects. This means a `Point` can be defined as a pair of any algebraic
[Sympy Expressions](https://docs.sympy.org/latest/tutorials/intro-tutorial/basic_operations.html) that can be evaluated into a floating point value.


`Line` and `Circle` are each defined by two points. So each construction
must begin with at least two given points at the start. As lines and circles
are added, intersection points are discovered with previous lines and circles
and added to the model, so they may be used with new lines and circles.


There are three main operations of the `Model`:


* set\_point
* construct\_line
* construct\_circle


The major responsibilities of the `Model`:


* **deduplicate**


when elements are added to the model, we check to see if they already exist. This is particularly important for intersection points that often coincide with exisitng points.
* **clean values**
* discover **intersections**
* **save** to and load from json
* maintain a set of **related** info for each element:


	+ ancestral relationships
	+ establish labels for elements
	+ classes for styles


All of the plotting functionality has moved to **GEOMETOR** [render](https://github.com/geometor/render). However, there are several report functions in the this module:


* report\_summary
* report\_group\_by\_type
* report\_sequence


![_images/screenshot.png](_images/screenshot.png)

## recent logs


* 23.324 - [First Log - Lots of changes](index.html#document-log/23.324-124954/index)


This log entry marks the commencement of the Geometor.model project. After
extensive changes in recent months, the project’s concepts, though not new, are
entering a phase of significant development. The primary focus has been on
refining the Geometor code, transitioning from the original Geometor Explorer,
which encompassed a broad range of functions, to a more segmented approach.
This segmentation allows for a clearer division of the project’s key
components: modeling, rendering, and analyzing complex geometric constructions.
* 22.348 - [Welcome to GEOMETOR.com](index.html#document-log/22.348-054131)


first log entry for the new system




### mission


Advancing the frontiers of geometric exploration and understanding through innovative Python libraries, pioneering rendering tools, and in-depth studies of the golden ratio, fostering a collaborative and insightful journey into the heart of geometry and its manifestations in nature and mathematics.


* Foster groundbreaking exploration in geometry by developing advanced Python libraries and rendering tools, bridging classical constructions with modern computational power.
* Illuminate the intrinsic patterns and principles of geometry, particularly the golden ratio, revealing their profound implications in natural and mathematical structures.
* Build a collaborative, global community dedicated to continuous innovation, education, and research in the field of geometry, encouraging contributions and discoveries that transcend traditional boundaries.



#### goals


* 23.324 - [First Log - Lots of changes](index.html#document-log/23.324-124954/index)


This log entry marks the commencement of the Geometor.model project. After
extensive changes in recent months, the project’s concepts, though not new, are
entering a phase of significant development. The primary focus has been on
refining the Geometor code, transitioning from the original Geometor Explorer,
which encompassed a broad range of functions, to a more segmented approach.
This segmentation allows for a clearer division of the project’s key
components: modeling, rendering, and analyzing complex geometric constructions.
* 22.348 - [Welcome to GEOMETOR.com](index.html#document-log/22.348-054131)


first log entry for the new system





### usage



#### installation


You can install `geometor.model` using pip:



```
pip install geometor-model

```


or clone this repo and install it directly.



```
git clone https://github.com/geometor/model
cd model
pip install -e .

```





### demos




#### demo




#### vesica






### projects



contents


* [explorer](#explorer)
* [divine](#divine)
* [Euclid](#euclid)




#### explorer


tools for exploring geometric constructions with symbolic algebra




#### divine


explorations into the Divine Proportion




#### Euclid


exploring Euclid’s elements as computational structures





### logs


[*Tags*](log/tag.html "Tags")
[*Categories*](log/category.html "Categories")
[*Drafts*](log/drafts.html "Drafts")
[*Archives*](log/archive.html "Archives")
[*Posts*](log.html "Posts")
[*GEOMETOR Feed*](/log/atom.xml "GEOMETOR Feed")


* 23.324 - [First Log - Lots of changes](index.html#document-log/23.324-124954/index)


This log entry marks the commencement of the Geometor.model project. After
extensive changes in recent months, the project’s concepts, though not new, are
entering a phase of significant development. The primary focus has been on
refining the Geometor code, transitioning from the original Geometor Explorer,
which encompassed a broad range of functions, to a more segmented approach.
This segmentation allows for a clearer division of the project’s key
components: modeling, rendering, and analyzing complex geometric constructions.


[*more*](index.html#document-log/23.324-124954/index)
* 22.348 - [Welcome to GEOMETOR.com](index.html#document-log/22.348-054131)


first log entry for the new system


[*more*](index.html#document-log/22.348-054131)




### references




#### sympy




#### matplotlib




#### textualize






### glossary



Todo


establish glossary entries




examplean example of how to structure a glossary item






### connect




### todos



Todo


establish glossary entries



(The [*original entry*](index.html#id1) is located in /home/phiarchitect/PROJECTS/geometor/geometor.com/docsrc/glossary.rst, line 4.)




### changelog



#### 0.1.0


*2023-11-15*


**fixed**


**added**


**changed**





### about


I have always been deeply interested in architecture and have had the privilege of practicing it in many different domains.


Architecture is order.






## indices


* [Index](genindex.html)
* [Module Index](py-modindex.html)
* [Search Page](search.html)







