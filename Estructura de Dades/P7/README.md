
# Observations about this practice

`15.05.2012`
Finally, I've decided to use a quadratic probing when collisions happen.
Seems to be quite good.

---

`14.05.2012`
Here we have a Python array that indicates the amount of movies with an
integer rating value that ranges from 0 to 100. Each index of the array is a
possible value of rating that a movie may have (`movie.rating * 10`):

```python
[
  0,                   // 00
  0,0,0,0,0,0,0,0,0,0, // 01 - 10
  0,0,0,0,0,0,0,0,0,0, // 11 - 20
  1,0,0,0,0,0,0,0,0,0, // 21 - 30
  0,0,0,0,1,0,0,1,2,1, // 31 - 40
  0,0,1,0,0,1,0,0,3,1, // 41 - 50
  2,4,2,2,2,3,3,3,3,3, // 51 - 60
  4,1,5,5,3,3,2,4,4,4, // 61 - 70
  4,6,1,1,3,2,3,1,0,0, // 71 - 80
  3,0,1,0,0,0,1,0,0,0, // 81 - 90
  0,0,0,0,0,0,0,0,0,0  // 91 - 100
]
```

And here a posh visual representation:

![The chart](http://dl.dropbox.com/u/9123154/EI_ED_P7_000.PNG)

There are some things that can be extracted from the numbers:

* The extremes of the list are almost empty.
* It is obvious that every collision will come from any movie with rating near
the middle.
* There aren't too many gaps between the values.

The practice indicates that the hashtable must have 200 buckets, meaning that 
each rating has two spots where movies can be added. And that is the easy way
to go, if a collision is done and both spots are full, then rehash, advancing
through the structure.

`OBS` I don't think that solving the problem with a fixed bucket size in
mind is a good idea at all. 

`OBS` I believe that using a list-based solution won't be performant wise, as
it is still dependant over the hash function and the amount of buckets 
available, and I think that at the end, it will fragment the lookup, 
increasing it unnecesarily.

But the good thing is that it can overcome the bucket size limit.

`OBS` The average rating of the elements [49, 78] is 2.9. This means that the
amount of buckets needed for each rating would be 3, roughly speaking.
