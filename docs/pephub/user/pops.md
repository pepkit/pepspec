# PEPs vs POPs

**Portable Encapsulated Projects (PEPs)** vs **PEP of PEPs (POPs).**

### POPs

POP is simply a group of PEPs represented as a PEP. Users can think of it as a group, collection, or folder of projects. 
It groups PEPs together to represent similar projects, analyses, or related information, making it easier to manage and navigate related proposals.

Each POP can contain other PEPs or POPs (since a POP is a PEP), allowing for a recursive structure. 
This recursive nature enables complex hierarchies and relationships to be efficiently organized within the PEP framework.

### Database structure
In the database POP in represented as a PEP with a special schema, that containing the list of PEPs that are part of the POP.

![POPs](../img/pop.svg)
