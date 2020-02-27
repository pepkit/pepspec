---
title: Create automatic sample groups
redirect_from: "/docs/implied_attributes/"
---

The `imply` modifier lets you set global, group-level attributes at the project level instead of duplicating that information for every sample that belongs to a group of samples. This makes your project more portable and does a better job conceptually with separating sample attributes from project attributes.

### Example

```
sample_modifiers:
  imply:
    - if:
        genome: ["hg18", "hg19", "hg38"]
      then:
        organism: "human"
    - if:
        genome: ["mm9", "mm10"]
      then:
        organism: "mouse"  
    - if:
        organism: ["human", "mouse", "Mouse"]
      then:
        family: "mammal"
    - if:
        organism: ["bird", "jay", "cardinal"]
      then:
        family: "aves"
```

In this example we expect the samples will have existing `genome` attributes. The first and second implications will set an `organism` attribute to either `human` or `mouse`, depending on the value in the `genome` attribute. The next implication then adds a new variable, `family`, with the value `mammal` for any samples with `human` or `mouse` as the `organism`.

We've therefore used implied attributes to automatically create sample groups on the basis of existing attributes. We could then use the value in `family`, for example, to do a differential comparison on these samples. Any new samples added to the table in the original format will immediately work with any downstream tools.



